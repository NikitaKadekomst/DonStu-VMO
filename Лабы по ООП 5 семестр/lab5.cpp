// 1. Создайте класс, который содержит счетчик созданных
// объектов. Напишите программу - тест, в которой проверяется,
// сколько объектов класса создано при входе в функцию main,
// после статического создания массива объектов, после
// динамического создания объекта, после удаления динамического
// объекта.
// 2. Создайте класс с закрытыми конструкторами и
// деструктором. Реализуйте методы для создания и уничтожения
// объектов класса. Напишите программу - тест.
// 3. Создайте класс, для которого возможно создание только
// одного объекта.
// 4. Создайте класс на Java со статическими полями и
// методами. Инициализируйте статические поля в статическом
// блоке инициализации.

#include <iostream>
#include <clocale>
using namespace std;

// ----------
// ЗАДАНИЕ 1
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


// Статические свойства/методы должны
// объявляться за пределами описания класса
// свойства - обязательно,
// методы - рекомендуемо.
int Counter::total;

int Counter::get_num_of_instances() {
	return total;
}

// ----------
// ЗАДАНИЕ 2
// ----------
class Closed {
private:
    Closed() {}
    ~Closed() {}
public:
   
};

// ----------
// ЗАДАНИЕ 3
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
    // ЗАДАНИЕ 1
    // ----------
	/*Counter c1;
	Counter c2;
	Counter c3;*/
	/*
	Counter* c4 = new Counter();
	Counter* c5 = new Counter();*/

  /*  cout << "Количество созданных объектов класса Counter = " << Counter::get_num_of_instances() << endl;

    delete c4;

    cout << "Количество созданных объектов класса Counter = " << Counter::get_num_of_instances() << endl;*/

    // ----------
    // ЗАДАНИЕ 3
    // ----------
	Singleton* s = Singleton::getInstance();
    s->setValues("Nikita", "C++");
    
    Singleton* s1 = Singleton::getInstance();
    s1->print();

	return 0;
}