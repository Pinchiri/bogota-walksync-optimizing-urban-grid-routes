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
    def __init__(self, master, graph):
        super().__init__(master=master)
        self.graph = graph
        self.setup_ui()

    def setup_ui(self):
        # Crear un grafo con NetworkX
        G = nx.Graph()
        for vertex_id, neighbors in self.graph.get_adj_matrix().items():
            for neighbor_id, weight in neighbors.items():
                G.add_edge(vertex_id, neighbor_id, weight=weight)

        # Configurar posiciones en cuadrícula según tu esquema
        positions = {}
        for node in G.nodes:
            x, y = node  # Nodo representa (calle, carrera)
            positions[node] = (15 - y, x)  # Carrera define eje X, Calle define eje Y (invertido)

        # Dibujar el grafo con NetworkX y matplotlib
        fig, ax = plt.subplots(figsize=(5, 5))
        nx.draw(
            G,
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
            if loc in G.nodes:
                nx.draw_networkx_nodes(G, positions, nodelist=[loc], node_color=color, node_size=800)

        # Dibujar las etiquetas de los bordes
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, positions, edge_labels=labels, ax=ax)

        # Añadir leyenda fuera del área del gráfico
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=name)
            for _, (name, color) in IMPORTANT_LOCATIONS.items()
        ]
        ax.legend(handles=legend_elements, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

        # Ajustar los márgenes para que la leyenda no tape el gráfico
        plt.subplots_adjust(right=0.75)

        # Integrar el gráfico en el Frame de CustomTkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill="both", expand=True)
