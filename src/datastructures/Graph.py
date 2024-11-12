from typing import TYPE_CHECKING 
if TYPE_CHECKING: 
    from .Vertex import Vertex
    from .Edge import Edge

class Graph:
    def __init__(self):
        self.__adj_matrix = {}  # Adjacency Matrix
        self.__vertices = {}
        self.__next_id = 0  # Counter for the next vertex ID

    def add_vertex(self, vertex: 'Vertex'):
        if vertex.get_id() not in self.__vertices:
            self.__vertices[vertex.get_id()] = vertex
            self.__adj_matrix[vertex.get_id()] = {}
        else:
            raise ValueError("Vertex already exists.")

    def add_edge(self, edge: 'Edge'):
        first_id = edge.get_first_vertex().get_id()
        second_id = edge.get_second_vertex().get_id()
        weight = edge.get_weight()

        if first_id not in self.__vertices or second_id not in self.__vertices:
            raise ValueError("Both vertices must be in the graph.")
        
        if second_id in self.__adj_matrix[first_id] and self.__adj_matrix[first_id][second_id] == weight:
            print(f"Edge between {first_id} and {second_id} already exists with weight {weight}.")
            return
        
        if first_id in self.__adj_matrix[second_id] and self.__adj_matrix[second_id][first_id] == weight:
            print(f"Edge between {first_id} and {second_id} already exists with weight {weight}.")
            return

        self.__adj_matrix[first_id][second_id] = weight
        self.__adj_matrix[second_id][first_id] = weight
        
        # Add the edge to both vertices 
        self.__vertices[first_id].add_edge(self.__vertices[second_id], edge)
        self.__vertices[second_id].add_edge(self.__vertices[first_id], edge)

    def find_vertex(self, vertex_id: int):
        return self.__vertices.get(vertex_id, None)

    def get_adj_matrix(self):
        return self.__adj_matrix

    def print_horizontal_edges(self):
        print("Horizontal Edges:")
        for vertex in self.__vertices.values():
            for neighbor_id, edge in vertex.get_edges().items():
                neighbor = self.__vertices[neighbor_id]
                if vertex.get_id()[0] == neighbor.get_id()[0] and vertex.get_id()[1] < neighbor.get_id()[1]:
                    print(edge.get_name() + f" ({edge.get_weight()} minutes)") 

    def print_vertical_edges(self):
        print("Vertical Edges:")
        for vertex in self.__vertices.values():
            for neighbor_id, edge in vertex.get_edges().items():
                neighbor = self.__vertices[neighbor_id]
                if vertex.get_id()[1] == neighbor.get_id()[1] and vertex.get_id()[0] < neighbor.get_id()[0]:
                    print(edge.get_name() + f" ({edge.get_weight()} minutes)")

    def __str__(self):
        output = "Adjacency Matrix:\n"
        for vertex_id, edges in self.__adj_matrix.items():
            output += f"{vertex_id}: {edges}\n"
        return output