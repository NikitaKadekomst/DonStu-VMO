from core.Approximation import *
from core.DataGen import *

from gui.screens.ResultScreen import ResultScreen as ResultScreenCLS
from gui.screens.ProgramScreen import *
from gui.custom.ColoredButton import *

from tkinter import ttk
from tkinter import filedialog as fd


# Класс интерфейса настроек аппроксимации.
class FileImportScreen(ProgramScreen):
    def __init__(self, parent, controller):
        ProgramScreen.__init__(self, parent, controller)
        self._func = []
        self._x_arr = []
        self._y_arr = []
        self._pol_deg = 1
        self._entries_data = ""
        self._current_file = ""

        # Заголовок текущего режима работы с программой.
        self.mode_label = Label(self,
                                text="Окно настроек программы",
                                font=("Arial Bold", 12))
        self.mode_label.place(relx=0.5, rely=0.14, anchor=CENTER)

        # /* ------------------------------------ */ #
        #   БЛОК "ВВОД ДАННЫХ".
        # /* ------------------------------------ */ #
        self.data_block_label = Label(self,
                                      text="Ввод данных",
                                      font=("Arial Bold", 12))
        self.data_block_label.place(relx=0.2, rely=0.25, anchor=CENTER)

        self.file_import_button_label = Label(self,
                                              text="Импорт набора данных \nв программу",
                                              font=("Arial Bold", 10))
        self.file_import_button_label.place(relx=0.2, rely=0.35, anchor=CENTER)
        self.file_import_button = ColoredButton(self,
                                                width=20,
                                                text="Импорт файла",
                                                command=self.process_file)
        self.file_import_button.place(relx=0.2, rely=0.43, anchor=CENTER)
        self.current_file_label = Label(self,
                                        text="",
                                        font=("Arial Bold", 10))
        self.current_file_label.place(relx=0.2, rely=0.49, anchor=CENTER)

        # Блок "Ввод степени полинома"
        self.polynom_pow_entry_label = Label(self,
                                             text="Введите степень n полинома\nдля аппроксимации: ",
                                             font=("Arial Bold", 10))
        self.polynom_pow_entry_label.place(relx=0.2, rely=0.57, anchor=CENTER)
        self.polynom_deg_entry = Entry()
        self.polynom_deg_entry.place(relx=0.2, rely=0.64, anchor=CENTER)

        # /* ------------------------------------ */ #
        #   БЛОК "НАСТРОЙКИ ГРАФИКА. КООРДИНАТЫ".
        # /* ------------------------------------ */ #
        self.graph_settings_label = Label(self,
                                          text="Настройки графика",
                                          font=("Arial Bold", 12))
        self.graph_settings_label.place(relx=0.68, rely=0.25, anchor=CENTER)

        # Минимальное значение по оси x.
        self.min_x_value_label = Label(self,
                                       text="Минимальное значение по оси x.",
                                       font=("Arial Bold", 10))
        self.min_x_value_label.place(relx=0.55, rely=0.32, anchor=CENTER)
        self.min_x_value_entry = Entry()
        self.min_x_value_entry.place(relx=0.55, rely=0.37, anchor=CENTER)

        # Максимальное значение по оси x.
        self.max_x_value_label = Label(self,
                                       text="Максимальное значение по оси x.",
                                       font=("Arial Bold", 10))
        self.max_x_value_label.place(relx=0.55, rely=0.44, anchor=CENTER)
        self.max_x_value_entry = Entry()
        self.max_x_value_entry.place(relx=0.55, rely=0.49, anchor=CENTER)

        # Минимальное значение по оси y.
        self.min_y_value_label = Label(self,
                                       text="Минимальное значение по оси y.",
                                       font=("Arial Bold", 10))
        self.min_y_value_label.place(relx=0.55, rely=0.56, anchor=CENTER)
        self.min_y_value_entry = Entry()
        self.min_y_value_entry.place(relx=0.55, rely=0.61, anchor=CENTER)

        # Максимальное значение по оси y.
        self.max_y_value_label = Label(self,
                                       text="Максимальное значение по оси y.",
                                       font=("Arial Bold", 10))
        self.max_y_value_label.place(relx=0.55, rely=0.68, anchor=CENTER)
        self.max_y_value_entry = Entry()
        self.max_y_value_entry.place(relx=0.55, rely=0.73, anchor=CENTER)

        # /* --------------------------------------- */ #
        #   БЛОК "НАСТРОЙКИ ГРАФИКА. ЦВЕТА ГРАФИКА".
        # /* --------------------------------------- */ #

        # Цвет базовых точек.
        self.base_dots_color_label = Label(self,
                                           text="Цвет базовых точек",
                                           font=("Arial Bold", 10))
        self.base_dots_color_label.place(relx=0.8, rely=0.32, anchor=CENTER)
        self.base_dots_color_entry = Entry()
        self.base_dots_color_entry.place(relx=0.8, rely=0.37, anchor=CENTER)

        # Цвет кривой, проходящей через точки.
        self.base_curve_color_label = Label(self,
                                            text="Цвет кривой, проходящей \nчерез точки",
                                            font=("Arial Bold", 10))
        self.base_curve_color_label.place(relx=0.8, rely=0.44, anchor=CENTER)
        self.base_curve_color_entry = Entry()
        self.base_curve_color_entry.place(relx=0.8, rely=0.49, anchor=CENTER)

        # Цвет прибл. кривой.
        self.fitting_curve_color_label = Label(self,
                                               text="Цвет прибл. кривой",
                                               font=("Arial Bold", 10))
        self.fitting_curve_color_label.place(relx=0.8, rely=0.56, anchor=CENTER)
        self.fitting_curve_color_entry = Entry()
        self.fitting_curve_color_entry.place(relx=0.8, rely=0.61, anchor=CENTER)

        # Толщина прибл. кривой.
        self.fitting_curve_linewidth_label = Label(self,
                                                   text="Толщина прибл. кривой",
                                                   font=("Arial Bold", 10))
        self.fitting_curve_linewidth_label.place(relx=0.8, rely=0.68, anchor=CENTER)
        self.fitting_curve_linewidth_entry = Entry()
        self.fitting_curve_linewidth_entry.place(relx=0.8, rely=0.73, anchor=CENTER)

        # /* ----------------------------- */ #
        #   БЛОК "УПРАВЛЕНИЕ ДАННЫМИ".
        # /* ----------------------------- */ #
        self.show_graph_button = ColoredButton(self,
                                               width=20,
                                               text="Вычислить коэфф-ы \nи построить график",
                                               command=self.run)
        self.show_graph_button.place(relx=0.35, rely=0.87, anchor=CENTER)
        self.show_graph_button = ColoredButton(self,
                                               width=20,
                                               text="Очистить \nсодержимое",
                                               command=self.clear)
        self.show_graph_button.place(relx=0.6, rely=0.87, anchor=CENTER)

    # FileImportScreen.process_file()
    # -----------------------------------------------
    # Обработчик по нажатию на кнопку "Импорт файла"
    # -----------------------------------------------
    def process_file(self, *args):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        path = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        # Фиксирует текущий файл в строке "Файл: ..."
        filename = path.split("/")[-1]
        self.current_file_label.config(text=f"Файл: {filename}")

        # Разложение файла на составляющие.
        datagen = DataGen()
        self._func, self._x_arr, self._y_arr = datagen.get_data_from_file(path)

    # FileImportScreen.process_entries_data()
    # ------------------------------------------
    # Метод для обработки исходных полей.
    # ------------------------------------------
    def process_entries_data(self):
        pol_deg = self.polynom_deg_entry.get() if self.polynom_deg_entry.get().isnumeric() else ""
        min_x_value = self.min_x_value_entry.get() if self.min_x_value_entry.get().isnumeric() else ""
        max_x_value = self.max_x_value_entry.get() if self.min_x_value_entry.get().isnumeric() else ""
        min_y_value = self.min_y_value_entry.get() if self.polynom_deg_entry.get().isnumeric() else ""
        max_y_value = self.min_y_value_entry.get() if self.polynom_deg_entry.get().isnumeric() else ""
        base_dots_color = self.base_dots_color_entry.get() if self.polynom_deg_entry.get().isalpha() else ""
        base_curve_color = self.base_curve_color_entry.get() if self.polynom_deg_entry.get().isalpha() else ""
        fitting_curve_color = self.fitting_curve_color_entry.get() if self.polynom_deg_entry.get().isalpha() else ""
        fitting_curve_linewidth = self.fitting_curve_linewidth_entry.get() if self.polynom_deg_entry.get().isnumeric() else ""

        return {
            "pol_deg": pol_deg or 1,
            "min_x_value": min_x_value or None,
            "max_x_value": max_x_value or None,
            "min_y_value": min_y_value or None,
            "max_y_value": max_y_value or None,
            "base_dots_color": base_dots_color or "red",
            "base_curve_color": base_curve_color or "pink",
            "fitting_curve_color": fitting_curve_color or "blue",
            "fitting_curve_linewidth": fitting_curve_linewidth or 1
        }

    # FileImportScreen.run()
    # ------------------------------------------
    # Базовый метод, запускающий логику экрана
    # при запуске экрана. Точка входа в класс.
    # ------------------------------------------
    def run(self, *args):
        self._entries_data = self.process_entries_data()
        approx = Approximation(self._x_arr, self._y_arr, int(self._entries_data["pol_deg"]))
        self.controller.show_frame(ResultScreenCLS, [approx.pass_result_data(), self.process_entries_data()])

    # FileImportScreen.show_entries()
    # -------------------------------------------
    # Плэйсинг всех полей.
    # Отображает поля при переключении экранов.
    # -------------------------------------------
    def show_entries(self):
        self.polynom_deg_entry.place(relx=0.2, rely=0.64, anchor=CENTER)
        self.min_x_value_entry.place(relx=0.55, rely=0.37, anchor=CENTER)
        self.max_x_value_entry.place(relx=0.55, rely=0.49, anchor=CENTER)
        self.min_y_value_entry.place(relx=0.55, rely=0.61, anchor=CENTER)
        self.max_y_value_entry.place(relx=0.55, rely=0.73, anchor=CENTER)
        self.base_dots_color_entry.place(relx=0.8, rely=0.37, anchor=CENTER)
        self.base_curve_color_entry.place(relx=0.8, rely=0.49, anchor=CENTER)
        self.fitting_curve_color_entry.place(relx=0.8, rely=0.61, anchor=CENTER)
        self.fitting_curve_linewidth_entry.place(relx=0.8, rely=0.73, anchor=CENTER)

    # FileImportScreen.hide_entries()
    # -------------------------------------------
    # Плэйсинг всех полей.
    # Скрывает поля при переключении экранов.
    # -------------------------------------------
    def hide_entries(self):
        self.polynom_deg_entry.place_forget()
        self.min_x_value_entry.place_forget()
        self.max_x_value_entry.place_forget()
        self.min_y_value_entry.place_forget()
        self.max_y_value_entry.place_forget()
        self.base_dots_color_entry.place_forget()
        self.base_curve_color_entry.place_forget()
        self.fitting_curve_color_entry.place_forget()
        self.fitting_curve_linewidth_entry.place_forget()

    # FileImportScreen.сlear()
    # -------------------------------------------
    # Полная очистка всех полей настроек.
    # -------------------------------------------
    def clear(self, *args):
        self.polynom_deg_entry.delete(0, END)
        self.min_x_value_entry.delete(0, END)
        self.max_x_value_entry.delete(0, END)
        self.min_y_value_entry.delete(0, END)
        self.max_y_value_entry.delete(0, END)
        self.base_dots_color_entry.delete(0, END)
        self.base_curve_color_entry.delete(0, END)
        self.fitting_curve_color_entry.delete(0, END)
        self.fitting_curve_linewidth_entry.delete(0, END)
