#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <conio.h>
#include <map>
using namespace std;

class Person {
	string name;
	string lastname;
	string occupation;
	int age;
	int count = 0;

public:
	Person(string nm = "Nikita", string lm = "Zabashtin", string oc = "Programmer", int a = 20) {
		cout << "-----------------------------" << endl;
		cout << "Произошел вызов конструктора!" << endl;
		cout << "-----------------------------" << endl;

		age = a;
		name = nm;
		lastname = lm;
		occupation = oc;
	}
	Person(const Person& p) {
		cout << "-----------------------------------------" << endl;
		cout << "Произошел вызов конструктора копирования!" << endl;
		cout << "-----------------------------------------" << endl;

		count++;
		if (count >= 2)
		{
			exit(1);
		}

		age = p.age;
		name = p.name;
		lastname = p.lastname;
		occupation = p.occupation;
	}
	~Person() {
		cout << "-----------------------------" << endl;
		cout << "Произошел вызов деструктора!" << endl;
		cout << "-----------------------------" << endl;
	}

	// Геттеры для полей.

	int getAge() {
		return age;
	}

	string getName() {
		return name;
	}

	string getLastname() {
		return lastname;
	}

	string getOccupation() {
		return occupation;
	}

	// Сеттеры для полей

	void setAge(int newVal) {
		age = newVal;
	}

	void setName(string newVal) {
		name = newVal;
	}

	void setLastname(string newVal) {
		lastname = newVal;
	}

	void setOccupation(string newVal) {
		occupation = newVal;
	}
};

// ----------------
// Задание Дениса
// ---------------
class Student {
	int grade;
	string name;
public:
	Student(string nm, int gr) {
		name = nm;
		grade = gr;
	}

	int get_grade() {
		return grade;
	}

	string get_name() {
		return name;
	}
};

class Examinator {
	map<string, string>grades;
public: 
	Examinator() {}

	void check(Student obj[], int obj_length) {
		for (int i = 0; i < obj_length; i++) {
			int grade = obj[i].get_grade();

			if (grade == 5) {
				grades[obj[i].get_name()] = "Отличник";
			}

			if (grade == 4) {
				grades[obj[i].get_name()] = "Хорошист";
			}

			if (grade == 3) {
				grades[obj[i].get_name()] = "Троечник";
			}
		}
	}
	
	map<string, string> print_checks() {
		return grades;
	}
};
// ----------------
// Задание Дениса
// ---------------



int* ex3_create_array(int size) {
	int* arr = new int[size];

	for (int i = 0; i < size; i++)
		arr[i] = rand() % 300;

	return arr;
}

void ex3_fill_array(int* array, int size) {
	for (int i = 0; i < size; i++)
		array[i] = rand() % 300;
}

void ex3() {
	int count;
	cout << "Введите количество элементов: ";
	cin >> count;

	int* ten = ex3_create_array(count);
	int* empty_ten = new int[count];
	ex3_fill_array(empty_ten, count);


	for (int i = 0; i < count; i++) {
		cout << ten[i] << ' ';
	}

	cout << endl;
	for (int i = 0; i < count; i++) {
		cout << empty_ten[i] << ' ';
	}
}

void main(void) {
	setlocale(LC_ALL, "Russian");

	cout << "----------------------" << endl;
	cout << "Вход в функцию main()" << endl;
	cout << "----------------------" << endl;

	string choice;
	cout << "Какое задание хотите выполнить? (1) or (other)?";
	cin >> choice;

	if (choice == "other") {
		string d_or_c = "default";
		cout << "Введите режим работы: начальные значения (default) или кастомные (custom)?: ";
		cin >> d_or_c;

		if (d_or_c == "custom") {
			string name;
			cout << "Имя человека: ";
			cin >> name;

			string lastname;
			cout << "Фамилия человека: ";
			cin >> lastname;

			string occupation;
			cout << " человека: ";
			cin >> occupation;

			int age = 2003;

			Person person(name, lastname, occupation, age);
			cout << "Фамилия человека: " << person.getLastname() << endl;
			cout << "Имя человека: " << person.getName() << endl;
			cout << "Профессия человека: " << person.getOccupation() << endl;
			person.setOccupation("Baker");
			cout << "Группа человека: " << person.getOccupation() << endl;
		}
		else {
			Person person;
			cout << "Фамилия человека: " << person.getLastname() << endl;
			cout << "Имя человека: " << person.getName() << endl;
			cout << "Профессия человека: " << person.getOccupation() << endl;
			person.setOccupation("Baker");
			cout << "Группа человека: " << person.getOccupation() << endl;

			Person c_person(person);
			cout << "Скопированное значение профессии человека: " << c_person.getOccupation() << endl;

			Person c1_person(person);
		}
	}
	else if (choice == "1") {
		ex3();
		cout << endl;
	}

	// ----------------
	// Задание Дениса
	// ---------------
	Student stud1("Nikita", 3), stud2("Victor", 4), stud3("Anya", 3), stud4("Nastya", 4), stud5("Alexey", 5);
	Student obj[5] = { stud1, stud2, stud3, stud4, stud5 };
	Examinator ex1;

	ex1.check(obj, 5);
	for (auto const& x : ex1.print_checks())
	{
		std::cout << x.first  // string (key)
			<< ':'
			<< x.second // string's value 
			<< std::endl;
	}
	// ----------------
	// Задание Дениса
	// ---------------

	cout << "------------------------" << endl;
	cout << "Выход из функции main()" << endl;
	cout << "------------------------" << endl;
}