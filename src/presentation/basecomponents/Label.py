import customtkinter
from utils.uiconstants import *


class Label(customtkinter.CTkLabel):
    def __init__(
        self,
        master,
        row,
        column,
        font,
        justify="left",
        text="Default",
        text_color="white",
        **kwargs
    ):
        super().__init__(
            master=master,
            justify=justify,
            font=font,
            text=text,
            text_color=text_color,
            **kwargs
        )
        self.grid(row=row, column=column)
