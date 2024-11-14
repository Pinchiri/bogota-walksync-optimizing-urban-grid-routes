from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from .Edge import Edge


class Vertex:
    def __init__(self, vertex_id: int, name: str):
        self.__vertex_id = vertex_id
        self.__name = name
        self.__edges = {}  # Dictionary of Edges

    def add_edge(self, neighbor: "Vertex", edge: "Edge"):
        self.__edges[neighbor.get_vertex_id()] = edge

    def get_name(self) -> str:
        return self.__name

    def get_edges(self) -> Dict[int, "Edge"]:
        return self.__edges

    def get_vertex_id(self) -> int:
        return self.__vertex_id

    def __str__(self):
        return self.__vertex_id + ": " + self.__name
