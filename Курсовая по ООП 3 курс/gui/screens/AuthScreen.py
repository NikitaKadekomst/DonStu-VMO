from gui.custom.ColoredButton import *


# Класс AuthScreen
# Шаблон экрана аутентификации.
class AuthScreen(Frame):
    def __init__(self, parent, controller, auth_type=""):
        Frame.__init__(self, parent)
        self.controller = controller

        # Основной заголовок.
        self.heading_label = Label(self, text="Система учета товаропотока\n сортировочного центра",
                                   font=("Arial Bold", 14), padx=15, pady=10)
        self.heading_label.place(relx=0.5, rely=0.15, anchor=CENTER)

        # Вид аутентификации.
        self.auth_label = Label(self, text=auth_type,
                                   font=("Arial Bold", 13), padx=15, pady=10)
        self.auth_label.configure(fg=TEXT_COLOR)
        self.auth_label.place(relx=0.495, rely=0.31, anchor=CENTER)

        # Блок "Имя пользователя"
        self.username_label = Label(self, text="Пользователь: ",
                                    font=("Arial Bold", 11), padx=10, pady=10)
        self.username_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.username_entry = Entry(self)
        self.username_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

        # Блок "Пароль для входа"
        self.password_label = Label(self, text="Пароль: ",
                                    font=("Arial Bold", 11), padx=10, pady=10)
        self.password_label.place(relx=0.5, rely=0.52, anchor=CENTER)
        self.password_entry = Entry(self, show="* ")
        self.password_entry.place(relx=0.5, rely=0.57, anchor=CENTER)

        # Сообщение о состоянии доступа.
        self.access_message = Label(self, font=("Arial Bold", 9), padx=10,
                                    pady=10)
        self.access_message.place(relx=0.98, rely=0.05, anchor=E)

    # AuthScreen.clear()
    # ---------------------------------------------------
    # Очистка содержимого в окне.
    # ---------------------------------------------------
    # В случае возвращения на окна аутентификации
    # из меню очищает все данные в полях/сообщениях
    # ---------------------------------------------------
    def clear(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.access_message.configure(text="")





