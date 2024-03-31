import math
import numpy as np
from sympy import *
from scipy.interpolate import interp1d


# Корневой класс, реализующий логику программы.
class Approximation:
    def __init__(self, x_arr, y_arr, pol_deg):
        self.x, self.y, self.a, self.b = symbols('x y a b')
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.pol_deg = pol_deg

    # Approximation.gaussian()
    # ------------------------------------------------------
    # Решает матричное умножение A * b = x по
    # методу Гаусса.
    # ------------------------------------------------------
    #  Принимает на вход две переменные:
    #  A - матрица коэффициентов - квадратный двумерный
    #  numpy array типа float
    #  b - вектор свободных членов - numpy array типа float
    #  Вовращает вектор решений
    # -------------------------------------------------------
    def gaussian(self, A, b):
        # составляем расширенную матрицу системы
        reshaped_b = b.reshape((len(b), 1))
        A = np.hstack((A, reshaped_b))

        # приводим матрицу к треугольному виду
        # i - опорная строка
        # j - текущая строка (всегда меньше i)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                A[j] -= A[i] * A[j][i] / A[i][i]

        # обратный ход
        x = np.array([0] * len(b), dtype=float)  # вектор решений

        i = len(A) - 1
        while i >= 0:
            x[i] = (A[i][-1] - sum(x * A[i][0:-1])) / A[i][i]
            i -= 1

        # вектор решений
        return x

    # Approximation.get_reg_coeffs()
    # ------------------------------------------------
    # Алгоритм реализации метода наименьших квадратов
    # для функции регрессии n-ой степени.
    # ------------------------------------------------
    # АРГУМЕНТЫ:
    # --x_arr = python list координат x.
    # --y_arr = python list координат y.
    # --precision = количество знаков после запятой
    # в итоговых коэффициентах.
    # ------------------------------------------------
    def get_reg_coeffs(self, x_arr, y_arr, n=1):
        # Проверка на корректность степени полинома.
        if n < 1:
            raise ValueError("Степень n полинома в функции get_reg_coeffs() обязана быть >= 1")

        # matrix = квадратная матрица коэффициентов размерности (n + 1) * (n + 1)
        # vect = вектор свободных коэффициентов размерности (n+1) * 1
        matrix = [[0 for j in range(n + 1)] for i in range(n + 1)]
        vect = [0 for j in range(n + 1)]

        # Заполняем матрицу коэффициентов.
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0 and j == 0:
                    matrix[i][j] = len(x_arr)
                matrix[i][j] = float(sum([x_arr[n] ** (i + j) for n in range(len(x_arr))]))

        # Заполняем вектор свободных членов.
        for j in range(len(vect)):
            vect[j] = sum([float(y_arr[i]) * (float(x_arr[i]) ** j) for i in range(len(x_arr))])

        # Решаем матричное уравнение методом Гаусса
        # и возвращаем итоговый вектор коэффициентов.
        return np.flip(self.gaussian(np.array(matrix), np.array(vect)))

    # Формирование настроек для построения аппроксимации.
    # ---------------------------------------------------------------------
    # 1. Функция get_reg_coeffs() вычисляет коэффициенты полинома степени n
    #    по заданным векторам x (x_arr) и y (y_arr), записывая в coeffs
    # 2. Вызов np.poly1d(coeffs) позволяет высчитать по заданным
    #    коэффициентам кривой значения f(xi) в записать в массив
    #    approx_y для каждого x.
    # 3. Возвращает массив коэфф-ов, округленных до знака coef_prec,
    #    вектор x и экспериментальный вектор f(xi) для дальнейшего
    #    построения графика.
    # --------------------------------------------------------------------
    # АРГУМЕНТЫ:
    # --x_arr = вектор x
    # --y_arr = вектор y
    # --deg = степень аппроксимирующего полинома.
    # --coef_prec = до скольки знаков после запятой округлять
    # коффициенты регрессии.
    # --------------------------------------------------------------------
    def approx(self, x_arr, y_arr, n, coef_prec=3):
        coeffs = self.get_reg_coeffs(x_arr, y_arr, n)
        func_from_coeffs = np.poly1d(coeffs)
        approx_y = np.array([func_from_coeffs(i) for i in np.nditer(x_arr)])
        rounded_coeffs = np.array([np.round(coef, coef_prec) for coef in np.nditer(coeffs)])

        return rounded_coeffs, approx_y

    # ResultScreen.form_vect_matrix()
    # -------------------------------------------
    # Формирует упорядоченный словарь координат
    # для построения графического представления
    # вычислений.
    # -------------------------------------------
    def form_vect_dict(self, x_arr, y_arr):
        def create_tuple(a, b):
            return a, b

        # Создаем словарь пар "x: y" и сортируем в порядке невозрастания.
        x_y_dict = dict(map(create_tuple, list(x_arr), list(y_arr)))
        x_y_dict = dict(sorted(x_y_dict.items()))

        # Разделяем словарь на вектора x и y.
        x_arr = np.array(list(x_y_dict.keys()))
        y_arr = np.array(list(x_y_dict.values()))

        return x_arr, y_arr

    # Approximation.form_approx_str()
    # -----------------------------------------------------------
    # Формирует строковое представление аппроксимирующей функции.
    # -----------------------------------------------------------
    # АРГУМЕНТЫ:
    # --coeff_obj = NumPy-массив коэффициентов кривой.
    # -----------------------------------------------------------
    def form_approx_str(self, coeffs_obj):
        coeffs = np.flip(coeffs_obj)
        approx_str = ""

        for i in range(len(coeffs)):
            c_sign = " + " if coeffs[i] > 0 else " - "

            if i == 0:
                if c_sign == " + ":
                    approx_str += f"{abs(coeffs[i])}"
                else:
                    approx_str += f"-{abs(coeffs[i])}"
            if i == 1:
                approx_str += f"{c_sign}{abs(coeffs[i])}x"
            if i > 1:
                approx_str += f"{c_sign}{abs(coeffs[i])}x^{i}"

        return approx_str

    # Approximation.calc_sum_of_sq(precision)
    # ----------------------------------------------------
    # Считает сумму квадратов разности теоретических
    # и практических значений функции для оценки
    # точности построения аппроксимирующей прямой.
    # Задача метода наименьших квадратов состоит в
    # поиске минимума данной характеристики.
    # ---------------------------------------------------
    # Аргументы:
    # --precision = количество знаков после запятой.
    # ---------------------------------------------------
    def calc_sum_of_sq(self, precision=3):
        coeffs, approx_y_arr = self.approx(self.x_arr, self.y_arr, self.pol_deg)
        return round(sum([(self.y_arr[i] - approx_y_arr[i]) ** 2 for i in range(len(self.y_arr))]), precision)

    # Approximation.calc_coef_of_corr(mean_prec, coef_prec)
    # --------------------------------------------------------------
    # Вычисляет коэффициент корреляции для линейной регрессии
    # и индекс корреляции для нелинейных полиномов по мат.формулам.
    # Характеристики корреляции характеризуют тесноту линейной
    # связи между абсциссой х и ординатой у.
    # --------------------------------------------------------------
    # АРГУМЕНТЫ:
    # --mean_prec = количество знаков после запятой
    # cредних арифметических векторов x и y.
    # --coef_prec = количество знаков после запятой
    # в итоговом коэффициенте.
    # --------------------------------------------------------------
    def calc_coef_of_corr(self, mean_prec=9, coef_prec=17):
        coeffs, approx_y_arr = self.approx(self.x_arr, self.y_arr, self.pol_deg)
        Mx = np.round(np.mean(self.x_arr), mean_prec)
        My = np.round(np.mean(self.y_arr), mean_prec)

        # Проверка на степени полинома.
        if self.pol_deg < 1:
            raise ValueError("Степень полинома должна быть >= 1!")

        if self.pol_deg < 2:
            # Расчет числителя.
            numerator = sum([(self.x_arr[i] - Mx) * (self.y_arr[i] - My) for i in range(len(self.x_arr))])

            # Расчет знаменателя.
            den_fp = sum([((x - Mx) ** 2) for x in self.x_arr])
            den_sp = sum([((y - My) ** 2) for y in self.y_arr])
            denominator = den_fp * den_sp

            return round(numerator / math.sqrt(denominator), coef_prec)
        else:
            numerator = sum([(self.y_arr[i] - approx_y_arr[i]) ** 2 for i in range(len(self.y_arr))])
            denominator = sum([(self.y_arr[i] - My) ** 2 for i in range(len(self.y_arr))])

            return round(math.sqrt(1 - (numerator / denominator)), coef_prec)

    # Approximation.pass_result_data()
    # ----------------------------------------------------
    # Возвращает словарь с характеристиками аппроксимации.
    # ----------------------------------------------------
    def pass_result_data(self):
        # Параметры для аппроксимации.
        x_arr, y_arr = self.form_vect_dict(self.x_arr, self.y_arr)
        coeffs, approx_y_arr = self.approx(x_arr, y_arr, n=self.pol_deg)

        return {
            "x_arr": x_arr,
            "y_arr": y_arr,
            "approx_y_arr": approx_y_arr,
            "pol_deg": self.pol_deg,
            "coeffs": coeffs,
            "pol_str": self.form_approx_str(coeffs),
            "min_sq_sum": self.calc_sum_of_sq(6),
            "corr_coef": self.calc_coef_of_corr(mean_prec=20, coef_prec=18)
        }
