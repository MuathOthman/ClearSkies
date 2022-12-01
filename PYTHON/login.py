from flask import Flask
import mysql.connector
from flask_cors import CORS


def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='lentopeli',
        user='testi',
        password='12345',
        autocommit=True
    )


def olduser(name):
    sql = f"select screen_name from game where screen_name= '{name}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        return {"correct": result_set[0]}
    else:
        return {"Error": "Give me a correct name"}


connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/login/<name>')
def login(name):
    response = olduser(name)
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3010)
