import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter
import networkx as nx

# Ubicaciones importantes con colores y nombres
IMPORTANT_LOCATIONS = {
    (54, 14): ("Javier Home", "red"),
    (52, 13): ("Andreina Home", "green"),
    (50, 14): ("The Darkness Club", "blue"),
    (54, 11): ("La Pasion Bar", "orange"),
    (50, 12): ("Mi Rolita Brewery", "purple"),
}

class GraphVisualizerComposable(customtkinter.CTkFrame):
    def __init__(self, master, graph_manager: "GraphManager", javier_path=None, andreina_path=None):
        super().__init__(master=master)
        self.graph1 = graph_manager.javier_graph
        self.graph2 = graph_manager.andreina_graph
        self.javier_path = javier_path
        self.andreina_path = andreina_path

        

        self.setup_ui()

    def setup_ui(self):
        # Crear el grafo con NetworkX para el primer gráfico
        G1 = nx.Graph()
        for vertex_id, neighbors in self.graph1.get_adj_matrix().items():
            for neighbor_id, weight in neighbors.items():
                G1.add_edge(vertex_id, neighbor_id, weight=weight)
        positions1 = self.get_positions(G1)

        # Crear el grafo con NetworkX para el segundo gráfico
        G2 = nx.Graph()
        for vertex_id, neighbors in self.graph2.get_adj_matrix().items():
            for neighbor_id, weight in neighbors.items():
                G2.add_edge(vertex_id, neighbor_id, weight=weight)
        positions2 = self.get_positions(G2)

        # Dibujar el primer gráfico
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        self.draw_graph(G1, positions1, ax1, self.javier_path)
        ax1.set_title("Javier")  # Título del primer gráfico

        # Dibujar el segundo gráfico
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        self.draw_graph(G2, positions2, ax2, self.andreina_path)
        ax2.set_title("Andreina")  # Título del segundo gráfico

        # Crear los canvas para ambos gráficos
        self.canvas1 = FigureCanvasTkAgg(fig1, master=self)
        self.canvas_widget1 = self.canvas1.get_tk_widget()

        self.canvas2 = FigureCanvasTkAgg(fig2, master=self)
        self.canvas_widget2 = self.canvas2.get_tk_widget()

        # Usar grid para colocar los gráficos en el mismo Frame
        self.canvas_widget1.grid(row=0, column=0, padx=10, pady=10)
        self.canvas_widget2.grid(row=0, column=1, padx=10, pady=10)

    def get_positions(self, graph):
        # Configurar posiciones en cuadrícula según tu esquema
        positions = {}
        for node in graph.nodes:
            x, y = node
            positions[node] = (15 - y, x)  # Carrera define eje X, Calle define eje Y (invertido)
        return positions

    def draw_graph(self, graph, positions, ax, path=None):
        nx.draw(
            graph,
            positions,
            with_labels=True,
            node_color="skyblue",
            node_size=500,
            edge_color="gray",
            font_size=8,
            font_color="black",
            ax=ax,
        )

        # Dibujar las ubicaciones importantes
        for loc, (name, color) in IMPORTANT_LOCATIONS.items():
            if loc in graph.nodes:
                nx.draw_networkx_nodes(graph, positions, nodelist=[loc], node_color=color, node_size=800)

        # Dibujar las etiquetas de los bordes
        labels = nx.get_edge_attributes(graph, "weight")
        nx.draw_networkx_edge_labels(graph, positions, edge_labels=labels, ax=ax)

        # Resaltar el camino si se proporciona
        if path:
            edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(graph, positions, edgelist=edges, edge_color="red", width=2, ax=ax)

        # Añadir leyenda fuera del área del gráfico
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=name)
            for _, (name, color) in IMPORTANT_LOCATIONS.items()
        ]
        ax.legend(handles=legend_elements, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

        # Ajustar los márgenes para que la leyenda no tape el gráfico
        plt.subplots_adjust(right=0.75)
