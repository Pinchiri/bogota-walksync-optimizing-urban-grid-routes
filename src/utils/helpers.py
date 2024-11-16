import customtkinter
from typing import Literal
from utils.uiconstants import *

def create_custom_font(font_size: int, weight: Literal["normal", "bold"] = "normal"
  ) -> customtkinter.CTkFont:
  return customtkinter.CTkFont(family=FONT_FAMILY, size=font_size, weight=weight)