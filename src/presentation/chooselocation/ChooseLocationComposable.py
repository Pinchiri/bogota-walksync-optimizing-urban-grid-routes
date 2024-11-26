import customtkinter
from .ChooseLocationViewModel import ChooseLocationViewModel
from utils.uiconstants import *
from presentation.basecomponents.Button import Button
from presentation.basecomponents.Label import Label
from GraphManager import GraphManager
from utils.uiconstants import *
from utils.constants import *
from utils.helpers import *
from presentation.graphvisualizer.GraphVisualizerComposable import GraphVisualizerComposable


class ChooseLocationComposable(customtkinter.CTkFrame):
    def __init__(
        self,
        master,
        graph_manager: "GraphManager",        
    ):
        super().__init__(master)
        self.view_model = ChooseLocationViewModel(graph_manager=graph_manager)                
        #self.graph_visualizer = GraphVisualizerComposable(master=self, graph_manager=graph_manager)

        self.choose_label = Label(
            master=self,
            text="Choose the destination of the meeting:",
            row=0,
            column=0,
            padx=30,
            pady=10,
            font=create_custom_font(
                font_size=FONT_SIZE_NORMAL, weight=FONT_WEIGHT_BOLD
            ),
        )

        self.location_buttons_frame = customtkinter.CTkFrame(master=self)
        self.location_buttons_frame.grid(row=1, column=0, padx=20, pady=30, sticky="ew")

        self.location_buttons()

        self.results_label = Label(
            master=self.location_buttons_frame,
            text="",
            row=0,
            column=3,
            padx=30,
            pady=10,
            font=create_custom_font(
                font_size=FONT_SIZE_NORMAL, weight=FONT_WEIGHT_BOLD
            ),            
        )

    def location_buttons(self):
        self.choose_bar_button = Button(
            master=self.location_buttons_frame,
            text=LA_PASION_BAR_STR,
            command=self.choose_bar_command,
            row=0,
            column=0,
            padx=20,
            pady=30,
            font=create_custom_font(
                font_size=FONT_SIZE_NORMAL, weight=FONT_WEIGHT_BOLD
            ),
            sticky="w",
        )

        self.choose_club_button = Button(
            master=self.location_buttons_frame,
            text=THE_DARKNESS_CLUB_STR,
            command=self.choose_club_command,
            row=0,
            column=1,
            padx=20,
            pady=30,
            font=create_custom_font(
                font_size=FONT_SIZE_NORMAL, weight=FONT_WEIGHT_BOLD
            ),
            sticky="w",
        )

        self.choose_brewery_button = Button(
            master=self.location_buttons_frame,
            text=MI_ROLITA_BREWERY_STR,
            command=self.choose_brewery_command,
            row=0,
            column=2,
            padx=20,
            pady=30,
            font=create_custom_font(
                font_size=FONT_SIZE_NORMAL, weight=FONT_WEIGHT_BOLD
            ),
            sticky="w",
        )

    def choose_bar_command(self):
        self.view_model.calculate_bar_walk_results()
        self.update_results_label(results=self.view_model.bar_results)
        
        javier_path = self.view_model.graph_manager.javier_path
        andreina_path = self.view_model.graph_manager.andreina_path
        self.visualize_graph_composable(javier_path, andreina_path)

    def choose_club_command(self):
        self.view_model.calculate_club_walk_results()
        self.update_results_label(results=self.view_model.club_results)
        
        javier_path = self.view_model.graph_manager.javier_path
        andreina_path = self.view_model.graph_manager.brewery_to_andreina_path
        self.visualize_graph_composable(javier_path, andreina_path)

    def choose_brewery_command(self):
        self.view_model.calculate_brewery_walk_results()
        self.update_results_label(results=self.view_model.brewery_results)

        javier_path = self.view_model.graph_manager.javier_path
        andreina_path = self.view_model.graph_manager.brewery_to_andreina_path
        self.visualize_graph_composable(javier_path, andreina_path)

    def update_results_label(self, results: str):
        self.results_label.configure(text=results)
        self.results_label.update()    
    
    def visualize_graph_composable(self, javier_path, andreina_path):              
        graph_visualizer = GraphVisualizerComposable(master=self, graph_manager=self.view_model.graph_manager, javier_path=javier_path, andreina_path=andreina_path)     
        graph_visualizer.grid(row=2, column=0, padx=30, pady=30, sticky="new")    
