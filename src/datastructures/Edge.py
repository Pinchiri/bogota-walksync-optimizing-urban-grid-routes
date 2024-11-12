from typing import TYPE_CHECKING 
if TYPE_CHECKING:   
  from .Vertex import Vertex

class Edge:
  def __init__(self, first_vertex: 'Vertex', second_vertex: 'Vertex', weight: int, name: str):
    self.__first_vertex = first_vertex
    self.__second_vertex = second_vertex
    self.__weight = weight
    self.__name = name
    
  def get_first_vertex(self):
    return self.__first_vertex
  
  def get_second_vertex(self):
    return self.__second_vertex
  
  def get_weight(self):
    return self.__weight
  
  def get_name(self):
    return self.__name
  
  def __str__(self):
    return str(self.__name)+ " (" + str(self.__weight) + ") " + " -> " + str(self.__second_vertex) + ", " + str(self.__second_vertex)  