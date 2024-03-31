from tkinter import *

# Экраны приложения.
from gui.screens.FileImportScreen import FileImportScreen as FileImportScreenCLS
from gui.screens.ResultScreen import ResultScreen as ResultScreenCLS


# Основной класс интерфейса.
# ------------------------------------------------------
# Входная точка в интерфейс.
# Управляет сменой экранов в приложении.
# Наследуется от основного класса Tk библиотеки tkinter.
# ------------------------------------------------------
class GUI(Tk):
    def __init__(self, width, height, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # Размеры окна.
        self.w_width = width
        self.w_height = height

        # Базовые настройки окна.
        self.title("Аппроксимация с помощью полинома n – ой степени")

        # Задаем иконку.
        self.icon = PhotoImage(file="images/calculator.png")
        self.iconphoto(False, self.icon)

        # Задание размеров окна.
        self.geometry(f"{self.w_width}x{self.w_height}")

        # Создание базового контейнера.
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Словарь для хранения объектов страниц приложения.
        self.frames = {}

        # Кортеж всех страниц приложения.
        self.screens = (FileImportScreenCLS,
                        ResultScreenCLS)

        # При запуске приложения отображается
        # экран настроек и импорта файла.
        self.show_frame(FileImportScreenCLS)

    # GUI.back_to_settings()
    # --------------------------------------------
    # Настройки для возврата с экрана результата
    # на экран настроек.
    # --------------------------------------------
    def back_to_settings(self):
        self.frames[ResultScreenCLS].forget()
        self.frames[FileImportScreenCLS].tkraise()
        self.frames[FileImportScreenCLS].show_entries()

    # GUI.show_frame(scr, data)
    # --------------------------------------------
    # Отображение заданной страницы интерфейса.
    # -----------------------------------------------
    # АРГУМЕНТЫ
    # --scr = имя класса страницы.
    # --data (opt) = опциональный объект данных.
    # -----------------------------------------------
    def show_frame(self, scr, data=""):
        frame = ""
        cont = scr

        # Экран вычислений создается только при вычисленных
        # на предыдущем экране данных.
        if cont == ResultScreenCLS:
            frame = cont(self.container, self, data[0], data[1])
            frame.create_graph()
            if FileImportScreenCLS in self.frames:
                self.frames[FileImportScreenCLS].hide_entries()
        else:
            frame = cont(self.container, self)

        self.frames[cont] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.clear()
        frame.tkraise()

    # GUI.iter_over_screens()
    # ----------------------------------------------
    # Итерация по всем доступным экранам приложения.
    # ----------------------------------------------
    def iter_over_screens(self):
        for frame in self.frames:
            print(frame)

    # Запуск интерфейса.
    # ------------------------------------------------
    # Запускает весь интерфейс в основном классе Main
    # ------------------------------------------------
    def run(self):
        self.mainloop()
