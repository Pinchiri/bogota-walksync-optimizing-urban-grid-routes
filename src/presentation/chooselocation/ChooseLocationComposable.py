import customtkinter
from .ChooseLocationViewModel import ChooseLocationViewModel
from utils.uiconstants import *
from presentation.basecomponents.Button import Button
from presentation.basecomponents.Label import Label
from utils.uiconstants import *
from utils.constants import *
from utils.helpers import *

class ChooseLocationComposable(customtkinter.CTkFrame):
    def __init__(self, master, view_model: ChooseLocationViewModel = ChooseLocationViewModel()):
        super().__init__(master)
        self.view_model = view_model
        
        choose_label = Label(
            master=self,
            text="Elije el destino del encuentro:",
            row=0,
            column=0,
            padx=30,
            pady=10,
            font=create_custom_font(font_size=FONT_SIZE_NORMAL, weight=FONT_WEIGHT_BOLD),
        )
        
        self.location_buttons()
        
        
    
    def location_buttons(self):
        choose_lapasion = Button(
            master=self,
            text=LA_PASION_BAR_STR,
            command=self.view_model.lapasionbar_walk_results(),
            row=1,
            column=0,
            padx=20,
            pady=30,
            font=create_custom_font(font_size=FONT_SIZE_NORMAL, weight=FONT_WEIGHT_BOLD),
            sticky="w",
        )

        choose_the_darkness = Button(
            master=self,
            text=THE_DARKNESS_CLUB_STR,
            command=self.view_model.thedarknessclub_walk_results(),
            row=1,
            column=1,
            padx=20,
            pady=30,
            font=create_custom_font(font_size=FONT_SIZE_NORMAL, weight=FONT_WEIGHT_BOLD),
            sticky="w",
        )
        
        choose_mi_rolita = Button(
            master=self,
            text=MI_ROLITA_BREWERY_STR,
            command=self.view_model.mirolitabrewery_walk_results(),
            row=1,
            column=2,
            padx=20,
            pady=30,
            font=create_custom_font(font_size=FONT_SIZE_NORMAL, weight=FONT_WEIGHT_BOLD),
            sticky="w",
        )
        