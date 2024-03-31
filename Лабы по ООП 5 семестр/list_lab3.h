#pragma once

class List {
	// �������� ��������� �����
	class ListNode {
	public:
		int key; // ���������� ��� ������� ���� ��������
		char* data; // ������, ���������� � ����
		ListNode* prev, * next; /* ��������� �� ���������� �
		��������� ���� */
	};
	ListNode* first; // ��������� �� ������ ���� ������
public:
	List() : first(0) {}
	~List() { del(); }
	void addData(int key, char* data); // �������� ����
	void removeData(int key); // ������� ���� � ���������
	char* findData(int key); // ������� ������ �� �����
	void show(); // ���������� ������ � ���������� ����
private:
	ListNode* findNode(int key); // ����� ���� �� �����
	void del(); // ������� ��� ���� �� ������
};
