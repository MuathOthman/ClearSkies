import mysql.connector
from flask import Flask
from flask_cors import CORS

def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='ClearSkies',
        user='admin',
        password='12345',
        autocommit=True
    )


def budget(name):
    sql = f"select co2_consumed, co2_budget from game where screen_name ='{name}'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        return i

def first(name):
    laskuri = budget(name) - 50
    print(laskuri)
    sql = f"select co2_consumed, co2_budget from game where screen_name ='{name}'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        return i

connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/co2_budget/<name>')
def co2budget(name):
    response = budget(name)
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3099)
