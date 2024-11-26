from typing import Dict, Tuple
import customtkinter
from Config import Config
from utils.helpers import create_custom_font
from utils.uiconstants import FONT_SIZE_TITLE, FONT_WEIGHT_BOLD
from GraphManager import GraphManager
from presentation.basecomponents.Label import Label
from presentation.chooselocation.ChooseLocationComposable import (
    ChooseLocationComposable,
)
from presentation.graphvisualizer.GraphVisualizerComposable import (
    GraphVisualizerComposable,
)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.config = Config("config.ini")
        self.setup_window()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        graph_manager = GraphManager(config=self.config)
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

        # Create a canvas and a frame
        self.canvas = customtkinter.CTkCanvas(self)
        self.scrollable_frame = customtkinter.CTkFrame(self.canvas)

        self.scrollbar_vert = customtkinter.CTkScrollbar(
            master=self, command=self.canvas.yview, orientation="vertical"
        )
        self.scrollbar_horiz = customtkinter.CTkScrollbar(
            master=self, command=self.canvas.xview, orientation="horizontal"
        )

        self.canvas.configure(yscrollcommand=self.scrollbar_vert.set)
        self.canvas.configure(xscrollcommand=self.scrollbar_horiz.set)

        self.scrollbar_vert.grid(row=0, column=1, sticky="ns")
        self.scrollbar_horiz.grid(row=1, column=0, sticky="ew")

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Marco para seleccionar la ubicación
        self.choose_location_composable(graph_manager=graph_manager)

        # Marco para visualizar el grafo
        self.visualize_graph_composable(graph_manager=graph_manager)

    def on_close(self):
        self.quit()
        self.destroy()

    def visualize_graph_composable(
        self,
        graph_manager: "GraphManager",
    ):
        graph_visualizer = GraphVisualizerComposable(
            master=self.scrollable_frame, graph_manager=graph_manager
        )
        graph_visualizer.grid(row=2, column=0, padx=30, pady=30, sticky="new")

    def choose_location_composable(
        self,
        graph_manager: "GraphManager",
    ):
        choose_locations_frame = ChooseLocationComposable(
            master=self.scrollable_frame, graph_manager=graph_manager
        )
        choose_locations_frame.grid(row=1, column=0, padx=30, pady=30, sticky="new")

    def setup_window(self):
        self.title("Bogotá WalkSync")
        self.attributes("-fullscreen", True)  # Start the app in fullscreen mode
        self.bind(
            "<Escape>", self.exit_fullscreen
        )  # Bind the Escape key to exit fullscreen

    def exit_fullscreen(self, event=None):
        self.attributes("-fullscreen", False)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
