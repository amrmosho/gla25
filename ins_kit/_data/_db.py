from flask import abort
import mysql.connector
from ins_kit.ins_parent import ins_parent


class Database(ins_parent):
    def _table(self, name):
        if len(self.ins._eng._kit_settings) > 0 and name in self.ins._eng._kit_settings["db"]:
            return self.ins._eng._kit_settings["db"][name]
        else:
            return name

    def _jar(self, operation):

        r = {}
        jar = self.ins._this._settings["jar"]

        ops = []
        for k in jar:
            if jar[k]["operation"] == operation:
                ops.append(jar[k])

        for op in ops:
            if op["info"] == "now":
                r[op["target"]] = self.ins._date._now()

        return r

    """
    A class for interacting with a MySQL database, providing methods for connection, data manipulation, table management, and console output.
    """

    def _connect(self):
        """
        Establishes a connection to the MySQL database.
        """
        try:
            set = self.ins._eng._app_settings("db")["main"]

            self.connection = mysql.connector.connect(
                host=set["host"],
                user=set["user"],
                password=set["password"],
                database=set["name"],
            )
            self.cursor = self.connection.cursor()
            self._console_print("Connected to MySQL database successfully")
        except mysql.connector.Error as err:
            self.ins._console.error("db", "db_connection_failed", err.msg)

    def __db_open(self):
        if not hasattr(self, "connection") or not self.connection or not self.connection.is_connected:
            self._connect()
            self.open_status = True
        return self.open_status

    def __db_close(self):
        if self.open_status:
            self._close()
            self.open_status = False
        return self.open_status

    def _close(self):
        """
        Closes the database connection and cursor.
        """
        if self.connection:
            self.cursor.close()
            self.connection.close()
            del self.connection
            self._console_print("MySQL connection closed")

    query = ""
    open_status = False
    __get_deleted = False
    __get_disabled = False

    def _get_deleted(self):
        self.__get_deleted = True
        return self

    def _get_disabled(self):
        self.__get_disabled = True
        return self

    def _jget(self, table="", custom="*", where="1=1"):

        self.j_query = ""
        self.j_tquery = table

        if not self.__get_deleted:
            where = f"   {table}.kit_deleted<>1  and  {where} "

        if not self.__get_disabled:
            where = f"   {table}.kit_disabled<>1 and {where}  "
        sp = ""
        if "." not in custom:
            cs = custom.split(",")
            custom = ""
            for c in cs:
                custom += f"{sp} {table}.{c}"
                sp = ","

        self.j_cquery = custom
        self.j_wquery = f" Where {where}"
        return self

    def _jwith(self, table="", custom="*", _on="1=1", fk="", rfk="", join="join"):

        table = table.strip()
        tables = table.split(" ")
        table_name = table
        if len(tables) > 1:
            table_name = tables[1]

        if fk != "":
            _on = f"{table_name}.{fk} = {self.j_tquery}.id"

        if rfk != "":
            _on = f"{table_name}.id = {self.j_tquery}.{rfk}"

        self.j_query += f' {join} {table} on {_on} '
        sp = ","
        if "." not in custom:
            cs = custom.split(",")
            custom = ""
            for c in cs:
                custom += f"{sp} {table_name}.{c} as  {table_name}_{c}"

        self.j_cquery += custom
        return self

    def _jsql(self):
        sql = f"SELECT {self.j_cquery} From {
            self.j_tquery}  {self.j_query} {self.j_wquery} "
        return self._get_query(sql)

    def _jrun(self):
        sql = f"SELECT {self.j_cquery} From {
            self.j_tquery}  {self.j_query} {self.j_wquery} "
        return self._get_query(sql)

    def _get_query(self, query, return_error=False):

        if not hasattr(self, "connection") or not self.connection or not self.connection.is_connected:
            self._connect()
            self.open_status = True
            """self._console_print("No connection established")
            return None"""
        self.query = query
        try:
            self.cursor.execute(self.query)

            if self.cursor._rowcount == -1:
                return "done"
            # this will extract row headers
            row_headers = [x[0] for x in self.cursor.description]

            rv = self.cursor.fetchall()
            if self.open_status:
                self._close()
                self.open_status = False
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers, result)))
            return json_data

        except mysql.connector.Error as err:

            if return_error:
                return f"Error executing query: {err}"
            if self.open_status:
                self._close()
                self.open_status = False

            self.ins._console.error("db", "db_query_failed", err.msg)

            return False

    def _get_data(self, table="", custom="*", where="1=1" ,update_lang=False):

        table = self._table(table)

        if not self.__get_deleted:
            where = f"   {table}.kit_deleted<>1  and  {where} "

        if not self.__get_disabled:
            where = f"   {table}.kit_disabled<>1 and {where}  "

            self.__get_deleted = False
            self.__get_disabled = False

        self.query = f"SELECT {custom} FROM {table} where  {where}"
        rs= self._get_query(self.query)
        if update_lang:
            for r in rs:
                r = self.update_lang(r)
        return rs

    def update_lang(self, r):
        ln =self.ins._langs._this_get(True)
        if "kit_lang" in r and r["kit_lang"] !="" :
            lss = self.ins._json._decode(r["kit_lang"])
            if ln in lss:
                ls = lss[ln]
                for k, v in r.items():
                    if k in ls.keys():
                        r[k] = ls[k]
        return r

    def _get_row(self, table="", custom="*", where="1=1", update_lang=False):

        try:

            rs = self._get_data(table, custom, where ,update_lang)

            if rs == False or len(rs) == 0:
                return False
            r = rs[0]

     
            return r

        except IndexError as err:
            return self.ins._console.error("db", "db_record_not_found", self.query)

    def _update_filds(self, table_name, data: dict) -> dict:
        fs = self._get_table_fields(table_name)
        tmp = {}
        tmp.update(data)
        for k in data:
            if k not in fs:
                tmp.pop(k)
        return tmp

    def _insert(self, table_name, data: dict):
        """
        Inserts data into the specified table, removing missing values.

        Args:
            table_name (str): The name of the table.
            data (dict): The data to be inserted.
        """

        jar = self._jar("insert")
        if len(jar) > 0:
            data.update(jar)

        data = self._update_filds(table_name, data)
        self.__db_open()
        # Filter out None values
        if "id" in data:
            del data["id"]
        filtered_data = {key: value for key,
                         value in data.items() if value is not None}

        columns = ', '.join(filtered_data.keys())
        values = ', '.join(['%s'] * len(filtered_data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        try:
            self.cursor.execute(query, tuple(filtered_data.values()))
            self.connection.commit()

        # Retrieve the ID of the inserted row using cursor.lastrowid
            inserted_id = self.cursor.lastrowid
            self._console_print(f"Data inserted into {
                                table_name} successfully")
            self.__db_close()
            return inserted_id
        except mysql.connector.Error as err:
            self.__db_close()
            self.ins._console.error("db", "db_query_failed", err.msg)

    def _update(self, table_name, data: dict, condition):
        """
        Updates data in the specified table based on the given condition, removing missing values.

        Args:
            table_name (str): The name of the table.
            data (dict): The data to be updated.
            condition (str): The condition for updating the data.
        """
        jar = self._jar("update")
        if len(jar) > 0:
            data.update(jar)

        data = self._update_filds(table_name, data)
        if "id" in data:
            data.pop("id")
        self.__db_open()

        # Filter out None values
        filtered_data = {key: value for key,
                         value in data.items() if value is not None}

        set_values = ', '.join([f"{key} = %s" for key in filtered_data])
        query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"

        try:
            self.cursor.execute(query, tuple(filtered_data.values()))
            self.connection.commit()
            self._console_print(f"Data updated in {table_name} successfully")
            self.__db_close()

        except mysql.connector.Error as err:
            self.ins._console.error("db", "db_query_failed", err.msg)
            self.__db_close()

    def _delete(self, table_name, condition):
        """
        Deletes data from the specified table based on the given condition.

        Args:
            table_name (str): The name of the table.
            condition (str): The condition for deleting the data.
        """
        self.__db_open()

        query = f"DELETE FROM {table_name} WHERE {condition}"

        try:
            self.cursor.execute(query)
            self.connection.commit()
            self._console_print(f"Data deleted from {table_name} successfully")
            self.__db_close()

        except mysql.connector.Error as err:
            self.ins._console.error("db", "db_query_failed", err.msg)
            self.__db_close()

    def _set_query(self, query):
        """
        Creates a new table in the database.

        Args:
            table_name (str): The name of the table to create.
            columns (list): A list of column definitions as tuples (column_name, data_type).
        """
        self.__db_open()

        try:
            r = self.cursor.execute(query)
            self.__db_close()
            return r

        except mysql.connector.Error as err:
            self.ins._console.error("db", "db_query_failed", err.msg)

            self.__db_close()

    def _create_table(self, table_name, columns):
        """
        Creates a new table in the database.

        Args:
            table_name (str): The name of the table to create.
            columns (list): A list of column definitions as tuples (column_name, data_type).
        """
        if not self.connection:
            self._console_print("No connection established")
            return

        columns_str = ', '.join(
            [f"{column[0]} {column[1]}" for column in columns])
        query = f"CREATE TABLE {table_name} ({columns_str})"

        try:
            self.cursor.execute(query)
            self._console_print(f"Table {table_name} created successfully")
        except mysql.connector.Error as err:
            self.ins._console.error("db", "db_query_failed", err.msg)

    def _get_table_fields(self, table_name):
        """
        Retrieves the column names of a table.

        Args:
            table_name (str): The name of the table.

        Returns:
            list: A list of column names.
        """
        self.__db_open()
        query = f"DESCRIBE {table_name}"

        try:
            self.cursor.execute(query)
            fields = [row[0] for row in self.cursor.fetchall()]
            self.__db_close()
            return fields

        except mysql.connector.Error as err:
            self.__db_close()
            self.ins._console.error("db", "db_query_failed", err.msg)

            return None

    def _console_print(self, message):
        """
        Prints a message to the console.

        Args:
            message (str): The message to print.
        """
        self.ins._tmp._con(message)

    def _errr_print(self, message):
        """
        Prints a message to the console.

        Args:
            message (str): The message to print.
        """
        return self.ins._tmp._con(message)

    @staticmethod
    def _where_from_group(value, field="cat_id"):
        return f"( {field} like '%,{value}' or {field} like '{value},%' or {field} like '%,{value},%' or {field} = '{value}')"

    @staticmethod
    def _where_between_two_dates(from_date, to_date, field="date"):

        from_date = ""  # \ins::_timedate()->_date($from_date); //date($format, strtotime($from_date));
        to_date = ""  # \ins::_timedate()->_date($to_date);

        return f" ( `{field}` BETWEEN '{from_date}' AND  '{to_date}') "

    @staticmethod
    def _where_by_array(array, more="or", field="id"):
        r = ""
        m = ""
        if array is not list:
            array = array.split(",")

        for a in array:
            r += f" {m} {field}='{a}' "
            m = more

        if r == "":
            r = "1<>1"

        r = f"({r})"
        return r
