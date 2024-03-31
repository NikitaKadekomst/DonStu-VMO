//	1. ������� ����� Array, �������������� ������� �������
// �������������� �������. �������������� ��������
// �������������� ���, ����� ��� ������ ������� �� ����������
// ������� �������������� ����������.
// 
//	2. ������� ����� ����� ����� IntegerRange � ������������
// ���������� (�� ��������� �� 0 �� 100). �������������
// ����������� ������� ��������� � ������������. �����������
// �������� ������������ � �������������� ��������.���
// ���������� ����� �� ���� �������� �������� ����� �� �������
// ���������, �������������, ��� ������ ������ �������������
// ����������.���������� ������ ���� ������������ ������� OutOfRangeException.
// 
//	3. ������� ����� ������������� ����� ����� PositiveInteger
// ��� ����� ��������� IntegerRange. ������� ������ ����������
// LeftBoundException � RightBoundException, ��������������,
// ��������������, ������� ������ �������� �� ����� � ������
// �������. ����������� ��������� ����� ����������.
// 
//	4. ����������� ��� �������� ������ PositiveInteger ��
//������������, � �������������.
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <clocale>
#include <string>
using namespace std;

// --------------- //
//    ������� 1
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
//    ������� 2
// --------------- //
class OutOfRangeException : public exception {
	const char* message;
public:
	OutOfRangeException(const char* msg) { message = msg; }
	const char* what() { return message; }
};

// ����� IntegerRange
// ������ �������� �������� �� left �� right.
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

		if (integer < leftLimit) throw OutOfRangeException("�������� ����� ����� < ����� �������� �������!");
		if (integer > rightLimit) throw OutOfRangeException("�������� ����� ����� > ������ �������� �������!");
	}

	// ������� ��� �����.
	int getInteger() { return integer; }
	int getLeftLimit() { return leftLimit; }
	int getRightLimit() { return rightLimit; }

	// ���������� ��������.
	IntegerRange operator+(IntegerRange const& other)
	{
		integer = integer + other.integer;

		if (integer < leftLimit) throw OutOfRangeException("��������� �������� \"+\" < ����� ������� ���������!");
		if (integer > rightLimit) throw OutOfRangeException("��������� �������� \"+\" > ������ ������� ���������!");

		return *this;
	}

	// ���������� ���������.
	IntegerRange operator-(IntegerRange const& other)
	{
		integer = integer - other.integer;

		if (integer < leftLimit) throw OutOfRangeException("��������� �������� \"-\" < ����� ������� ���������!");
		if (integer > rightLimit) throw OutOfRangeException("��������� �������� \"-\" > ������ ������� ���������!");
		
		return *this;
	}

	// ���������� ���������.
	IntegerRange operator*(IntegerRange const& other)
	{
		integer = integer * other.integer;

		if (integer < leftLimit) throw OutOfRangeException("��������� �������� \"*\" ��������� ���������� ����� ������� ���������!");
		if (integer > rightLimit) throw OutOfRangeException("��������� �������� \"*\" ��������� ���������� ������ ������� ���������!");

		return *this;
	}

	// ���������� �������.
	IntegerRange operator/(IntegerRange const& other)
	{
		integer = integer / other.integer;

		if (other.integer == 0) throw OutOfRangeException("������ ��������� ��� ������� �� ����� ��������� ����!");
		if (integer < leftLimit) throw OutOfRangeException("��������� �������� \"/\" < ����� ������� ���������!");
		if (integer > rightLimit) throw OutOfRangeException("��������� �������� \"/\" ��������� ���������� ������ ������� ���������!");

		return *this;
	}

	// ���������� ������������.
	void operator=(IntegerRange const& other) {
		integer = other.integer;
		leftLimit = other.leftLimit;
		rightLimit = other.rightLimit;

		if (integer < leftLimit) throw OutOfRangeException("��������� �������� \"=\" < ����� ������� ���������!");
		if (integer > rightLimit) throw OutOfRangeException("��������� �������� \"=\" ��������� ���������� ������ ������� ���������!");
	}

	// ����� ����������.
	void print() { cout << "������� ����� �����: " << integer << "\n"; }
};

// --------------- //
//    ������� 3
// --------------- //

// ����� ���������� LeftBoundException.
class LeftBoundException : public exception {
	const char* message;
public:
	LeftBoundException(const char* msg) { message = msg; }
	const char* what() { return message; }
};

// ����� ���������� RightBoundException.
class RightBoundException : public exception {
	const char* message;
public:
	RightBoundException(const char* msg) { message = msg; }
	const char* what() { return message; }
};

// ����� ������������� ����� PositiveInteger.
class PositiveInteger {
	IntegerRange* intRange;
public:
	PositiveInteger(IntegerRange* ir) {
		intRange = ir;

		if (intRange->leftLimit < 0) throw LeftBoundException("����� ������� ��������� <0!");
		if (intRange->rightLimit < 0) throw RightBoundException("������ ������� ��������� <0!");
		if (intRange->integer < 0) throw OutOfRangeException("����� ����� ���������� ������ <0!");
	}

	// ������� ��� �����.
	int getInteger() { return intRange->integer; }
	int getLeftLimit() { return intRange->leftLimit; }
	int getRightLimit() { return intRange->rightLimit; }

	// ���������� ��������.
	PositiveInteger operator+(PositiveInteger const& other)
	{
		intRange->integer = intRange->integer + other.intRange->integer;

		if (intRange->integer < 0) throw LeftBoundException("��������� �������� \"+\" <!");
		if (intRange->integer > intRange->rightLimit) throw RightBoundException("��������� �������� \"+\" ��������� ���������� ������ ������� ���������!");

		return *this;
	}

	// ���������� ���������.
	PositiveInteger operator-(PositiveInteger const& other)
	{
		intRange->integer = intRange->integer - other.intRange->integer;

		if (intRange->integer < 0) throw LeftBoundException("��������� �������� \"-\" <0!");
		if (intRange->integer > intRange->rightLimit) throw RightBoundException("��������� \"-\" �������� ��������� ������ ������� ���������!");

		return *this;
	}

	// ���������� ���������.
	PositiveInteger operator*(PositiveInteger const& other)
	{
		intRange->integer = intRange->integer * other.intRange->integer;

		if (intRange->integer < 0) throw LeftBoundException("��������� �������� \"*\" <0!");
		if (intRange->integer > intRange->rightLimit) throw RightBoundException("��������� �������� \"*\" ��������� ���������� ������ ������� ���������!");

		return *this;
	}

	// ���������� �������.
	PositiveInteger operator/(PositiveInteger const& other)
	{
		intRange->integer = intRange->integer / other.intRange->integer;

		if (other.intRange->integer == 0) throw OutOfRangeException("������ ��������� ��� ������� �� ����� ��������� ����!");
		if (intRange->integer < 0) throw LeftBoundException("��������� �������� \"/\" <0!");
		if (intRange->integer > intRange->rightLimit) throw RightBoundException("��������� �������� \"/\" ��������� ���������� ������ ������� ���������!");

		return *this;
	}

	// ���������� ������������.
	void operator=(PositiveInteger const& other) {
		intRange->integer = other.intRange->integer;
		intRange->leftLimit = other.intRange->leftLimit;
		intRange->rightLimit = other.intRange->rightLimit;

		if (intRange->integer < 0) throw LeftBoundException("��������� �������� \"=\" <0!");
		if (intRange->integer > intRange->rightLimit) throw OutOfRangeException("��������� �������� \"=\" ��������� ���������� ������ ������� ���������!");
	}
};

int main()
{
	setlocale(LC_ALL, "Russian");

	// ��������� ���� ����������.
	try {
		//
		// ������� 1.
		//
		Array arr1;
		arr1[9] = 10;
			 
		//
		// ������� 2.
		//
		IntegerRange ir(100, 5, 200);
		IntegerRange ir2(5, 5, 200);

		//
		// ������� 3.
		//
		PositiveInteger p1(&ir);
		PositiveInteger p2(&ir2);

		// ����� �� ������������/��������.
		cout << "����� ��������������� �����: " << p1.getInteger() << endl;
		cout << "������ �����: " << p1.getRightLimit() << endl;

		p1 = p1 / p2;

		cout << "------------------------------------" << endl;

		// ����� ����� ������������/��������.
		cout << "����� ��������������� �����: " << p1.getInteger() << endl;
		cout << "������ �����: " << p1.getRightLimit() << endl;
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

