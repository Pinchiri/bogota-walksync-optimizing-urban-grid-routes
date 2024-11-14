from utils.constants import *
from datastructures.Vertex import Vertex
from datastructures.Edge import Edge
from datastructures.Graph import Graph


def main():
    while True:

        javier_graph = create_javier_graph()
        javier_graph.print_horizontal_edges()
        javier_graph.print_vertical_edges()

        andreina_graph = create_andreina_graph()
        break


def initialize_graphs():
    print("hola")


def create_javier_graph() -> "Graph":
    graph = Graph(GRAPH_SIZE)

    # Create vertices
    create_graph_vertices(graph=graph)

    # Create edges
    create_graph_edges(
        graph=graph,
        speed=JAVIER_SPEED,
        speed_bad_shape=JAVIER_SPEED_BAD_SHAPE,
        speed_c51=JAVIER_SPEED_C51,
    )

    return graph


def create_andreina_graph() -> "Graph":
    graph = Graph(GRAPH_SIZE)

    # Create vertices
    create_graph_vertices(graph=graph)

    # Create edges
    create_graph_edges(
        graph=graph,
        speed=ANDREINA_SPEED,
        speed_bad_shape=ANDREINA_SPEED_BAD_SHAPE,
        speed_c51=ANDREINA_SPEED_C51,
    )

    return graph


def create_graph_vertices(graph: "Graph"):
    for avenue in range(GRAPH_AVENUE_LOW_LIMIT, GRAPH_AVENUE_HIGH_LIMIT):
        for street in range(GRAPH_STREET_LOW_LIMIT, GRAPH_STREET_HIGH_LIMIT):
            vertex = Vertex(vertex_id=(avenue, street), name=f"C{avenue} -- C{street}")
            graph.add_vertex(vertex)


def create_graph_edges(
    graph: "Graph", speed: int, speed_bad_shape: int, speed_c51: int
):
    for avenue in range(GRAPH_AVENUE_LOW_LIMIT, GRAPH_AVENUE_HIGH_LIMIT):
        for street in range(GRAPH_STREET_LOW_LIMIT, GRAPH_STREET_HIGH_LIMIT):
            v1 = graph.find_vertex(vertex_id=(avenue, street))

            # Horizontal edges
            if street < LAST_STREET:
                v2 = graph.find_vertex(vertex_id=(avenue, street + 1))
                weight = speed_c51 if avenue == HIGH_TRAFFIC_AVENUE else speed
                edge_name = f"C{avenue} - C{street} to C{street + 1}"
                graph.add_edge(
                    Edge(
                        first_vertex=v1,
                        second_vertex=v2,
                        weight=weight,
                        name=edge_name,
                        type_int=0,
                        type_name="Horizontal",
                    )
                )

            # Vertical edges
            if avenue < LAST_AVENUE:
                v2 = graph.find_vertex(vertex_id=(avenue + 1, street))
                weight = (
                    speed_bad_shape if street >= BEGINNING_STREET_BAD_SHAPE else speed
                )
                edge_name = f"C{avenue} to C{avenue + 1} - C{street}"
                graph.add_edge(
                    Edge(
                        first_vertex=v1,
                        second_vertex=v2,
                        weight=weight,
                        name=edge_name,
                        type_int=1,
                        type_name="Vertical",
                    )
                )


if __name__ == "__main__":
    main()
