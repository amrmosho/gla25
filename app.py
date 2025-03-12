
from flask import Flask
import mysql.connector


app = Flask(__name__)


def db_test():

    try:
        


        host = "localhost"
        user = "gla_user"
        password = "Gla-insya$2025"
        name = "galla_db"
        
        
        host = "localhost"
        user = "root"
        password = ""
        name = "py_insya_2"        

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=name,
        )
        cursor = connection.cursor()
        cursor.execute("select * from kit_menu")


        row_headers = [x[0] for x in cursor.description]

        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))

        cursor.close()
        connection.close()
        del connection
        return json_data

    except mysql.connector.Error as err:

        return err.msg



@app.route('/')
def hello_world():
    return ">>>>>" + db_test()


if __name__ == "__main__":
    app.run()
