import mysql.connector
from flask import Flask
from flask_cors import CORS

def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='kirkuk123',
        autocommit=True
    )


def consumed(name):
    sql = f"select co2_consumed from game where screen_name ='{name}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        return {"consumed": result_set[0]}
    else:
        return {"Error": "Give me a correct name"}

connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/consumed/<name>')
def co2_consumed(name):
    response = consumed(name)
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4995)
