import time
from core.auth.Auth import *
from gui.custom.TransparentButton import *
from gui.screens.AuthScreen import *
from gui.screens.goods.GoodsScreen import GoodsScreen as GoodsScreenCLS


# Класс LoginScreen экрана авторизации в системе.
# ---------------------------------------------------------
# Пользователь вводит логин и пароль для входа в систему.
# Наследуется от класса-шаблона экранов доступа AuthScreen.
# ---------------------------------------------------------
class LoginScreen(AuthScreen):
    def __init__(self, parent, controller):
        AuthScreen.__init__(self, parent, controller, "Вход")

        # Кнопка "Войти в систему".
        self.send_button = ColoredButton(self, text="Войти в систему", command=self.set_access_status)
        self.send_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Кнопка "Cоздать аккаунт".
        self.send_button = TransparentButton(self, text="Cоздать аккаунт", command=self.controller.show_registration_page)
        self.send_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    # LoginScreen.set_access_status()
    # -------------------------------------------------------------------
    # Вывод пользовательских сообщений о текущем статусе входа в систему.
    # Вход в систему в случае успешного статуса.
    # -------------------------------------------------------------------
    def set_access_status(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" and password == "":
            self.access_message.configure(text="Введите данные для входа!")
            self.access_message.configure(fg="red")
            return

        if username == "":
            self.access_message.configure(text="Введите имя пользователя!")
            self.access_message.configure(fg="red")
            return

        if password == "":
            self.access_message.configure(text="Введите пароль для входа!")
            self.access_message.configure(fg="red")
            return

        # Дать ли пользователю доступ в систему.
        access_status = self.controller.auth.verify_access(username, password)
        self.access_message.configure(text=access_status)

        # Конфигурация сообщения.
        if access_status == "Доступ разрешён!":
            self.controller.show_frame(GoodsScreenCLS)
            self.controller.show_goods_screen_content()
        elif access_status == "Неверный пароль!" or access_status == f"Пользователь с ником \"{username}\" не найден!":
            self.access_message.configure(fg="red")
