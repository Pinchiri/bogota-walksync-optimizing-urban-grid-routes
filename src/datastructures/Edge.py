from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Vertex import Vertex


class Edge:
    def __init__(
        self,
        first_vertex: "Vertex",
        second_vertex: "Vertex",
        weight: int,
        name: str,
        type_int: int,
        type_name: str,
    ):
        self.__first_vertex = first_vertex
        self.__second_vertex = second_vertex
        self.__weight = weight
        self.__name = name
        self.__type_int = type_int  # Horizontal (0) or Vertical (1)
        self.__type_name = type_name  # Horizontal or Vertical

    def get_first_vertex(self) -> "Vertex":
        return self.__first_vertex

    def get_second_vertex(self) -> "Vertex":
        return self.__second_vertex

    def get_weight(self) -> int:
        return self.__weight

    def get_name(self) -> str:
        return self.__name

    def get_type_int(self) -> int:
        return self.__type_int

    def get_type_name(self) -> str:
        return self.__type_name

    def __str__(self):
        return (
            str(self.__name)
            + " ("
            + str(self.__weight)
            + ") "
            + " -> "
            + str(self.__second_vertex)
            + ", "
            + str(self.__second_vertex)
        )
