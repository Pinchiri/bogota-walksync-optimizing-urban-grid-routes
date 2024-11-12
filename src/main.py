import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils.constants import *
from datastructures.Vertex import Vertex
from datastructures.Edge import Edge
from datastructures.Graph import Graph


def main():
    while True:
        vertex_id_counter = 0
        # Example usage
        graph = create_javier_graph()
        graph.print_horizontal_edges()
        graph.print_vertical_edges()
        break
        
def initialize_graphs():
    print("hola")
    
def create_javier_graph():
    graph = Graph()

    # Create vertices
    for street in range(50, 55):
        for avenue in range(10, 15):
            vertex = Vertex(id = (street, avenue), 
                            name = f"C{street} -- C{avenue}"
                            )
            graph.add_vertex(vertex)

    # Create edges
    for street in range(50, 55):
        for avenue in range(10, 15):
            v1 = graph.find_vertex(vertex_id = (street, avenue))
            
            # Horizontal edges
            if avenue < 14:
                v2 = graph.find_vertex(vertex_id = (street, avenue + 1))
                weight = JAVIER_SPEED_BAD_SHAPE if avenue >= 12 else JAVIER_SPEED
                edge_name = f"C{street} - C{avenue} to C{avenue + 1}"
                graph.add_edge(Edge( 
                                    first_vertex = v1, 
                                    second_vertex = v2, 
                                    weight = weight, 
                                    name = edge_name
                                    )
                               )
            
            # Vertical edges
            if street < 54:
                v2 = graph.find_vertex(vertex_id = (street + 1, avenue))
                weight = JAVIER_SPEED_C51 if street == 51 else JAVIER_SPEED
                edge_name = f"C{street} to C{street + 1} - C{avenue}"
                graph.add_edge(Edge( 
                                    first_vertex = v1, 
                                    second_vertex = v2, 
                                    weight = weight, 
                                    name = edge_name
                                    )
                               )

    return graph



if __name__ == "__main__":
    main()
