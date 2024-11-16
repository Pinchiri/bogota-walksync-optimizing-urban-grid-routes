from typing import Tuple
from utils.constants import *
from GraphManager import GraphManager


def main():
    while True:
        graph_manager = GraphManager()
        javier_graph, andreina_graph = graph_manager.initialize_graphs()

        javier_shortest_paths = javier_graph.dijkstra(
            javier_graph.find_vertex(JAVIER_HOME)
        )

        andreina_shortest_paths = andreina_graph.dijkstra(
            andreina_graph.find_vertex(ANDREINA_HOME)
        )

        andreina_time, andreina_path = andreina_shortest_paths[THE_DARKNESS_CLUB]

        javier_time, javier_path = javier_shortest_paths[THE_DARKNESS_CLUB]
        graph_manager.get_walk_results_str(
            javier_time=javier_time,
            andreina_time=andreina_time,
            javier_path=javier_path,
            andreina_path=andreina_path,
        )

        break


if __name__ == "__main__":
    main()
