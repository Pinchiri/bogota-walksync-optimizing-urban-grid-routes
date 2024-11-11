from src.datastructures.Vertex import Vertex
from src.datastructures.Edge import Edge

class Graph:
    def __init__(self):
        self.__adj_matrix = {} # Adjacency Matrix
        self.__vertices = {}

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

        self.__adj_matrix[first_id][second_id] = weight
        self.__adj_matrix[second_id][first_id] = weight
        
        # Add the edge to both vertices 
        self.__vertices[first_id].add_edge(self.__vertices[second_id], edge) 
        self.__vertices[second_id].add_edge(self.__vertices[first_id], edge)

    def find_vertex(self, vertex_id: int):
        return self.__vertices.get(vertex_id, None)

    def get_adj_matrix(self):
        return self.__adj_matrix

    def __str__(self):
        output = "Adjacency Matrix:\n"
        for vertex_id, edges in self.__adj_matrix.items():
            output += f"{vertex_id}: {edges}\n"
        return output