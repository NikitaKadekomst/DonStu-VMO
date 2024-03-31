# Утилиты и конфиги.
from utilities.constants import *
from utilities.db import *

# База данных и аутентификация.
from core.db.Database import Database
from core.auth.Auth import *

# Модуль интерфейса.
from gui.GUI import *


# Класс Main
# -----------------------------------
# Точка входа для запуска приложения
# -----------------------------------
class Main:
    def __init__(self):
        self.db = Database(DB, HOST, PORT, USER, PASSWORD)
        self.auth = Auth(self.db)

    # Запуск программы.
    def run(self):
        # Запуск окна программы.
        gui = GUI(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_BG, self.db, self.auth)
        gui.run()

        # Закрытие соединения с базой после закрытия окна.
        self.db.close()


# Входная точка в программу.
if __name__ == "__main__":
    program = Main()
    program.run()
