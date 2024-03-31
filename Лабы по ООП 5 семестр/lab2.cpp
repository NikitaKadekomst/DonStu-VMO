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
		cout << "��������� ����� ������������!" << endl;
		cout << "-----------------------------" << endl;

		age = a;
		name = nm;
		lastname = lm;
		occupation = oc;
	}
	Person(const Person& p) {
		cout << "-----------------------------------------" << endl;
		cout << "��������� ����� ������������ �����������!" << endl;
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
		cout << "��������� ����� �����������!" << endl;
		cout << "-----------------------------" << endl;
	}

	// ������� ��� �����.

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

	// ������� ��� �����

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
// ������� ������
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
				grades[obj[i].get_name()] = "��������";
			}

			if (grade == 4) {
				grades[obj[i].get_name()] = "��������";
			}

			if (grade == 3) {
				grades[obj[i].get_name()] = "��������";
			}
		}
	}
	
	map<string, string> print_checks() {
		return grades;
	}
};
// ----------------
// ������� ������
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
	cout << "������� ���������� ���������: ";
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
	cout << "���� � ������� main()" << endl;
	cout << "----------------------" << endl;

	string choice;
	cout << "����� ������� ������ ���������? (1) or (other)?";
	cin >> choice;

	if (choice == "other") {
		string d_or_c = "default";
		cout << "������� ����� ������: ��������� �������� (default) ��� ��������� (custom)?: ";
		cin >> d_or_c;

		if (d_or_c == "custom") {
			string name;
			cout << "��� ��������: ";
			cin >> name;

			string lastname;
			cout << "������� ��������: ";
			cin >> lastname;

			string occupation;
			cout << " ��������: ";
			cin >> occupation;

			int age = 2003;

			Person person(name, lastname, occupation, age);
			cout << "������� ��������: " << person.getLastname() << endl;
			cout << "��� ��������: " << person.getName() << endl;
			cout << "��������� ��������: " << person.getOccupation() << endl;
			person.setOccupation("Baker");
			cout << "������ ��������: " << person.getOccupation() << endl;
		}
		else {
			Person person;
			cout << "������� ��������: " << person.getLastname() << endl;
			cout << "��� ��������: " << person.getName() << endl;
			cout << "��������� ��������: " << person.getOccupation() << endl;
			person.setOccupation("Baker");
			cout << "������ ��������: " << person.getOccupation() << endl;

			Person c_person(person);
			cout << "������������� �������� ��������� ��������: " << c_person.getOccupation() << endl;

			Person c1_person(person);
		}
	}
	else if (choice == "1") {
		ex3();
		cout << endl;
	}

	// ----------------
	// ������� ������
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
	// ������� ������
	// ---------------

	cout << "------------------------" << endl;
	cout << "����� �� ������� main()" << endl;
	cout << "------------------------" << endl;
}