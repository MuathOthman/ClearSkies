from flask import Flask
import mysql.connector
from flask_cors import CORS


def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='Flight_game',
        user='root',
        password='kirkuk123',
        autocommit=True
    )

def newuser(user):
    sql = f"select screen_name from game where screen_name = '{user}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        return {"old": "Username already taken!"}
    else:
        return {"new": "Welcome to Clearskies!"}


connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/signup/<user>')
def signup(user):
    response = newuser(user)
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
