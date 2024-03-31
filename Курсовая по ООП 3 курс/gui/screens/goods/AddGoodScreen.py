from gui.custom.ColoredButton import *
from gui.screens.MenuScreen import *
from gui.screens.MenuScreen import MenuScreen


# Экран приложения для добавления вещи в БД.
# --------------------------------------------------------
# Наследуется от класса Frame библиотеки Tkinter.
# --------------------------------------------------------
class AddGoodScreen(MenuScreen):
    def __init__(self, parent, controller):
        MenuScreen.__init__(self, parent, controller, "list")

        # --Текущая страница.
        self.user_label = Label(self, text="Добавить вещь в БД", font=("Arial Bold", "11"))
        self.user_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        # --Словарь базовых полей.
        self.fields_info = {"Название": "title", "Категория": "category", "Бренд": "brand", "Цвета": "colors",
                            "Цена": "price", "Описание": "description", "Структура": "structure"}

        # --Вывод полей.
        self.print_fields(0.27, 0.32, 4)

        # --Кнопка "Добавить данные в базу".
        self.append_to_db_btn = ColoredButton(self, text="Добавить в базу данных", command=self.add_to_db)
        self.append_to_db_btn.place(relx=0.5, rely=0.88, anchor=CENTER)

    # -------------------
    #       МЕТОДЫ
    # -------------------

    # AddGoodScreen.configure_fields()
    # -----------------------------------------------------------------
    # Настройка отображения полей при переключении экранов
    # -----------------------------------------------------------------
    # АРГУМЕНТЫ:
    # --mode (place, forget) = режим отображения (place - отобразить,
    # forget - скрыть)
    # --relx_start, rely_start, column_count = см. метод print_fields()
    # -----------------------------------------------------------------
    def configure_fields(self, mode, relx_start=0.3, rely_start=0.32, column_count=4):
        if mode == "place":
            self.print_fields(relx_start, rely_start, column_count)
        if mode == "forget":
            for name in self.fields_info:
                entry_name = f"{self.fields_info[name]}_entry"
                getattr(AddGoodScreen, entry_name).place_forget()

    # AddGoodScreen.print_fields()
    # -------------------------------------------------
    # Генерация полей для ввода данных о новой вещи.
    # -------------------------------------------------
    # АРГУМЕНТЫ:
    # --relx_start (float) = координата x первого поля.
    # --rely_start (float) = координата y первого поля.
    # --column_count (int) = количество полей в столбце.
    # --------------------------------------------------
    def print_fields(self, relx_start, rely_start, column_count):
        relx = relx_start
        rely = rely_start
        i = 0

        for name in self.fields_info:
            # Установка расстояния между столбцами по координате x.
            if (i + 1) % (column_count + 1) == 0:
                relx += 0.25
                rely = rely_start

            label_name = f"{self.fields_info[name]}_label"
            entry_name = f"{self.fields_info[name]}_entry"

            # Инициализация и отображение лейбла поля.
            setattr(AddGoodScreen, label_name, Label(self, text=name, font=("Arial Bold", 10)))
            getattr(AddGoodScreen, label_name).place(relx=relx, rely=rely)
            rely = rely + 0.05

            # Инициализация и отображение самого поля.
            setattr(AddGoodScreen, entry_name, Entry())
            getattr(AddGoodScreen, entry_name).place(relx=relx, rely=rely)
            rely = rely + 0.07

            i += 1

    # AddGoodScreen.add_to_db()
    # ----------------------------------------------
    # Добавление новой вещи в базу данных.
    # ----------------------------------------------
    def add_to_db(self):
        db_info = {}

        for name in self.fields_info:
            entry_name = f"{self.fields_info[name]}_entry"
            entry_value = getattr(AddGoodScreen, entry_name).get()
            if not entry_value:
                self.user_message.configure(
                    text="Заполните все указанные поля! (при отсутствии значения параметра используйте прочерк)",
                    fg="red")
                return
            db_info[self.fields_info[name]] = entry_value

        resp = self.controller.db.insert_single_row_into_table("goods", list(db_info.keys()), list(db_info.values()))

        if not resp:
            self.user_message.configure(text="Данные успешно добавлены в базу!", fg="green")
            return
        if resp:
            self.user_message.configure(text="Ошибка при добавлении в базу...", fg="red")
