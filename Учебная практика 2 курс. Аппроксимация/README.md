# Учебная практика за 2 курс.
Тема: Программная реализация линейной и полиномиальной регрессий.  

## Аппроксимация полиномом n-ой степени. Теория.  
В математике, эконометрике, физике и других сферах науки зачастую возникает необходимость решения задачи аппроксимации - нахождения приближенного закона (функции), описывающего зависимость между параметрами на основе некоторого представленного набора экспериментальных данных. Например, в результате проведения лабораторного эксперимента получен набор данных, связывающий количество колебаний маятника с приложенной изначальной силой натяжения, и затем требуется описать приближенную зависимость между этими величинами. 

Одним из наиболее эффективных методов решения задачи аппроксимации является метод наименьших квадратов. Метод наименьших квадратов (МНК) — математический метод, основанный на минимизации суммы квадратов отклонений некоторых функций от экспериментальных входных данных. Он является одним из базовых методов регрессионного анализа для оценки неизвестных параметров регрессионных моделей по выборочным данным.  

Будучи примененным к задаче аппроксимации, МНК позволяет вычислить коэффициенты регрессии – некоторой теоретической функции (полинома), по которой в дальнейшем строится регрессионная модель, отражающая наиболее приближенную функциональную зависимость между величинами, что является возможным, благодаря различным оценкам, применённым к построенной модели, в частности, минимуму суммы квадратов разности и коэффициенту (индексу) корреляции.  

## Инструкция по работе с программой.  
Для работы с программой требуется запустить файл Main.py, содержащий класс входной точки.
После запуска требуется импортировать файл с желаемым тестом из папки /tests.  
В программе используются библиотеки и модули Python:
1) matplotlib (графики)
2) numpy (работа с матрицами)
3) scipy (интерполяция для более плавных кривых)
4) sympy (редкие математические выражения)
5) math (арифметические операции)
6) tkinter (интерфейс)

