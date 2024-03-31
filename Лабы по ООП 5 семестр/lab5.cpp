// 1. �������� �����, ������� �������� ������� ���������
// ��������. �������� ��������� - ����, � ������� �����������,
// ������� �������� ������ ������� ��� ����� � ������� main,
// ����� ������������ �������� ������� ��������, �����
// ������������� �������� �������, ����� �������� �������������
// �������.
// 2. �������� ����� � ��������� �������������� �
// ������������. ���������� ������ ��� �������� � �����������
// �������� ������. �������� ��������� - ����.
// 3. �������� �����, ��� �������� �������� �������� ������
// ������ �������.
// 4. �������� ����� �� Java �� ������������ ������ �
// ��������. ��������������� ����������� ���� � �����������
// ����� �������������.

#include <iostream>
#include <clocale>
using namespace std;

// ----------
// ������� 1
// ----------
class Counter {
	static int total;
public:
	Counter() {
		total++;
	}
	~Counter() {
		total--;
	}

	static int get_num_of_instances();
};


// ����������� ��������/������ ������
// ����������� �� ��������� �������� ������
// �������� - �����������,
// ������ - ������������.
int Counter::total;

int Counter::get_num_of_instances() {
	return total;
}

// ----------
// ������� 2
// ----------
class Closed {
private:
    Closed() {}
    ~Closed() {}
public:
   
};

// ----------
// ������� 3
// ----------
class Singleton {
private:
    string name, loves;
    static Singleton*
    instancePtr;
    Singleton() {}

public:
    Singleton(const Singleton& obj)
        = delete;

    static Singleton* getInstance()
    {
        if (instancePtr == NULL)
        {
            instancePtr = new Singleton();
            return instancePtr;
        }
        else
        {
            return instancePtr;
        }
    }

    void setValues(string name,
        string loves)
    {
        this->name = name;
        this->loves = loves;
    }

    void print()
    {
        cout << name << " Loves " <<
            loves << "." << endl;
    }
};

Singleton* Singleton::instancePtr = NULL;

int main() {
	setlocale(LC_ALL, "Russian");

    // ----------
    // ������� 1
    // ----------
	/*Counter c1;
	Counter c2;
	Counter c3;*/
	/*
	Counter* c4 = new Counter();
	Counter* c5 = new Counter();*/

  /*  cout << "���������� ��������� �������� ������ Counter = " << Counter::get_num_of_instances() << endl;

    delete c4;

    cout << "���������� ��������� �������� ������ Counter = " << Counter::get_num_of_instances() << endl;*/

    // ----------
    // ������� 3
    // ----------
	Singleton* s = Singleton::getInstance();
    s->setValues("Nikita", "C++");
    
    Singleton* s1 = Singleton::getInstance();
    s1->print();

	return 0;
}