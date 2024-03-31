//	1. ������� ����� Test c ����������� �������� ����� W �
// �������� Z, ������� ������� ��������� "��� �������� �������
// ������ Test". �������� ����������� ��� ������������� ��������
// ������ Test � ����� ����������, ����������� �� ���������
// �������� 1. �������� ������ ������ ������� fun, ������� ��
// ���������� �������� � �������� ��������� �� ������ ���� Test.
//	2. ������� �� ������� ������ ������� fun, �������
// ������� �� ����� �������� ��������� W � �������� �� ������
// Test ������� Z.
//	3. � ������� main ������� ���������� ������ Test(���
//  ����� �������������) � ��������� � ��� ������� fun.
//	4. ������� ����� � ������������� ��������� ������������.
//	5. ��������� � ����������� ��������� - ������
// ������������� ���� ������� A � B, � ������� A ���� B.

#include <iostream>
#include <clocale>
#include <string>
#include <map>
using namespace std;

// --------------
//  ������� 1-3
// --------------
class Test {
protected:
	int W = 100;
private:
	int param;
	void Z() {
		cout << "��� �������� ������� ������ Test" << endl;
	}
public:
	Test(int p = 1) {
		param = p;
	}
	friend void fun(Test& obj);
};

void fun(Test& obj) {
	cout << "�������� ��������� W = " << obj.W << endl;
	obj.Z();
}

// --------------
//  ������� 4-5
// --------------

// ����� Homework.
class Student;

class Homework {
private:
	int course;
	string deadline;
	map<string, string> disciplines;
	friend class Student;
public:
	Homework() : deadline("tomorrow"), course(3), disciplines({ { "Math", "closed" }, { "Science", "closed" }, {"C++", "open"}, {"Python", "open"} }) {}
};

// ����� Student - ���� ������ Homework.
class Student {
private:
	string name;
	string group;
	int birth;
	Homework hm;
public:
	Student(Homework homework, string n = "Nikita", string gp = "VMO31", int b = 2003) :
		name(n), group(gp), birth(b), hm(homework) {}

	void set_dp_as_closed(string dp) {
		hm.disciplines[dp] = "closed";
	}

	void work_on_dp(string dp) {
		if (hm.disciplines[dp] == "open") {
			cout << "------------------------------------------------------------" << endl;
			cout << "Working on discipline " << dp << "..." << endl;
			set_dp_as_closed(dp);
			cout << "Homework on discipline " << dp << " is successfully closed!" << endl;
			cout << "------------------------------------------------------------" << endl;
			return;
		}
		else if (hm.disciplines[dp] == "closed") {
			cout << "-------------------------------------------------------------" << endl;
			cout << "Discipline " << dp << " is already closed. Be happy, dear Student!" << endl;
			cout << "-------------------------------------------------------------" << endl;
			return;
		}
		else {
			cout << "-------------------------------------------------------------" << endl;
			cout << "Set the acceptable status for discipline " << dp << "!" << endl;
			cout << "-------------------------------------------------------------" << endl;
			return;
		}
	}

	void operator=(const Student& s)
	{
		name = s.name;
		group = s.group;
		birth = s.birth;
		hm = s.hm;
	}

	string get_name() {
		return name;
	}

	string get_group() {
		return group;
	}

	int get_course() {
		return hm.course;
	}

	int get_birth() {
		return birth;
	}

	Homework get_hm() {
		return hm;
	}
};


int main() {
	setlocale(LC_ALL, "Russian");

	// -------------
	//  ������� 1-3
	// -------------
	Test t;
	fun(t);

	// ------------
	//  ������� 5
	// ------------
	Homework hm;
	Student stud(hm);
	Student stud1(hm);

	cout << stud.get_course() << endl;

	//stud = stud1;

	//cout << stud1.get_name() << endl;
	//cout << stud1.get_course() << endl;
	//cout << stud1.get_group() << endl;

	/*stud.work_on_dp("Math");
	stud.work_on_dp("Python");
	stud.work_on_dp("Python");
	stud.work_on_dp("Something");*/


	return 0;
}