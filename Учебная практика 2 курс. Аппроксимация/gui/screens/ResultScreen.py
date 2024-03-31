from gui.screens.ProgramScreen import *
from gui.custom.ColoredButton import *

import tkinter
from tkinter import font
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


# Экран с результатами вычислений и графиком.
class ResultScreen(ProgramScreen):
    def __init__(self, parent, controller, data, graph_settings):
        ProgramScreen.__init__(self, parent, controller)
        self._func = []
        self._x_arr = []
        self._y_arr = []
        self._pol_deg = 1
        self.data = data
        self.graph_settings = graph_settings

        # "Стрелочка" возврата.
        self.canvas = Canvas(self, width=32, height=32, cursor="hand2")
        self.canvas.place(anchor=CENTER, relx=0.07, rely=0.07)
        self.backup_img = PhotoImage(file="images/backup-arrow.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.backup_img)
        self.canvas.bind("<Button-1>", self.back_to_settings)

        # Заголовок текущего режима работы с программой.
        self.mode_label = Label(self,
                                text="Результат вычислений",
                                font=("Arial Bold", 12))
        self.mode_label.place(relx=0.5, rely=0.14, anchor=CENTER)

        # Оформление шрифтов.
        polynom_deg_label_font = font.Font(family="Arial", weight="bold", size=11)
        approx_coeffs_label_font = font.Font(family="Arial", weight="bold", size=11)
        pol_str_label_font = font.Font(family="Arial", weight="bold", size=11)
        min_sq_label_font = font.Font(family="Arial", weight="bold", size=11)
        corr_coef_label_font = font.Font(family="Arial", weight="bold", size=11)

        # /* ------------------------------------ */ #
        #   ПУНКТ "СТЕПЕНЬ ПОЛИНОМА"
        # /* ------------------------------------ */ #
        self.polynom_deg_label = Label(self,
                                       text=f"Cтепень аппроксимирующего полинома",
                                       font=polynom_deg_label_font)
        self.polynom_deg_label.place(relx=0.2, rely=0.3, anchor=CENTER)
        self.polynom_deg_value = Label(self,
                                       text=self.data["pol_deg"],
                                       font=("Arial Bold", 10))
        self.polynom_deg_value.place(relx=0.2, rely=0.34, anchor=CENTER)

        # /* ------------------------------------ */ #
        #   ПУНКТ "КОЭФФИЦИЕНТЫ КРИВОЙ"
        # /* ------------------------------------ */ #
        self.approx_coeffs_label = Label(self,
                                         text="Коэффициенты аппрокс. кривой",
                                         font=approx_coeffs_label_font)
        self.approx_coeffs_label.place(relx=0.2, rely=0.41, anchor=CENTER)
        self.approx_coeffs_label_value = Label(self,
                                               text=self.data["coeffs"],
                                               font=("Arial Bold", 10))
        self.approx_coeffs_label_value.place(relx=0.2, rely=0.45, anchor=CENTER)

        # /* ------------------------------------ */ #
        #   ПУНКТ "ПОЛИНОМИАЛЬНАЯ ФУНКЦИЯ"
        # /* ------------------------------------ */ #
        self.pol_str_label = Label(self,
                                   text="Аппроксимирующий полином",
                                   font=pol_str_label_font)
        self.pol_str_label.place(relx=0.2, rely=0.52, anchor=CENTER)
        self.pol_str_label_value = Label(self,
                                         text=self.data["pol_str"],
                                         font=("Arial Bold", 10))
        self.pol_str_label_value.place(relx=0.2, rely=0.56, anchor=CENTER)

        # /* ----------------------------------------- */ #
        #   ПУНКТ "МИНИМУМ СУММЫ РАЗНОСТЕЙ КВАДРАТОВ"
        # /* ----------------------------------------- */ #
        self.min_sq_label = Label(self,
                                  text="Сумма квадратов разности",
                                  font=min_sq_label_font)
        self.min_sq_label.place(relx=0.2, rely=0.63, anchor=CENTER)
        self.min_sq_label_value = Label(self,
                                        text=self.data["min_sq_sum"],
                                        font=("Arial Bold", 10))
        self.min_sq_label_value.place(relx=0.2, rely=0.67, anchor=CENTER)

        # /* ------------------------------------ */ #
        #   ПУНКТ "КОЭФФИЦИЕНТ КОРРЕЛЯЦИИ"
        # /* ------------------------------------ */ #
        self.corr_coef_label = Label(self,
                                     text="Коэффициент (индекс) корреляции",
                                     font=corr_coef_label_font)
        self.corr_coef_label.place(relx=0.2, rely=0.74, anchor=CENTER)
        self.corr_coef_label_value = Label(self,
                                           text=self.data["corr_coef"],
                                           font=("Arial Bold", 10))
        self.corr_coef_label_value.place(relx=0.2, rely=0.78, anchor=CENTER)

        # /* ---------------------------------- */ #
        #       НАСТРОЙКИ ОТОБРАЖЕНИЯ
        # /* ---------------------------------- */ #

        # Если длина строк "Аппроксимирующий полином"
        # и "Коэффициенты аппрокс. кривой" > 40 символов,
        # то выставляем ограничение.
        symb = 50
        pol_str_value_text = self.pol_str_label_value.cget("text")
        approx_coeffs_label_text = self.approx_coeffs_label_value.cget("text")
        if len(pol_str_value_text) > symb:
            self.pol_str_label_value.config(text=f"{pol_str_value_text[0:symb]}...")
        if len(approx_coeffs_label_text) > symb:
            self.approx_coeffs_label_value.config(text=f"{approx_coeffs_label_text[0:symb]}...")

        # Конфигурация лейбла "Коэффициент (индекс) корреляции".
        if self.data["pol_deg"] < 2:
            self.corr_coef_label.config(text="Коэффициент корреляции")
        else:
            self.corr_coef_label.config(text="Индекс корреляции")

    # ResultScreen.back_to_settings()
    # ---------------------------------------------------------
    # Обработчик "стрелочки", возвращающей на экран настроек.
    # ---------------------------------------------------------
    def back_to_settings(self, *args):
        self.controller.back_to_settings()

    # ResultScreen.create_graph()
    # ---------------------------------------------------------
    # Построение общего графического представления всех данных
    # ---------------------------------------------------------
    def create_graph(self):
        # Необходимые данные.
        x_arr = np.array(self.data["x_arr"])
        y_arr = np.array(self.data["y_arr"])
        approx_y_arr = np.array(self.data["approx_y_arr"])
        pol_deg = self.data["pol_deg"]
        pol_str = self.data["pol_str"]

        # Инициализация фигуры.
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Заголовок графика.
        title = f"Линейная регрессия"
        if pol_deg >= 2:
            title = f"Полиномиальная регрессия ({pol_deg} степень)"

        # Создание сплайнов для обеих кривых (чтобы сделать их плавными).
        x_y_spline = make_interp_spline(x_arr, y_arr)
        x_approx_y_spline = make_interp_spline(x_arr, approx_y_arr)

        lin_x = np.linspace(x_arr.min(), x_arr.max(), 500)
        lin_y = x_y_spline(lin_x)
        lin_approx_y = x_approx_y_spline(lin_x)

        # Создание графика.
        ax.set_title(title)
        ax.scatter(x_arr, y_arr, color=self.graph_settings["base_dots_color"])
        ax.plot(lin_x, lin_y, color=self.graph_settings["base_curve_color"])
        ax.plot(lin_x, lin_approx_y, color=self.graph_settings["fitting_curve_color"],
                linewidth=self.graph_settings["fitting_curve_linewidth"], label=f"{pol_str}")
        ax.grid(linewidth=1.0)
        ax.legend(fontsize=9, loc="lower right")

        # Интервалы по x и y.
        if self.graph_settings["min_x_value"] and self.graph_settings["max_x_value"]:
            min_x_value = float(self.graph_settings["min_x_value"])
            max_x_value = float(self.graph_settings["max_x_value"])
            plt.xlim([min_x_value, max_x_value])

        if self.graph_settings["min_y_value"] and self.graph_settings["max_y_value"]:
            min_y_value = float(self.graph_settings["min_y_value"])
            max_y_value = float(self.graph_settings["max_y_value"])
            plt.ylim([min_y_value, max_y_value])

        # Расположение графика в интерфейсе Tkinter.
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.65, rely=0.55, anchor=CENTER)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().place(relx=0.65, rely=0.55, anchor=CENTER)

        # Отображение графика.
        plt.show()
