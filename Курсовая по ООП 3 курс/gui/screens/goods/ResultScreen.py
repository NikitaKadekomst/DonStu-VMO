from gui.custom.ColoredButton import *
from gui.screens.MenuScreen import *


# Окно информации о выбранной вещи.
# --------------------------------------------------------
# Функционал для взаимодействия со списком товаров.
# Наследуется от класса Frame библиотеки Tkinter.
# --------------------------------------------------------
class ResultScreen(MenuScreen):
    def __init__(self, parent, controller, info):
        MenuScreen.__init__(self, parent, controller, "list")

        # --Информация о запрошенном товаре
        # Передается аргумент info при инициализации экземпляра
        # класса во время вызова GUI.show_frame(ResultScreen, info)
        self.info = info

        # --Заголовок рассматриваемой вещи.
        self.title = ""

        # --Вспомогательный словарь для печати таблицы.
        self.entity_info = {"Название": "title", "Категория": "category", "Бренд": "brand", "Цвета": "colors",
                            "Цена": "price", "Описание": "description", "Структура": "structure"}

        # --Информация о пользователе.
        self.user_label = Label(self, font=("Arial Bold", "11"))
        self.user_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        # --Инициализация фрейма таблицы.
        self.table_frame = Frame(borderwidth=1, relief=SOLID)

        # --Вывод таблицы с информацией о выбранной вещи.
        self.print_table()

        # Кнопка "Сохранить изменения".
        self.delete_item_button = ColoredButton(self, text="Сохранить изменения", command=self.save_changes)
        self.delete_item_button.place(relx=0.5, rely=0.91, anchor=CENTER)

    # -------------------
    #       МЕТОДЫ
    # -------------------

    # ResultScreen.hide_good_table()
    # --------------------------------------
    # Скрывает таблицу с информацией о вещи
    # --------------------------------------
    def hide_good_table(self):
        self.table_frame.place_forget()

    # ResultScreen.print_info()
    # ---------------------------------------------------------
    # Вывод таблицы с информацией о вещи.
    # --------------------------------------------------------
    # АРГУМЕНТЫ:
    # --max_entry_height = максимальная высота поля в строках
    # --bg = цвет заднего поля фона.
    # --font = шрифт текста в поле.
    # --include_emp = режим отображения полей со значением "-"
    # ---------------------------------------------------------
    def print_table(self, max_entry_height=15, bg="#e3e3e3", font=('Arial Bold', "11"), include_emp=False):
        # Изначальные данные.
        data_dict = {}
        table_list = []
        initial_data = self.info[0]

        # Формируем удобный словарь данных для дальнейшего добавления в табличный список.
        for key in initial_data:
            for entity_key in self.entity_info:
                if key == self.entity_info[entity_key]:
                    if initial_data[key] == "-" and not include_emp:
                        continue
                    data_dict[entity_key] = initial_data[key]

        # Добавление в табличный список.
        # Получение названия выбранной вещи.
        good_title = ""
        for param in data_dict:
            if param == "Название":
                good_title = data_dict[param]
                self.title = good_title
            table_list.append(tuple([param, data_dict[param]]))

        # Заполнение таблицы.
        total_rows = len(data_dict.values())
        for i in range(total_rows):
            for j in range(2):
                width = 15 if j == 0 else 50
                cell_plain_text = ""
                cell_name = ""

                # Формирование имени для ячеек с названиями параметров.
                if j == 0:
                    cell_plain_text = table_list[i][j]
                    for name in self.entity_info:
                        if name == cell_plain_text:
                            cell_name = f"{self.entity_info[name]}_cell"

                # Формирование имени для ячеек с описаниями параметров.
                if j == 1:
                    prev_cell_plain_text = table_list[i][j - 1]
                    cell_plain_text = table_list[i][j]
                    for name in self.entity_info:
                        if name == prev_cell_plain_text:
                            cell_name = f"{self.entity_info[name]}_desc_cell"

                # Базовое ограничение по высоте ячейки.
                height = len(cell_plain_text) / width
                if height > max_entry_height:
                    height = max_entry_height

                # Ячейка с названием свойства должна иметь ту же высоту,
                # что и ячейка с ее описанием.
                if table_list[i][j - 1]:
                    prev_cell = table_list[i][j - 1]
                    for name in self.entity_info:
                        if name == prev_cell and hasattr(ResultScreen, f"{self.entity_info[prev_cell]}_cell"):
                            getattr(ResultScreen, f"{self.entity_info[prev_cell]}_cell").configure(height=height)

                # Инициализация.
                setattr(ResultScreen, cell_name, Text(self.table_frame, width=width, bg=bg, font=font))

                # Настройка расположения и вставка текста.
                getattr(ResultScreen, cell_name).grid(row=i, column=j, padx=1, pady=1)
                getattr(ResultScreen, cell_name).configure(height=height)
                getattr(ResultScreen, cell_name).insert(END, cell_plain_text)

        # Конфигурация заголовка.
        self.user_label.configure(text=f"Информация о вещи \"{good_title}\"")

        # Расположение таблицы.
        self.table_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

    # ResultScreen.save_changes()
    # -------------------------------------------------------
    # Запись в базу данных новой информации о выбранной вещи.
    # -------------------------------------------------------
    def save_changes(self):
        row_info = {}

        for name in self.entity_info:
            cell_name = f"{self.entity_info[name]}_desc_cell"
            cell_value = ""

            if hasattr(ResultScreen, cell_name):
                cell_value = getattr(ResultScreen, cell_name).get("1.0", END)

            row_info[self.entity_info[name]] = cell_value

        self.controller.db.update_row("goods", row_info, f"title='{self.title}'")
        self.user_message.configure(text="Данные успешно обновлены в базе!", fg="green")
