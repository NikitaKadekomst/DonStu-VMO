from core.auth.Auth import *

from gui.custom.TransparentButton import *
from gui.screens.auth.LoginScreen import LoginScreen
from gui.screens.goods.GoodsScreen import *
from gui.screens.AuthScreen import *
from gui.screens.auth.LoginScreen import LoginScreen as LoginScreenCLS


# Класс RegisterScreen
# Экран регистрации нового пользователя.
# ---------------------------------------
class RegisterScreen(AuthScreen):
    def __init__(self, parent, controller):
        AuthScreen.__init__(self, parent, controller, "Регистрация")

        # Кнопка "Зарегистрироваться".
        self.send_button = ColoredButton(self, text="Зарегистрироваться", command=self.register_user)
        self.send_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Кнопка "Вход в аккаунт".
        self.send_button = TransparentButton(self, text="Уже есть аккаунт",
                                             command=lambda: self.controller.show_frame(LoginScreenCLS))
        self.send_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    # Регистрация пользователя.
    # ------------------------------------------------------
    # Обработчик кнопки "Зарегистрироваться".
    # Проверяет корректность введенных данных.
    # В случае успеха переводит на страницу входа в систему.
    # ------------------------------------------------------
    def register_user(self, *args):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Создает права для нового пользователя.
        new_user = self.controller.auth.register_new_user(username, password)

        # Сообщение пользователю.
        if new_user == f"Пользователь с ником {username} уже существует!":
            self.access_message.configure(fg="red")
            self.access_message.configure(text=new_user)
            return

        # Отобразить окно для входа.
        self.controller.show_frame(LoginScreenCLS)



