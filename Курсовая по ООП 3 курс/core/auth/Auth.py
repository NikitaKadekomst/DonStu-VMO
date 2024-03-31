import bcrypt
from utilities.db import *


# Класс Auth модуля аутентификации.
# ---------------------------------------------
# Реализует функционал авторизации в системе
# через SQL-запросы к БД MySQL.
# ---------------------------------------------
class Auth:
    def __init__(self, db):
        self.db = db
        self._create_users_table()

    # ВНУТРЕННИЙ МЕТОД.
    # Создание таблицы для хранения данных юзеров.
    def _create_users_table(self):
        table_name = "users"
        columns = {
            "username": "varchar(32)",
            "password": "char(64)",
            "currentUser": "varchar(32)"
        }
        database = DB
        self.db.create_table(table_name, database, columns, "id")

    # Auth.register_new_user()
    # -------------------------------------------
    # Регистрация прав для нового юзера.
    # -------------------------------------------
    # АРГУМЕНТЫ
    # --user == имя пользователя
    # --password = пароль
    # --------------------------------------------
    # ВОЗВРАЩАЕМЫЙ ТИП
    # string, если юзер существует
    # --------------------------------------------
    def register_new_user(self, user, password):
        response = self.db.select_from_table("users", False, ["username"])

        # Если такой юзер уже существует, выходим из метода c cоответствующим логом.
        for resp_user in response:
            if resp_user["username"] == user:
                print(f"login.create_new_user(): user `{user}` is already exists!")
                print("-" * 50)
                return f"Пользователь с ником {user} уже существует!"

        # Хэширование пароля перед записью.
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        pw_to_store = hashed.decode("utf-8")

        # Запись пользователя в базу.
        self.db.insert_single_row_into_table("users", ["username", "password", "currentUser"], [user, pw_to_store, "-"])

    # Auth.delete_user()
    # ----------------------------------------------
    # Удаление информации об указанном пользователе
    # ----------------------------------------------
    # АРГУМЕНТЫ
    # --username == имя пользователя
    # ----------------------------------------------
    # ВОЗВРАЩАЕМЫЙ ТИП
    # void, если юзер существует
    # ----------------------------------------------
    def delete_user(self, username):
        self.db.delete_single_row_from_table("users", "username", username)

    # Auth.verify_access()
    # ----------------------------------------------
    # Проверка на возможность доступа.
    # ----------------------------------------------
    # АРГУМЕНТЫ
    # --user == имя пользователя
    # --password = пароль
    # --------------------------------------------
    def verify_access(self, user, password):
        response = self.db.select_from_table("users", False, ["username", "password"])

        if not response:
            return "Не найдены права для пользователей!"

        for resp_user in response:
            username = resp_user["username"]
            password_hash = resp_user["password"]

            if username == user and bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8")):
                self.change_current_user(user)
                return "Доступ разрешён!"
            elif resp_user["username"] == user and not bcrypt.checkpw(password.encode("utf-8"),
                                                                      password_hash.encode("utf-8")):
                return "Неверный пароль!"

        return f"Пользователь с ником \"{user}\" не найден!"

    # Auth.change_current_user()
    # -------------------------------------------
    # Обновляет в БД информацию о текущем юзере,
    # вошедшем в систему.
    # -------------------------------------------
    # АРГУМЕНТЫ
    # --username = имя нового текущего
    # пользователя системы
    # -------------------------------------------
    def change_current_user(self, username):

        # Очистить поле currentUser у всех записей в таблице.
        self.db.update_row("users", {"currentUser": "-"}, "currentUser='YES'")

        # Отметить поле currentUser=YES у записи с соответствующим username.
        self.db.update_row("users", {"currentUser": "YES"}, f"username='{username}'")

    # Auth.get_current_user_name()
    # -----------------------------------------------
    # Возвращает имя текущего пользователя в системе
    # -----------------------------------------------
    # ВОЗВРАЩАЕМЫЙ ТИП
    # string с именем текущего пользователя.
    # -----------------------------------------------
    def get_current_user_name(self):
        db_resp = self.db.select_from_table("users", False, ["username"], "currentUser='YES'")
        if db_resp:
            return db_resp[0]["username"]
        else:
            print("Ошибка при получении имени текущего пользователя")
            print(db_resp)
            return
