from tkinter import *
from gui.screens.goods.GoodsScreen import *


# Класс MenuScreen
# --------------------------------------------------------
# Базовый шаблон внутренних экранов приложения.
# Наследуется от класса Frame библиотеки Tkinter.
# --------------------------------------------------------
class MenuScreen(Frame):
    def __init__(self, parent, controller, backup_mode):
        Frame.__init__(self, parent)
        self.controller = controller

        # --Заголовок текущей страницы.
        self.user_label = Label(self,
                                text=f"Пользователь: {self.controller.auth.get_current_user_name()}",
                                font=("Arial Bold", "11"),
                                fg="black")
        self.user_label.place(relx=0.85, rely=0.05, anchor=CENTER)

        # --Кнопка возврата.
        self.canvas = Canvas(self, width=32, height=32, cursor="hand2")
        self.canvas.place(anchor=CENTER, relx=0.07, rely=0.07)
        self.img = PhotoImage(file="media/backup-arrow.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.canvas.bind("<Button-1>", lambda bcpmd: self.controller.set_backup_mode(backup_mode))

        # --Основной заголовок.
        self.heading_label = Label(self, text="Система учета товаропотока\n сортировочного центра",
                                   font=("Arial Bold", 14))
        self.heading_label.place(relx=0.5, rely=0.13, anchor=CENTER)

        # --Лейбл для сообщения пользовалю
        self.user_message = Label(self, font=("Arial Bold", 9), padx=10,
                                  pady=10)
        self.user_message.place(relx=0.98, rely=0.95, anchor=E)
