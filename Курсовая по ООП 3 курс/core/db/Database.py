import pymysql
import pandas as pd


# Класс Database для работы с БД MySQL.
# Реализован на основе библиотеки pymysql.
# ------------------------------------------------
# Осуществляет подключение к серверу базы данных.
# Содержит следующий функционал для работы с
# базой данных:
# 1) выборка из указанной таблицы;
# 2) удаление из указанной таблицы;
# 3) добавление в таблицу;
# 4) создание/удаление таблиц;
# 5) парсинг DataFrame датасетов и запись их в БД.
# -------------------------------------------------
class Database:
    def __init__(self, db, host, port, user, password):
        self._connection = ""
        self._db = db
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._connection = None

        self._connect()

    # Database._connect()
    # Осуществить подключение к серверу базу данных.
    # ------------------------------------------------
    # Приватный метод, устанавливающий подключение
    # c cервером базы данных.
    # ------------------------------------------------
    def _connect(self):
        try:
            self._connection = pymysql.connect(
                host=self._host,
                port=self._port,
                user=self._user,
                database=self._db,
                password=self._password,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Connection successful!")
            print("-" * 150)
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    # Database.create_table()
    # Cоздать таблицу в БД.
    # ------------------------------------------------------------------------------------------------------
    # АРГУМЕНТЫ
    # --table_name (string) = название таблицы.
    # --database (string) = название базы данных.
    # --сolumns (dict) = информация о колонках таблицы в форме cловаря вида "название колонки: тип значения".
    # --primary_key (string) = название поля, использующееся в качестве PRIMARY KEY
    # --auto_inc (boolean) = поддерживать ли опцию авто инкремента.
    # ------------------------------------------------------------------------------------------------------
    def create_table(self, table_name, database, columns, primary_key, auto_inc=True):
        if not self.is_table_exists(table_name, database):
            query_str = f"CREATE TABLE `{table_name}` ("

            if auto_inc:
                query_str += "id int AUTO_INCREMENT, "

            for col in columns:
                query_str += f"{col} {columns[col]}, "

            query_str += f"PRIMARY KEY ({primary_key}));"

            success_message = f"Table named `{table_name}` was created successfully!"
            self.create_query(query_str, success_msg=success_message)
        else:
            return f"Table {table_name} is already exists in database {database}!"

    # Database.is_table_exists()
    # Проверить, существует ли создаваемая таблица в БД.
    # Реализован на базе Database.create_query()
    # ------------------------------------------------------
    # АРГУМЕНТЫ
    # --table_name (string) = название таблицы.
    # --database (string) = название базы данных.
    # ---------------------------------------------------------
    def is_table_exists(self, table_name, database):
        resp = self.create_query(f"SHOW TABLES FROM {database} LIKE '{table_name}';", return_mode=True)
        return True if resp else False

    # Database.select_from_table()
    # Выбрать определенные строки из таблицы.
    # -----------------------------------------------------------------------------
    # АРГУМЕНТЫ
    # --table_name (string) = название таблицы
    # --star (boolean) = получать ли всю информацию из таблицы (SELECT * FROM)
    # --columns (list) = если star=False, список конкретных колонок для выборки.
    # -----------------------------------------------------------------------------
    # ВОЗВРАЩАЕМЫЙ ТИП: список словарей вида "колонка: значение в колонке, ..."
    # -----------------------------------------------------------------------------
    def select_from_table(self, table_name, star=True, columns=None, where_cond=""):
        try:
            with self._connection.cursor() as cursor:
                if star and where_cond == "":
                    query_str = f"SELECT * FROM {table_name}"
                    cursor.execute(query_str)
                    print("Data is fetched successfully")
                    print("SQL request:", query_str)
                    return cursor.fetchall()
                elif star and where_cond != "":
                    query_str = f"SELECT * FROM {table_name} WHERE {where_cond}"
                    cursor.execute(query_str)
                    print("Data is fetched successfully")
                    print("SQL request:", query_str)
                    return cursor.fetchall()
                else:
                    if type(columns) == list:
                        query_str = "SELECT "
                        for col_i in range(len(columns)):
                            if col_i < len(columns) - 1:
                                query_str += f"{columns[col_i]}, "
                            else:
                                query_str += f"{columns[col_i]} "
                        query_str += f"FROM {table_name}"

                        if where_cond != "":
                            query_str += f" WHERE {where_cond};"
                        else:
                            query_str += ";"

                        data = f"Data from table: {table_name}, columns: {columns}"
                        if where_cond:
                            data += f", where: {where_cond} is fetched successfully"

                        cursor.execute(query_str)
                        print("SQL request:", query_str)
                        print("-" * 150)
                        return cursor.fetchall()
                    else:
                        raise ValueError("db.select_from_table(): переданный параметр columns не является списком!")
        except Exception as ex:
            print("Error during fetching...")
            print(ex)
            print("-" * 150)

    # Database.delete_single_row_from_table()
    # Удаление из определенной таблицы единственной записи.
    # Реализован на базе Database.create_query()
    # ------------------------------------------------------------
    # АРГУМЕНТЫ
    # --table_name (string) = название таблицы
    # --сolumn (string) = по какой колонке удалять строку.
    # --сolumn_val (string) = по какому значению в колонке сolumn
    # удалять строку.
    # ------------------------------------------------------------
    def delete_single_row_from_table(self, table_name, column, column_val):
        delete_success = f"Value {column_val} in column `{column}` from table {table_name} was successfully deleted!"
        delete_failure = f"Value {column_val} in column `{column}` from table {table_name} cannot be deleted!"

        self.create_query(f"DELETE FROM {table_name} WHERE {column}='{column_val}'",
                          success_msg=delete_success,
                          error_msg=delete_failure)

    # Database.insert_single_row_into_table()
    # Вставка в определенную таблицу единственной записи.
    # --------------------------------------------------------------------
    # АРГУМЕНТЫ
    # --table_name = название таблицы
    # --сolumns = список названий колонок в виде списка.
    # --values = список значений для вставки в колонки в виде списка.
    # --------------------------------------------------------------------
    def insert_single_row_into_table(self, table_name, columns, values):
        try:
            with self._connection.cursor() as cursor:
                query_str = f"INSERT INTO `{table_name}` ("

                # Вставка названий колонок.
                for col_i in range(len(columns)):
                    if col_i != len(columns) - 1:
                        query_str += f"{columns[col_i]}, "
                    else:
                        query_str += f"{columns[col_i]})"

                query_str += " VALUES ("

                # Вставка значений в каждой колонке.
                for val_i in range(len(values)):
                    if val_i != len(values) - 1:
                        query_str += f'"{values[val_i]}", '
                    else:
                        query_str += f'"{values[val_i]}");'

                cursor.execute(query_str)
                self._connection.commit()
                print(f"Values {values} were successfully added into {table_name}'s columns {columns}!")
                print("-" * 150)
        except Exception as ex:
            print(f"Error during insertion...")
            return ex

    # Database.insert_rows_into_table()
    # Вставка в указанную таблицу нескольких записей.
    # Реализован на базе Database.insert_single_row_into_table()
    # ---------------------------------------------------------------------
    # АРГУМЕНТЫ
    # --table_name (string) = название таблицы
    # --insertion_info (dict) = информация о вставке в форме словаря вида
    # "колонка: cписок значений для вставки"
    # ----------------------------------------------------------------------
    def insert_rows_into_table(self, table_name, insertion_info):
        # Получаем список колонок таблицы.
        columns = [col for col in insertion_info]

        # Получаем максимальное количество значений для вставки в колонку.
        max_index = max([len(insertion_info[col]) for col in insertion_info])

        # Построчно вставляем данные в таблицу.
        for col_i in range(max_index):
            values = []
            for col in insertion_info:
                # Отмечаем пустые ячейки без переданных значений как "-".
                if col_i > len(insertion_info[col]) - 1:
                    values.append("-")
                else:
                    values.append(insertion_info[col][col_i])
            self.insert_single_row_into_table(table_name, columns=columns, values=values)

    # Database.update_row()
    # Обновление указанной строки в таблице.
    # Реализован на базе Database.create_query()
    # ----------------------------------------------------------------------------------
    # АРГУМЕНТЫ
    # --table_name (string) = название таблицы.
    # --columns_to_set (dict) = словарь с данными для обновления вида
    #                                           "колонка: новое значение"
    #                                           "колонка: cписок значений для вставки".
    # --where_cond (string) = условие WHERE SQL-запроса.
    # ----------------------------------------------------------------------------------
    def update_row(self, table_name, columns_to_set, where_cond=""):
        query_str = f"UPDATE {table_name} SET "

        index = 0
        key_index = len(columns_to_set.keys()) - 1

        for col in columns_to_set:
            if index < key_index:
                query_str += f"{col}='{columns_to_set[col]}', "
                index = index + 1
            else:
                query_str += f"{col}='{columns_to_set[col]}'"

        if where_cond != "":
            query_str += f" WHERE {where_cond};"

        success_msg = f"Rows {columns_to_set} in table {table_name}, {where_cond} updated successfully!"

        self.create_query(query_str, success_msg=success_msg)

    # Database.create_query()
    # Создание общего SQL-запроса.
    # ----------------------------------------------------------
    # АРГУМЕНТЫ
    # --query (string) = текст SQL запроса.
    # --return_mode (bool) = должен ли запрос записать
    # в базу данные или же вернуть ответ пользователю.
    # --commit (bool) = настройка коммита для запроса.
    # --success_msg (string) = текст ответа при удачном запросе.
    # --error_msg (string) = текст ответа при неудачном запросе.
    # ----------------------------------------------------------
    def create_query(self, query, return_mode=False, commit=True, success_msg="Query was executed successfully!",
                     error_msg="Query was NOT "
                               "successfull..."):
        try:
            with self._connection.cursor() as cursor:
                if return_mode:
                    cursor.execute(query)
                    return cursor.fetchall()
                cursor.execute(query)
                if commit:
                    self._connection.commit()
                print(success_msg)
                print("-" * 150)
        except Exception as ex:
            print(error_msg)
            print(query)
            print("-" * 150)
            return ex

    # Database.close()
    # Закрытие соединения
    # ---------------------------------------------
    # В случае закрытия окна программы выполнить
    # закрытие текущего cоединения с БД.
    # ---------------------------------------------
    def close(self):
        try:
            self._connection.close()
            print("Connection closed!")
            print("-" * 150)
        except Exception as ex:
            print(ex)

    # Database.insert_dataset_into_table()
    # Cпарсить и записать датасет в указанную таблицу.
    # ----------------------------------------------------------------
    # АРГУМЕНТЫ
    # --init_dataset = датасет для парсинга
    # --file_type = тип файла датасета (поддерживаются .csv и .xlsx)
    # --table_name = таблицы для записи данных.
    # --dataset = Pandas DataFrame датасет.
    # ----------------------------------------------------------------
    def insert_dataset_into_table(self, init_dataset, file_type, usecols, table_name):
        dataset = ""
        try:
            if file_type == "xlsx":
                dataset = pd.read_excel(init_dataset, usecols=usecols)
            elif file_type == "csv":
                dataset = pd.read_csv(init_dataset, usecols=usecols)
            else:
                raise ValueError("Ошибка аргумента! Введен неподдерживаемый тип файла для парсинга датасета!")
        except Exception as ex:
            print(ex)

        # Создание таблицы
        dataset_columns = list(dataset.columns)
        columns = {}

        for column in dataset_columns:
            columns[column] = "longtext"

        self.create_table(table_name, self._db, columns, "id")

        # Очистка и запись данных в таблицу.
        values = {}
        for column in dataset_columns:
            col_values = dataset[column].tolist()
            cleared_col_values = []

            for val in col_values:
                if str(val) == "nan":
                    val = "-"
                val = str(val)
                val.replace("'", "\"")
                cleared_col_values.append(val)

            values[column] = cleared_col_values

        self.insert_rows_into_table(table_name, values)

    # -------------
    #   ГЕТТЕРЫ
    # -------------

    def get_host(self):
        return self._host

    def get_port(self):
        return self._port

    def get_user(self):
        return self._user
