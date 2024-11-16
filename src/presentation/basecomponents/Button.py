import customtkinter
from utils.uiconstants import *


class Button(customtkinter.CTkButton):
    def __init__(self, master, text, command, font, **kwargs):
        super().__init__(master, text=text, command=command, font=font)
        self.grid(**kwargs)
