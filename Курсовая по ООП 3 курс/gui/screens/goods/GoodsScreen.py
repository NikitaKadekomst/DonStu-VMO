import re
from threading import Timer
from tkinter import *
from gui.custom.ColoredButton import ColoredButton
from gui.screens.MenuScreen import *
from gui.screens.MenuScreen import MenuScreen
from gui.screens.goods.AddGoodScreen import AddGoodScreen as AddGoodsScreenCLS
from gui.screens.goods.ResultScreen import ResultScreen as ResultScreenCLS


# Класс GoodsScreen.
# Меню для работы с товарами склада.
# --------------------------------------------------------
# Функционал для взаимодействия со списком товаров.
# Наследуется от класса MenuScreen - базового шаблона
# внутренних экранов приложения.
# --------------------------------------------------------
class GoodsScreen(MenuScreen):
    def __init__(self, parent, controller):
        MenuScreen.__init__(self, parent, controller, "auth")

        # Информация о запрошенном товаре.
        self.info = {}
        self.db_items = []

        # Поле-фильтр.
        self.search_str = StringVar(value="Фильтр позиций по ключевым словам/буквам (Enter для запуска)")
        self.filter_entry = Entry(width=76, textvariable=self.search_str)
        self.filter_entry.place(relx=0.16, rely=0.36)
        self.filter_entry.bind('<Return>', self.filter_data)
        self.filter_entry.bind("<Button-1>", self.filter_clear)

        # Кнопка "Получить информацию".
        self.get_item_info_button = ColoredButton(self, width=15, text="Информация",
                                                  command=self.show_requested_info)
        self.get_item_info_button.place(relx=0.27, rely=0.3, anchor=CENTER)

        # Кнопка "Добавить вещь".
        self.add_item_button = ColoredButton(self, width=15, text="Добавить вещь", command=self.add_item)
        self.add_item_button.place(relx=0.49, rely=0.3, anchor=CENTER)

        # Кнопка "Удалить вещь".
        self.delete_item_button = ColoredButton(self, width=15, text="Удалить вещь", command=self.delete_item)
        self.delete_item_button.place(relx=0.71, rely=0.3, anchor=CENTER)

    # -------------------
    #       МЕТОДЫ
    # -------------------

    # GoodsScreen.display_goods_list()
    # -----------------------------------------------------------
    # Получить актуальный список товаров из базы данных.
    # -----------------------------------------------------------
    # Данный метод получает информацию из БД в виде актуального
    # списка товаров в системе.
    # Полученный список выводит в соответствующий listbox.
    # -----------------------------------------------------------
    def display_goods_list(self):
        # Запрос в БД для получения данных и вспомогательный словарь для их представления.
        data = self.controller.db.select_from_table("goods", False, ["id", "title"])
        self.db_items = []
        item_ID = 1

        # Заполнение вспомогательного словаря.
        for row in data:
            title = row["title"]
            self.db_items.append(f"{item_ID}. {title}")
            item_ID += 1

        # Блок со списком названий товаров из БД.
        items_var = Variable(value=self.db_items)
        self.items_listbox = Listbox(listvariable=items_var,
                                     selectmode=EXTENDED,
                                     width=70,
                                     height=20,
                                     font=("Arial Bold", 9),
                                     cursor="hand2")
        self.items_listbox.place(relx=0.5, rely=0.65, anchor=CENTER)

        # Настройки прокрутки.
        self.items_listbox_scroll = Scrollbar(command=self.items_listbox.yview, orient=VERTICAL, cursor="hand2")
        self.items_listbox.config(yscrollcommand=self.items_listbox_scroll.set)
        self.items_listbox_scroll.place(in_=self.items_listbox, relx=1.0, relheight=1.0, bordermode="outside")

    # GoodsScreen.show_requested_info()
    # ----------------------------------------------------------
    # Получить информацию о выбранной пользователем вещи.
    # -----------------------------------------------------------
    # Вычленяет из листбокса выделенное поле title вещи.
    # По этому полю запрашивает полную информацию о вещи из БД.
    # Отправляет информацию на экран отображения.
    # Отображает сам экран с информацией.
    # -----------------------------------------------------------
    # АРГУМЕНТЫ
    # --*args = базовые аргументы для обработчика
    # пользовательского события в модуле Tkinter
    # -----------------------------------------------------------
    def show_requested_info(self, *args):
        selected_item_title = ""

        # Если пользователь забыл выбрать вещь для просмотра, вывести об этом сообщение.
        if not self.items_listbox.curselection():
            self.user_message.config(text="Выберите позицию из списка для получения информации!", fg="red")
            return

        # Вычленяем заголовок в формате, соотносящимся с полем в БД.
        for i in self.items_listbox.curselection():
            pattern = r'^\d+\.\s(.*)$'
            string = self.items_listbox.get(i)
            selected_item_title = re.match(pattern, string).group(1)

        # Запрашиваем информацию о вещи из БД по заголовку.
        info = self.controller.db.select_from_table("goods", star=True, where_cond=f"title='{selected_item_title}'")

        if not info:
            self.user_message.config(text="Не удалось получить информацию о данной вещи!", fg="red")
            return

        self.controller.show_frame(ResultScreenCLS, info)

    # GoodsScreen.add_item()
    # -------------------------------------------------
    # Обработчик нажатия на кнопку "Добавить вещь".
    # ---------------------------------------------------
    # При нажатии на кнопку "Добавить вещь" пользователь
    # открывает экран-меню, позволяющее вручную добавить
    # новую вещь в систему.
    # ---------------------------------------------------
    def add_item(self):
        self.controller.hide_goods_screen_content()
        self.controller.show_frame(AddGoodsScreenCLS)

    # GoodsScreen.delete_item()
    # ---------------------------------------------------
    # Удаление вещи из базы данных.
    # ---------------------------------------------------
    # При нажатии на кнопку "Удалить вещь" пользователь
    # удаляет выбранную в списке товаров вещь из базы
    # данных системы.
    # ---------------------------------------------------
    def delete_item(self):
        selected_item_title = ""

        # Если пользователь забыл выбрать вещь для удаления, вывести об этом сообщение.
        if not self.items_listbox.curselection():
            self.user_message.config(text="Выберите позицию из списка для удаления!", fg="red")
            return

        for i in self.items_listbox.curselection():
            selected_item_title = re.sub(r"[0-9]+. [0-9]*", "", self.items_listbox.get(i))

        self.controller.db.delete_single_row_from_table("goods", "title", selected_item_title)
        self.user_message.config(text="Выбранная вещь успешно удалена из БД!", fg="green")

        # Очищение всех сообщений пользователю через msg_erase_interval секунд после появления.
        msg_erase_interval = 4.0
        timer = Timer(msg_erase_interval, self.clear_messages)
        timer.start()

        # Обновление контента после удаления.
        self.controller.hide_goods_screen_content()
        self.display_goods_list()
        self.configure_filter_entry("place")

    # GoodsScreen.filter_data()
    # ----------------------------------------------------------
    # Фильтрация позиций по ключевым словам.
    # ----------------------------------------------------------
    # Алгоритм работы поля фильтрации по ключевым словам.
    # Для запуска фильтра требуется нажать Enter.
    # ----------------------------------------------------------
    # АРГУМЕНТЫ
    # --*args = базовые аргументы для обработчика
    # пользовательского события в модуле Tkinter
    # -----------------------------------------------------------
    def filter_data(self, *args):
        sstr = self.filter_entry.get()
        self.items_listbox.delete(0, END)

        if sstr == "":
            for item in self.db_items:
                self.items_listbox.insert(END, item)
            return

        filtered_data = list()
        for item in self.db_items:
            if item.find(sstr) >= 0:
                filtered_data.append(item)

        for item in filtered_data:
            self.items_listbox.insert(END, item)

    # GoodsScreen.configure_filter_entry()
    # ---------------------------------------------------
    # Настройки отображения поля для фильтрации списка.
    # ---------------------------------------------------
    # АРГУМЕНТЫ
    # --mode (place, forget) = режим отображения или
    # скрытия поля
    # ---------------------------------------------------
    def configure_filter_entry(self, mode):
        if mode == "place":
            self.filter_entry.place(relx=0.16, rely=0.36)
        if mode == "forget":
            self.filter_entry.place_forget()

    # GoodsScreen.clear_messages()
    # -------------------------------------
    # Очистка пользовательских сообщений.
    # -------------------------------------
    def clear_messages(self):
        self.user_message.configure(text="")

    # GoodsScreen.filter_clear()
    # ----------------------------------------------
    # Очистка поля-фильтра при клике.
    # ----------------------------------------------
    # АРГУМЕНТЫ
    # --*args = базовые аргументы для обработчика
    # пользовательского события в модуле Tkinter
    # -----------------------------------------------
    def filter_clear(self, *args):
        self.filter_entry.delete(0, END)
