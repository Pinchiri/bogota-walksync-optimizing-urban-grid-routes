from typing import TYPE_CHECKING, Dict, List, Tuple
from Config import Config
from utils.constants import *
from datastructures.Vertex import Vertex
from datastructures.Edge import Edge
from datastructures.Graph import Graph


class GraphManager:
    def __init__(self, config: "Config"):
        self.config = config
        self.javier_graph: Graph = None
        self.andreina_graph: Graph = None
        self.andreina_shortest_paths: Dict[int, Tuple[int, list]] = {}
        self.javier_shortest_paths: Dict[int, Tuple[int, list]] = {}
        self.club_shortest_paths: Dict[int, Tuple[int, list]] = {}
        self.brewery_shortest_paths: Dict[int, Tuple[int, list]] = {}
        self.bar_shortest_paths: Dict[int, Tuple[int, list]] = {}
        self.andreina_path = []
        self.javier_path = []
        self.andreina_time = ZERO_INT
        self.javier_time = ZERO_INT

    def get_bar_results(self) -> str:
        self.javier_time, self.javier_path = self.javier_shortest_paths[
            self.config.LA_PASION_BAR
        ]
        self.andreina_time, self.andreina_path = self.andreina_shortest_paths[
            self.config.LA_PASION_BAR
        ]
        bar_results = self.get_walk_results_str(
            javier_time=self.javier_time,
            andreina_time=self.andreina_time,
            javier_path=self.javier_path,
            andreina_path=self.andreina_path,
        )

        return bar_results

    def get_club_results(self) -> str:
        self.javier_time, self.javier_path = self.javier_shortest_paths[
            self.config.THE_DARKNESS_CLUB
        ]
        self.andreina_time, self.club_to_andreina_path = self.club_shortest_paths[
            self.config.ANDREINA_HOME
        ]
        andreina_path = list(reversed(self.club_to_andreina_path))

        club_results = self.get_walk_results_str(
            javier_time=self.javier_time,
            andreina_time=self.andreina_time,
            javier_path=self.javier_path,
            andreina_path=andreina_path,
        )

        return club_results

    def get_brewery_results(self) -> str:
        self.javier_time, self.javier_path = self.javier_shortest_paths[
            self.config.MI_ROLITA_BREWERY
        ]
        self.andreina_time, self.club_to_andreina_path = self.brewery_shortest_paths[
            self.config.ANDREINA_HOME
        ]
        andreina_path = list(reversed(self.club_to_andreina_path))

        brewery_results = self.get_walk_results_str(
            javier_time=self.javier_time,
            andreina_time=self.andreina_time,
            javier_path=self.javier_path,
            andreina_path=andreina_path,
        )

        return brewery_results

    def get_walk_results_str(
        self,
        javier_time: int,
        andreina_time: int,
        javier_path: List[Tuple[int, int]],
        andreina_path: List[Tuple[int, int]],
    ) -> str:
        time_difference = self.calculate_time_difference(javier_time, andreina_time)

        results_str = f"""
        Javier's time: {javier_time} minutes
        Andreina's time: {andreina_time} minutes
        Javier's path: {self.get_path_str(javier_path)}
        Andreina's path: {self.get_path_str(andreina_path)}
        Time difference: {abs(time_difference)} minutes
        """

        if time_difference > 0:
            results_str += f"Javier has to leave {time_difference} minutes earlier\n"
        elif time_difference < 0:
            results_str += (
                f"Andreina has to leave {abs(time_difference)} minutes earlier\n"
            )
        else:
            results_str += "Both have to leave at the same time\n"

        return results_str

    def calculate_time_difference(self, javier_time: int, andreina_time: int) -> int:
        return javier_time - andreina_time

    def get_path_str(self, path: list) -> str:
        return " -> ".join(map(str, path))

    def initialize_graphs(self) -> Tuple["Graph", "Graph"]:
        self.javier_graph = self.create_javier_graph()
        self.andreina_graph = self.create_andreina_graph()
        self.calculate_shortest_paths()
        return self.javier_graph, self.andreina_graph

    def calculate_shortest_paths(self):
        self.javier_shortest_paths = self.javier_graph.dijkstra(
            self.javier_graph.find_vertex(self.config.JAVIER_HOME)
        )

        self.andreina_shortest_paths = self.andreina_graph.dijkstra(
            self.andreina_graph.find_vertex(self.config.ANDREINA_HOME)
        )

        self.club_shortest_paths = self.andreina_graph.dijkstra(
            self.andreina_graph.find_vertex(self.config.THE_DARKNESS_CLUB)
        )

        self.brewery_shortest_paths = self.javier_graph.dijkstra(
            self.javier_graph.find_vertex(self.config.MI_ROLITA_BREWERY)
        )

        self.bar_shortest_paths = self.javier_graph.dijkstra(
            self.javier_graph.find_vertex(self.config.LA_PASION_BAR)
        )

    def create_javier_graph(self) -> "Graph":
        graph = Graph(self.config.GRAPH_SIZE)

        self.create_graph_vertices(graph=graph)

        self.create_graph_edges(
            graph=graph,
            speed=self.config.JAVIER_SPEED,
            speed_bad_shape=self.config.JAVIER_SPEED_BAD_SHAPE,
            speed_c51=self.config.JAVIER_SPEED_C51,
        )

        return graph

    def create_andreina_graph(self) -> "Graph":
        graph = Graph(self.config.GRAPH_SIZE)

        self.create_graph_vertices(graph=graph)

        self.create_graph_edges(
            graph=graph,
            speed=self.config.ANDREINA_SPEED,
            speed_bad_shape=self.config.ANDREINA_SPEED_BAD_SHAPE,
            speed_c51=self.config.ANDREINA_SPEED_C51,
        )

        return graph

    def create_graph_vertices(self, graph: "Graph"):
        for avenue in range(self.config.FIRST_STREET, self.config.LAST_STREET + 1):
            for street in range(self.config.FIRST_AVENUE, self.config.LAST_AVENUE + 1):
                vertex_id, vertex_name = self.check_important_location(
                    avenue=avenue, street=street
                )
                vertex = Vertex(vertex_id=vertex_id, name=vertex_name)
                graph.add_vertex(vertex)

    def create_graph_edges(
        self, graph: "Graph", speed: int, speed_bad_shape: int, speed_c51: int
    ):
        for street in range(self.config.FIRST_STREET, self.config.LAST_STREET + 1):
            for avenue in range(self.config.FIRST_AVENUE, self.config.LAST_AVENUE + 1):
                v1 = graph.find_vertex(vertex_id=(street, avenue))

                # Horizontal edges
                if avenue < self.config.LAST_AVENUE:
                    v2 = graph.find_vertex(vertex_id=(street, avenue + 1))
                    weight = (
                        speed_c51
                        if street == self.config.HIGH_TRAFFIC_STREET
                        else speed
                    )
                    edge_name = f"C{street} - C{avenue} to C{avenue + 1}"
                    graph.add_edge(
                        Edge(
                            first_vertex=v1,
                            second_vertex=v2,
                            weight=weight,
                            name=edge_name,
                            type_int=0,
                            type_name=HORIZONTAL_TYPE_NAME_EDGE,
                        )
                    )

                # Vertical edges
                if street < self.config.LAST_STREET:
                    v2 = graph.find_vertex(vertex_id=(street + 1, avenue))
                    weight = (
                        speed_bad_shape
                        if avenue >= self.config.BEGINNING_AVENUE_BAD_SHAPE
                        and avenue <= self.config.END_AVENUE_BAD_SHAPE
                        else speed
                    )
                    edge_name = f"C{street} to C{street + 1} - C{avenue}"
                    graph.add_edge(
                        Edge(
                            first_vertex=v1,
                            second_vertex=v2,
                            weight=weight,
                            name=edge_name,
                            type_int=1,
                            type_name=VERTICAL_TYPE_NAME_EDGE,
                        )
                    )

    def check_important_location(self, avenue: int, street: int) -> Tuple[int, str]:
        vertex_id = (avenue, street)
        default_name = f"C{avenue} -- C{street}"
        vertex_name = self.config.LOCATION_MAP.get(vertex_id, default_name)
        return vertex_id, vertex_name
