#pragma once

class List {
	// закрытый вложенный класс
	class ListNode {
	public:
		int key; // уникальное для каждого узла значение
		char* data; // данные, хранящиеся в узле
		ListNode* prev, * next; /* указатели на предыдущий и
		следующий узлы */
	};
	ListNode* first; // указатель на первый узел списка
public:
	List() : first(0) {}
	~List() { del(); }
	void addData(int key, char* data); // добавить узел
	void removeData(int key); // удалить узел с указанным
	char* findData(int key); // вернуть данные по ключу
	void show(); // отобразить список в консольном окне
private:
	ListNode* findNode(int key); // поиск узла по ключу
	void del(); // удалить все узлы из списка
};
