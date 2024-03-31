using namespace std;
#include <iostream>
#include <cstring>
#include <clocale>

//1. ������� ��������� "�������" ���������� ��������� ����: 
//- ��� �������� 
//- �������� �������� 
//- ������� �������� 
//- ��� �������� 
//- ������. 
//
//2. ���������� ����������� ��� ������������� ����� ��������� 
//�� ���������� �� ���������.���������� ����������� ����������� 
//� ����������.�������� �������� ������.
//
//3. �������� � �������� ��������� �������� ����� struct �� class.
//��������� ���������.����� �������� �������� ? 
//������ ? ��� �� ��������� ? 
//
//4. �������� ������������ ������� ������� � ����� 
//������(�������� / ������ �������� ����). 
//
//5. ������ � ������������ � ���������� ������ ��������� 
//�� ����� � ���, ����� ������� ���� �������.
//�������������� ������� main ��������� ������� : 
//void main(void) { cout << "���� � ������� main()" << endl; 
// ... <����_main()> ... cout << "����� �� ������� main()" << endl; } 
//�������� ����� ������� ������������� � ������������. 
//
//6. ������� ���������� ������� Student test(Student s) { return s; } 
//������� �� � �������� ���������.��� ��������� � ������ ? 
//
//7. �������� �������� ��������� � - � test �� �������� �� ������.
//��� ���������� ? 
//
//8. �������� ������� ���������� � - � test �� �������� �� ������.
//��� ���������� ?

class Student {
	string name;
	string surname;
	string lastname;
	int birth;
	string group;
	int count = 0;
	
public:
	Student(string nm = "Nikita", string sm = "Zabashtin", string lm = "Victorovich", int b = 2003, string gr = "VMO31") {
		cout << "-----------------------------" << endl;
		cout << "��������� ����� ������������!" << endl;
		cout << "-----------------------------" << endl;

		birth = b;
		name = nm;
		surname = sm;
		lastname = lm;
		group = gr;
	}
	Student(const Student &p) {
		cout << "-----------------------------------------" << endl;
		cout << "��������� ����� ������������ �����������!" << endl;
		cout << "-----------------------------------------" << endl;

		count++;
		if (count >= 2) 
		{ exit(1); }


		birth = p.birth;
		name = p.name;
		surname = p.surname;
		lastname = p.lastname;
		group = p.group;
	}
	~Student() {
		cout << "-----------------------------" << endl;
		cout << "��������� ����� �����������!" << endl;
		cout << "-----------------------------" << endl;
	}
	
	// ������� ��� �����.

	int getBirthYear() {
		return birth;
	}

	string getName() {
		return name;
	}

	string getSurname() {
		return surname;
	}

	string getLastname() {
		return lastname;
	}

	string getGroupName() {
		return group;
	}

	// ������� ��� �����

	void setBirth(int newVal) {
		birth = newVal;
	}

	void setName(string newVal) {
		name = newVal;
	}

	void setSurname(string newVal) {
		surname = newVal;
	}

	void setLastname(string newVal) {
		lastname = newVal;
	}

	void setGroup(string newVal) {
		group = newVal;
	}
};

void main(void) { 
	setlocale(LC_ALL, "Russian");

	cout << "----------------------" << endl;
	cout << "���� � ������� main()" << endl; 
	cout << "----------------------" << endl;

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

		string surname;
		cout << "�������� ��������: ";
		cin >> surname;

		int birth = 2003;

		string group;
		cout << "������ ��������: ";
		cin >> group;

		Student student(name, surname, lastname, birth, group);
		cout << "������� ��������: " << student.getLastname() << endl;
		cout << "�������� ��������: " << student.getSurname() << endl;
		cout << "��� ��������: " << student.getName() << endl;
		cout << "������ ��������: " << student.getGroupName() << endl;
		student.setGroup("VMO31");
		cout << "������ ��������: " << student.getGroupName() << endl;
	}
	else {
		Student stud;
		cout << "������� ��������: " << stud.getLastname() << endl;
		cout << "������ ��������: " << stud.getGroupName() << endl;
		cout << "��������� �������� ��������: " << stud.getSurname() << endl;
		stud.setSurname("Alexandrovich");
		cout << "����� �������� ��������: " << stud.getSurname() << endl;

		Student c_stud(stud);
		cout << "������������� �������� ��������: " << c_stud.getSurname() << endl;

		Student d_stud(stud);
	}

	cout << "------------------------" << endl;
	cout << "����� �� ������� main()" << endl;
	cout << "------------------------" << endl;
}