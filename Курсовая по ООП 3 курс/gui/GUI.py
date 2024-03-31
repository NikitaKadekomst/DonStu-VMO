from tkinter import *

# Страницы доступа в систему.
from gui.screens.auth.RegisterScreen import RegisterScreen as RegisterScreenCLS
from gui.screens.auth.LoginScreen import LoginScreen as LoginScreenCLS

# Страницы-меню для работы с товаропотоком.
from gui.screens.goods.GoodsScreen import GoodsScreen as GoodsScreenCLS
from gui.screens.goods.ResultScreen import ResultScreen as ResultScreenCLS
from gui.screens.goods.AddGoodScreen import AddGoodScreen as AddGoodScreenCLS


# Класс GUI (Graphical User Interface)
# ------------------------------------------------------
# Входная точка в интерфейс.
# Управляет сменой экранов в приложении.
# Наследуется от основного класса Tk библиотеки Tkinter.
# ------------------------------------------------------
class GUI(Tk):
    def __init__(self, width, height, background, db, auth, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.width = width
        self.height = height
        self.base_bg = background
        self.db = db
        self.auth = auth

        # Ширина/высота экрана на устройстве.
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()

        # Координаты Tkinter-окна.
        self.x = (self.ws / 2) - (self.width / 2)
        self.y = (self.hs / 2) - (self.height / 2)

        # Расположение окна на экране.
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        self.configure(background=self.base_bg)
        self.title("Система учета товаропотока сортировочного центра")

        # Создание базового контейнера.
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Словарь для хранения экземпляров каждого экрана в приложении.
        self.frames = {}

        # Кортеж имен всех экранов приложения.
        self.screens = (LoginScreenCLS, RegisterScreenCLS,
                        GoodsScreenCLS, ResultScreenCLS,
                        AddGoodScreenCLS)

        # При запуске приложения отображается страница авторизации в системе.
        self.show_frame(LoginScreenCLS)

    # GUI.show_frame()
    # ----------------------------------------------
    # Отображение заданной страницы интерфейса.
    # -----------------------------------------------
    # АРГУМЕНТЫ
    # --сont (class name) = имя класса страницы.
    # --data (any) = информация, которую требуется
    # передать на запускаемый экран.
    # -----------------------------------------------
    def show_frame(self, scr, data=""):
        frame = ""
        cont = scr

        # Передача данных из БД на экран результата.
        if cont == ResultScreenCLS:
            frame = cont(self.container, self, data)
            self.hide_goods_screen_content()
        else:
            frame = cont(self.container, self)

        self.frames[cont] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    # GUI.set_backup_mode()
    # ---------------------------------------------
    # Метод для управления поведением возврата
    # на предыдущий экран в приложении.
    # ---------------------------------------------
    # АРГУМЕНТЫ
    # --*args = базовые аргументы для обработчика
    # пользовательского события в модуле Tkinter
    # ----------------------------------------------
    def set_backup_mode(self, backup_mode, *args):
        if backup_mode == "auth":
            self.hide_goods_screen_content()
            self.show_frame(LoginScreenCLS)
        if backup_mode == "list":
            self.configure_add_item_fields("forget")
            self.hide_good_table()
            self.show_goods_screen_content()

    # GUI.show_goods_screen_content()
    # -----------------------------------------
    # Отобразить контент экрана взаимодействия
    # со списком товаров при переключении
    # экранов.
    # ------------------------------------------
    def show_goods_screen_content(self):
        if GoodsScreenCLS in self.frames:
            self.frames[GoodsScreenCLS].display_goods_list()
            self.frames[GoodsScreenCLS].clear_messages()
            self.frames[GoodsScreenCLS].configure_filter_entry("place")
            self.frames[GoodsScreenCLS].tkraise()

    # GUI.hide_goods_screen_content()
    # -------------------------------------
    # Скрыть контент экрана взаимодействия
    # со списком товаров при переключении
    # экранов.
    # --------------------------------------
    def hide_goods_screen_content(self):
        if GoodsScreenCLS in self.frames:
            self.frames[GoodsScreenCLS].items_listbox.place_forget()
            self.frames[GoodsScreenCLS].filter_entry.place_forget()

    # GUI.hide_good_table()
    # ------------------------------------------
    # Скрыть таблицу с данными о выбранной вещи.
    # -------------------------------------------
    def hide_good_table(self):
        if ResultScreenCLS in self.frames:
            self.frames[ResultScreenCLS].hide_good_table()

    # GUI.configure_add_item_fields()
    # --------------------------------------------------
    # Настройка отображения полей экрана "Добавить вещь"
    # ---------------------------------------------------
    # АРГУМЕНТЫ
    # --mode = режим отображения полей.
    # ---------------------------------------------------
    def configure_add_item_fields(self, mode):
        if AddGoodScreenCLS in self.frames:
            self.frames[AddGoodScreenCLS].configure_fields(mode)

    # GUI.show_registration_page()
    # ------------------------------------------------
    # Отображение экрана регистрации в системе.
    # ------------------------------------------------
    # Выводит фрейм с меню для регистрации нового
    # пользователя в приложении.
    # ------------------------------------------------
    def show_registration_page(self, *args):
        self.show_frame(RegisterScreenCLS)

    # GUI.run()
    # -----------------------------------------------
    # Запуск интерфейса.
    # ------------------------------------------------
    # Запускает весь интерфейс в основном классе Main
    # ------------------------------------------------
    def run(self):
        self.mainloop()
