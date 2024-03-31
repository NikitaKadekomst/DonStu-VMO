from tkinter import *
from utilities.constants import *


# Класс интерфейса для кастомных кнопок управления.
# -------------------------------------------------
# Наследуется от класса Button модуля tkinter.
# -------------------------------------------------
class TransparentButton(Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=FLAT,  # Remove button relief
            highlightthickness=0,  # Remove highlight
            padx=7,  # Add horizontal padding
            pady=7,  # Add vertical padding
            font=("Arial Bold", 10),  # Set font
            foreground="black",  # Text color
            background="#06DDF2",  # Background color
            cursor="hand2"  # Hover cursor
        )
        # Bind events
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)

    # Наведение курсора на кнопку.
    def on_hover(self, event):
        self.config(background="#2DDBEC")

    # Отведение курсора от кнопки.
    def on_leave(self, event):
        self.config(background="#06DDF2")
