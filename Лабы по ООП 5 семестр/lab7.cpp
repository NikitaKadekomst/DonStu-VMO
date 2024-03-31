//	1. Создать класс Array, представляющий понятие массива
// фиксированного размера. Переопределить операцию
// индексирования так, чтобы при выходе индекса за допустимые
// границы генерировалось исключение.
// 
//	2. Создать класс целых чисел IntegerRange с ограниченным
// диапазоном (по умолчанию от 0 до 100). Предусмотреть
// возможность задания интервала в конструкторе. Перегрузить
// операцию присваивания и арифметические операции.При
// выполнении любой из этих операций возможен выход за границы
// интервала, следовательно, при выходе должно выбрасываться
// исключение.Исключение должно быть представлено классом OutOfRangeException.
// 
//	3. Создать класс положительных целых чисел PositiveInteger
// как класс наследник IntegerRange. Создать классы исключений
// LeftBoundException и RightBoundException, представляющие,
// соответственно, события выхода значения за левую и правую
// границы. Организуйте каскадный вызов исключений.
// 
//	4. Используйте при создании класса PositiveInteger не
//наследование, а агрегирование.
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <clocale>
#include <string>
using namespace std;

// --------------- //
//    ЗАДАНИЕ 1
// --------------- //
class IndexOutOfBounds : public exception {
public:
	IndexOutOfBounds() {}
	const char* what() { return "IndexOutOfBounds: Index is out of bounds!"; }
};

const int SIZE = 10;

class Array {
private:
	int arr[SIZE];
public:
	Array() { register int i; }

	int& operator[](int i) {
		if (i > SIZE) {
			throw IndexOutOfBounds();
			return arr[0];
		}

		return arr[i];
	}
};

// --------------- //
//    ЗАДАНИЕ 2
// --------------- //
class OutOfRangeException : public exception {
	const char* message;
public:
	OutOfRangeException(const char* msg) { message = msg; }
	const char* what() { return message; }
};

// Класс IntegerRange
// Задает числовой интервал от left до right.
class IntegerRange {
public:
	int integer;
	int leftLimit;
	int rightLimit;

	IntegerRange(int intgr = 0, int left = 0, int right = 100)
	{
		integer = intgr;
		leftLimit = left;
		rightLimit = right;

		if (integer < leftLimit) throw OutOfRangeException("Заданное целое число < левой заданной границы!");
		if (integer > rightLimit) throw OutOfRangeException("Заданное целое число > правой заданной границы!");
	}

	// Геттеры для полей.
	int getInteger() { return integer; }
	int getLeftLimit() { return leftLimit; }
	int getRightLimit() { return rightLimit; }

	// Перегрузка сложения.
	IntegerRange operator+(IntegerRange const& other)
	{
		integer = integer + other.integer;

		if (integer < leftLimit) throw OutOfRangeException("Результат операции \"+\" < левой границы интервала!");
		if (integer > rightLimit) throw OutOfRangeException("Результат операции \"+\" > правой границы интервала!");

		return *this;
	}

	// Перегрузка вычитания.
	IntegerRange operator-(IntegerRange const& other)
	{
		integer = integer - other.integer;

		if (integer < leftLimit) throw OutOfRangeException("Результат операции \"-\" < левой границы интервала!");
		if (integer > rightLimit) throw OutOfRangeException("Результат операции \"-\" > правой границы интервала!");
		
		return *this;
	}

	// Перегрузка умножения.
	IntegerRange operator*(IntegerRange const& other)
	{
		integer = integer * other.integer;

		if (integer < leftLimit) throw OutOfRangeException("Результат операции \"*\" превышает допустимую ЛЕВУЮ границу интервала!");
		if (integer > rightLimit) throw OutOfRangeException("Результат операции \"*\" превышает допустимую ПРАВУЮ границу интервала!");

		return *this;
	}

	// Перегрузка деления.
	IntegerRange operator/(IntegerRange const& other)
	{
		integer = integer / other.integer;

		if (other.integer == 0) throw OutOfRangeException("Второе слагаемое при делении не может равняться нулю!");
		if (integer < leftLimit) throw OutOfRangeException("Результат операции \"/\" < левой границы интервала!");
		if (integer > rightLimit) throw OutOfRangeException("Результат операции \"/\" превышает допустимую ПРАВУЮ границу интервала!");

		return *this;
	}

	// Перегрузка присваивания.
	void operator=(IntegerRange const& other) {
		integer = other.integer;
		leftLimit = other.leftLimit;
		rightLimit = other.rightLimit;

		if (integer < leftLimit) throw OutOfRangeException("Результат операции \"=\" < левой границы интервала!");
		if (integer > rightLimit) throw OutOfRangeException("Результат операции \"=\" превышает допустимую ПРАВУЮ границу интервала!");
	}

	// Вывод результата.
	void print() { cout << "Текущее целое число: " << integer << "\n"; }
};

// --------------- //
//    ЗАДАНИЕ 3
// --------------- //

// Класс исключения LeftBoundException.
class LeftBoundException : public exception {
	const char* message;
public:
	LeftBoundException(const char* msg) { message = msg; }
	const char* what() { return message; }
};

// Класс исключения RightBoundException.
class RightBoundException : public exception {
	const char* message;
public:
	RightBoundException(const char* msg) { message = msg; }
	const char* what() { return message; }
};

// Класс положительных чисел PositiveInteger.
class PositiveInteger {
	IntegerRange* intRange;
public:
	PositiveInteger(IntegerRange* ir) {
		intRange = ir;

		if (intRange->leftLimit < 0) throw LeftBoundException("Левая граница интервала <0!");
		if (intRange->rightLimit < 0) throw RightBoundException("Правая граница интервала <0!");
		if (intRange->integer < 0) throw OutOfRangeException("Целое число экземпляра класса <0!");
	}

	// Геттеры для полей.
	int getInteger() { return intRange->integer; }
	int getLeftLimit() { return intRange->leftLimit; }
	int getRightLimit() { return intRange->rightLimit; }

	// Перегрузка сложения.
	PositiveInteger operator+(PositiveInteger const& other)
	{
		intRange->integer = intRange->integer + other.intRange->integer;

		if (intRange->integer < 0) throw LeftBoundException("Результат операции \"+\" <!");
		if (intRange->integer > intRange->rightLimit) throw RightBoundException("Результат операции \"+\" превышает допустимую ПРАВУЮ границу интервала!");

		return *this;
	}

	// Перегрузка вычитания.
	PositiveInteger operator-(PositiveInteger const& other)
	{
		intRange->integer = intRange->integer - other.intRange->integer;

		if (intRange->integer < 0) throw LeftBoundException("Результат операции \"-\" <0!");
		if (intRange->integer > intRange->rightLimit) throw RightBoundException("Результат \"-\" операции превышает правую границу интервала!");

		return *this;
	}

	// Перегрузка умножения.
	PositiveInteger operator*(PositiveInteger const& other)
	{
		intRange->integer = intRange->integer * other.intRange->integer;

		if (intRange->integer < 0) throw LeftBoundException("Результат операции \"*\" <0!");
		if (intRange->integer > intRange->rightLimit) throw RightBoundException("Результат операции \"*\" превышает допустимую правую границу интервала!");

		return *this;
	}

	// Перегрузка деления.
	PositiveInteger operator/(PositiveInteger const& other)
	{
		intRange->integer = intRange->integer / other.intRange->integer;

		if (other.intRange->integer == 0) throw OutOfRangeException("Второе слагаемое при делении не может равняться нулю!");
		if (intRange->integer < 0) throw LeftBoundException("Результат операции \"/\" <0!");
		if (intRange->integer > intRange->rightLimit) throw RightBoundException("Результат операции \"/\" превышает допустимую правую границу интервала!");

		return *this;
	}

	// Перегрузка присваивания.
	void operator=(PositiveInteger const& other) {
		intRange->integer = other.intRange->integer;
		intRange->leftLimit = other.intRange->leftLimit;
		intRange->rightLimit = other.intRange->rightLimit;

		if (intRange->integer < 0) throw LeftBoundException("Результат операции \"=\" <0!");
		if (intRange->integer > intRange->rightLimit) throw OutOfRangeException("Результат операции \"=\" превышает допустимую правую границу интервала!");
	}
};

int main()
{
	setlocale(LC_ALL, "Russian");

	// Обработки всех исключений.
	try {
		//
		// ЗАДАНИЕ 1.
		//
		Array arr1;
		arr1[9] = 10;
			 
		//
		// ЗАДАНИЕ 2.
		//
		IntegerRange ir(100, 5, 200);
		IntegerRange ir2(5, 5, 200);

		//
		// ЗАДАНИЕ 3.
		//
		PositiveInteger p1(&ir);
		PositiveInteger p2(&ir2);

		// Вывод до присваивания/операций.
		cout << "Целое неотрицательное число: " << p1.getInteger() << endl;
		cout << "Правый лимит: " << p1.getRightLimit() << endl;

		p1 = p1 / p2;

		cout << "------------------------------------" << endl;

		// Вывод после присваивания/операций.
		cout << "Целое неотрицательное число: " << p1.getInteger() << endl;
		cout << "Правый лимит: " << p1.getRightLimit() << endl;
	}
	catch (IndexOutOfBounds ex) {
		cout << ex.what() << endl;
	}
	catch (LeftBoundException ex) {
		cout << "LeftBoundException: " << ex.what() << endl;
	}
	catch (RightBoundException ex) {
		cout << "RightBoundException: " << ex.what() << endl;
	}
	catch (OutOfRangeException ex) {
		cout << "OutOfRangeException: " << ex.what() << endl;
	}
	catch (exception ex) {
		cout << "Some unhandled exception: " << ex.what() << endl;
	}
}

