from typing import Dict, Literal, Tuple
import customtkinter
from utils.helpers import create_custom_font
from utils.uiconstants import *
from utils.constants import *
from presentation.basecomponents.Button import Button
from presentation.basecomponents.Label import Label
from presentation.chooselocation.ChooseLocationComposable import (
    ChooseLocationComposable,
)
from GraphManager import GraphManager

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.setup_window()

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

        self.choose_location_composable(
            graph_manager=graph_manager,
        )

    def choose_location_composable(
        self,
        graph_manager: "GraphManager",
    ):
        choose_locations_frame = ChooseLocationComposable(
            master=self, graph_manager=graph_manager
        )
        choose_locations_frame.grid(row=1, column=0, padx=30, pady=30, sticky="new")

    def setup_window(self):
        self.title(TITLE)
        self.resizable(False, False)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
