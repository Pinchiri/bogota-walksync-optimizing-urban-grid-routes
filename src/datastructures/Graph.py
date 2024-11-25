from typing import TYPE_CHECKING, Dict, Tuple

from datastructures.BinaryHeap import BinaryHeap

if TYPE_CHECKING:
    from .Vertex import Vertex
    from .Edge import Edge


class Graph:
    def __init__(self, size: int):
        self.__adj_matrix = {}  # Adjacency Matrix
        self.__vertices = {}
        self.__size = size

    def add_vertex(self, vertex: "Vertex"):
        if vertex.get_vertex_id() not in self.__vertices:
            self.__vertices[vertex.get_vertex_id()] = vertex
            self.__adj_matrix[vertex.get_vertex_id()] = {}
        else:
            raise ValueError("Vertex already exists.")

    def add_edge(self, edge: "Edge"):
        first_id = edge.get_first_vertex().get_vertex_id()
        second_id = edge.get_second_vertex().get_vertex_id()
        weight = edge.get_weight()

        if first_id not in self.__vertices or second_id not in self.__vertices:
            raise ValueError("Both vertices must be in the graph.")

        if (
            second_id in self.__adj_matrix[first_id]
            and self.__adj_matrix[first_id][second_id] == weight
        ):
            print(
                f"Edge between {first_id} and {second_id} already exists with weight {weight}."
            )
            return

        if (
            first_id in self.__adj_matrix[second_id]
            and self.__adj_matrix[second_id][first_id] == weight
        ):
            print(
                f"Edge between {first_id} and {second_id} already exists with weight {weight}."
            )
            return

        self.__adj_matrix[first_id][second_id] = weight
        self.__adj_matrix[second_id][first_id] = weight

        # Add the edge to both vertices
        self.__vertices[first_id].add_edge(self.__vertices[second_id], edge)
        self.__vertices[second_id].add_edge(self.__vertices[first_id], edge)

    def find_vertex(self, vertex_id: int) -> "Vertex":
        return self.__vertices.get(vertex_id, None)

    def dijkstra(self, start_vertex: "Vertex") -> Dict[int, Tuple[int, list]]:
        """
        Implements Dijkstra's algorithm to find the shortest path from the start vertex to all other vertices.
        Returns a dictionary with vertex Tuple IDs as keys and a Tuple (distance, path) as values.
        """
        bheap = BinaryHeap()
        bheap.heappush(
            (0, start_vertex.get_vertex_id(), [])  # (distance, vertex_id, path)
        )

        times = {vertex_id: float("inf") for vertex_id in self.__vertices}
        previous_vertices = {vertex_id: None for vertex_id in self.__vertices}
        times[start_vertex.get_vertex_id()] = 0

        while bheap:
            # Pop the vertex with the smallest distance
            current_time, current_vertex_id, path = bheap.heappop()

            if current_time > times[current_vertex_id]:
                continue

            # Update the path for the current vertex
            new_path = path + [current_vertex_id]

            # Check all neighbors of the current vertex
            for neighbor_id, weight in self.__adj_matrix[current_vertex_id].items():
                time = current_time + weight

                # If a shorter path is found, update the distance and queue
                if time < times[neighbor_id]:
                    times[neighbor_id] = time
                    previous_vertices[neighbor_id] = current_vertex_id
                    bheap.heappush((time, neighbor_id, new_path))

        # Reconstruct the shortest paths
        shortest_paths = {}
        for vertex_id in self.__vertices:
            if times[vertex_id] != float("inf"):
                shortest_paths[vertex_id] = (
                    times[vertex_id],
                    self._reconstruct_path(previous_vertices, vertex_id),
                )

        return shortest_paths

    def _reconstruct_path(
        self, previous_vertices: Dict[int, int], vertex_id: int
    ) -> list:
        """Reconstructs the shortest path to a vertex."""
        path = []
        while vertex_id is not None:
            path.insert(0, vertex_id)
            vertex_id = previous_vertices[vertex_id]
        return path

    def print_shortest_path(
        self, shortest_paths: Dict[int, Tuple[int, list]], target_vertex_id: int
    ):
        """
        Prints the shortest path to the given target vertex ID along with its total distance.
        The shortest_paths dictionary is expected to be the result of dijkstra().
        """
        if target_vertex_id not in shortest_paths:
            print(f"No path found to vertex {target_vertex_id}.")
            return

        # Get the distance and path from the shortest_paths dictionary
        distance, path = shortest_paths[target_vertex_id]

        # Print the result
        print(f"Shortest path to vertex {target_vertex_id}:")
        print(" -> ".join(map(str, path)))
        print(f"Total distance: {distance} minutes")

    def print_all_shortest_paths(self, shortest_paths: Dict[int, Tuple[int, list]]):
        """
        Prints the shortest paths to all vertices along with their total distances.
        The shortest_paths dictionary is expected to be the result of dijkstra().
        """
        print("All Shortest Paths:")
        for vertex_id, (distance, path) in shortest_paths.items():
            path_str = " -> ".join(map(str, path))
            print(
                f"To Vertex {vertex_id}: Path = {path_str}, Total Distance = {distance} minutes"
            )

    def print_horizontal_edges(self):
        print("Horizontal Edges:")
        for vertex in self.__vertices.values():
            vertex: Vertex
            for neighbor_id, edge in vertex.get_edges().items():
                if edge.get_type_int() == 0:  # Check if the edge is horizontal
                    print(edge.get_name() + f" ({edge.get_weight()} minutes)")

    def print_vertical_edges(self):
        print("Vertical Edges:")
        for vertex in self.__vertices.values():
            vertex: Vertex
            for neighbor_id, edge in vertex.get_edges().items():
                if edge.get_type_int() == 1:  # Check if the edge is vertical
                    print(edge.get_name() + f" ({edge.get_weight()} minutes)")

    def print_vertices(self):
        print("Vertices:")
        for vertex_id, vertex in self.__vertices.items():
            vertex: Vertex
            print(f"Vertex ID: {vertex_id}, Vertex Name: {vertex.get_name()}")

    def get_size(self) -> int:
        return self.__size

    def get_adj_matrix(self) -> Dict[tuple, Dict[tuple, int]]:
        return self.__adj_matrix

    def __str__(self):
        output = "Adjacency Matrix:\n"
        for vertex_id, edges in self.__adj_matrix.items():
            output += f"{vertex_id}: {edges}\n"
        return output
