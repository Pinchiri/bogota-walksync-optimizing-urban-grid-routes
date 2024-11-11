from src.datastructures.Edge import Edge

class Vertex:
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name
        self.__edges = {} # Dictionary of Edges 
        
    def add_edge(self, neighbor: 'Vertex', edge: 'Edge'): 
        self.__edges[neighbor.get_id()] = edge
    
    def get_name(self):
        return self.__name
    
    def get_edges(self):
        return self.__edges
    
    def get_id(self):
        return self.__id
        
    def __str__(self):
        return self.__id + ": " + self.__name