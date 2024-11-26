from typing import Dict, Tuple
import customtkinter
from utils.helpers import create_custom_font
from utils.uiconstants import FONT_SIZE_TITLE, FONT_WEIGHT_BOLD
from utils.constants import JAVIER_HOME, ANDREINA_HOME
from GraphManager import GraphManager
from presentation.basecomponents.Label import Label
from presentation.chooselocation.ChooseLocationComposable import ChooseLocationComposable
from presentation.graphvisualizer.GraphVisualizerComposable import GraphVisualizerComposable

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.setup_window()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        graph_manager = GraphManager()
        graph_manager.initialize_graphs()

        self.main_title = Label(
            master=self,
            text="Bogotá WalkSync",
            row=0,
            column=0,
            padx=30,
            pady=15,
            font=create_custom_font(font_size=FONT_SIZE_TITLE, weight=FONT_WEIGHT_BOLD),
        )

        # Marco para visualizar el grafo
        self.visualize_graph_composable(graph_manager=graph_manager)

        # Marco para seleccionar la ubicación
        self.choose_location_composable(graph_manager=graph_manager)   

    def on_close(self):
        # Método para manejar el cierre de la ventana correctamente        
        self.destroy()  # Destruye la ventana y limpia los recursos     

    def visualize_graph_composable(self, graph_manager: "GraphManager",):
        graph_visualizer = GraphVisualizerComposable(master=self, graph_manager=graph_manager)
        #graph_visualizer.grid(row=2, column=0, padx=30, pady=30, sticky="nsew")

        #graph_visualizer = GraphVisualizerComposable(master=self, graph=graph_manager.andreina_graph)
        graph_visualizer.grid(row=2, column=0, padx=30, pady=30, sticky="new")        
       

    def choose_location_composable(
        self,
        graph_manager: "GraphManager",        
    ):
        choose_locations_frame = ChooseLocationComposable(
            master=self, graph_manager=graph_manager
        )
        choose_locations_frame.grid(row=1, column=0, padx=30, pady=30, sticky="new")

    def setup_window(self):
        self.title("Bogotá WalkSync")
        self.resizable(False, False)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
