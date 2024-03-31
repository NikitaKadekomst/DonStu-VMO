# Реализация МНК
from tkinter import *
from core.Approximation import *


# Начальное окно приложение с выбором опций для работы.
# -----------------------------------------------------
# Наследуется от класса окна Frame библиотеки tkinter
# -----------------------------------------------------
class ProgramScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # ---------------------------
        #   ОСНОВНОЙ ЗАГОЛОВОК
        # */--------------------------
        self.main_label = Label(self,
                                text="Аппроксимация с помощью полинома n – ой степени",
                                font=("Arial Bold", 14))
        self.main_label.place(relx=0.5, rely=0.08, anchor=CENTER)

    # Очистка содержимого в окне.
    # ---------------------------------------
    # Родительский метод для переопределения
    # в дочерних экранах
    # ---------------------------------------
    def clear(self):
        pass
