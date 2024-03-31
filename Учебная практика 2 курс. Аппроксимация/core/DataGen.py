from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import numpy as np


# Класс для генерации тестовых табличных
# данных с записью в указанный файл.
class DataGen:
    def __init__(self):
        self.x = symbols("x")
        self._data = []
        self._func = None
        self._dots = None
        self._last_file = None

    # DataGen.create_data()
    # ---------------------------------------------------------
    # Генерация тестовых данных типа набор координат вида (x;y)
    # на основе параметров func, interval, dots, где:
    # --func = текстовая функция.
    # --interval = рассматриваемый интервал.
    # --dots = количество точек.
    # ---------------------------------------------------------
    def create_data(self, func, interval, dots):
        self._func = func
        self._dots = dots

        step = (interval[1] - interval[0]) / self._dots
        x_arr = np.arange(start=interval[0], stop=interval[1], step=step)
        lamb = lambdify(self.x, parse_expr(self._func))

        self._data = [[0, 0] for n in range(self._dots)]

        for i in range(len(self._data)):
            self._data[i][0] = round(float(x_arr[i]), 2)
            self._data[i][1] = round(lamb(float(x_arr[i])), 2)

        return self._data

    # DataGen.write_data_to_file()
    # --------------------------------------------------
    # Запись данных в файл, расположенного по пути file.
    # Данные имеют ввид:
    # Матрица 2 * N, где
    # --первый столбец = координаты x;
    # --второй столбец = координаты y.
    # --------------------------------------------------
    def write_data_to_file(self, file):
        self._last_file = file

        with open(file, "w") as file:
            file.write(f"Function: {self._func}\n")
            for i in range(len(self._data)):
                file.write(f"{self._data[i][0]} {self._data[i][1]}\n")

        print(f"Данные успешно записаны в файл {self._last_file}")

    # DataGen.get_data_from_file()
    # -----------------------------------------
    # Получение данных из существующего файла
    # по заданному пути filename
    # -----------------------------------------
    def get_data_from_file(self, filename):
        with open(filename, "r") as file:
            func = ""
            x_arr = []
            y_arr = []
            for line in file:
                if line == "":
                    continue
                if line.startswith("Function: "):
                    func = line.split(": ")[1]
                else:
                    parts = line.split(" ")
                    x_arr = np.append(x_arr, float(parts[0].strip()))
                    y_arr = np.append(y_arr, float(parts[1].strip()))
            return func, x_arr, y_arr
