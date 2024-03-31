using namespace std;
#include <iostream>
#include <cstring>
#include <clocale>

//1. Создать структуру "Студент" содержащую следующие поля: 
//- имя студента 
//- отчество студента 
//- фамилию студента 
//- год рождения 
//- группа. 
//
//2. Определить конструктор для инициализации полей структуры 
//со значениями по умолчанию.Определить конструктор копирования 
//и деструктор.Написать тестовый пример.
//
//3. Изменить в описании структуры ключевое слово struct на class.
//Запустить программу.Какие возникли проблемы ? 
//Почему ? Как их исправить ? 
//
//4. Написать интерфейсные функции доступа к полям 
//класса(получить / задать значение поля). 
//
//5. Внести в конструкторы и деструктор выдачу сообщений 
//на экран о том, какая функция была вызвана.
//Модифицировать функцию main следующим образом : 
//void main(void) { cout << "Вход в функцию main()" << endl; 
// ... <тело_main()> ... cout << "Выход из функции main()" << endl; } 
//Выяснить время вызовов конструкторов и деструкторов. 
//
//6. Описать глобальную функцию Student test(Student s) { return s; } 
//Вызвать ее в основной программе.Что произошло и почему ? 
//
//7. Изменить передачу параметра ф - и test на передачу по ссылке.
//Что изменилось ? 
//
//8. Изменить возврат результата ф - и test на передачу по ссылке.
//Что изменилось ?

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
		cout << "Произошел вызов конструктора!" << endl;
		cout << "-----------------------------" << endl;

		birth = b;
		name = nm;
		surname = sm;
		lastname = lm;
		group = gr;
	}
	Student(const Student &p) {
		cout << "-----------------------------------------" << endl;
		cout << "Произошел вызов конструктора копирования!" << endl;
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
		cout << "Произошел вызов деструктора!" << endl;
		cout << "-----------------------------" << endl;
	}
	
	// Геттеры для полей.

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

	// Сеттеры для полей

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
	cout << "Вход в функцию main()" << endl; 
	cout << "----------------------" << endl;

	string d_or_c = "default";
	cout << "Введите режим работы: начальные значения (default) или кастомные (custom)?: ";
	cin >> d_or_c;

	if (d_or_c == "custom") {
		string name;
		cout << "Имя студента: ";
		cin >> name;

		string lastname;
		cout << "Фамилия студента: ";
		cin >> lastname;

		string surname;
		cout << "Отчество студента: ";
		cin >> surname;

		int birth = 2003;

		string group;
		cout << "Группа студента: ";
		cin >> group;

		Student student(name, surname, lastname, birth, group);
		cout << "Фамилия студента: " << student.getLastname() << endl;
		cout << "Отчество студента: " << student.getSurname() << endl;
		cout << "Имя студента: " << student.getName() << endl;
		cout << "Группа студента: " << student.getGroupName() << endl;
		student.setGroup("VMO31");
		cout << "Группа студента: " << student.getGroupName() << endl;
	}
	else {
		Student stud;
		cout << "Фамилия студента: " << stud.getLastname() << endl;
		cout << "Группа студента: " << stud.getGroupName() << endl;
		cout << "Начальное отчество студента: " << stud.getSurname() << endl;
		stud.setSurname("Alexandrovich");
		cout << "Новое отчество студента: " << stud.getSurname() << endl;

		Student c_stud(stud);
		cout << "Скопированное значение отчества: " << c_stud.getSurname() << endl;

		Student d_stud(stud);
	}

	cout << "------------------------" << endl;
	cout << "Выход из функции main()" << endl;
	cout << "------------------------" << endl;
}