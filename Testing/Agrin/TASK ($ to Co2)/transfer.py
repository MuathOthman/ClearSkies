from flask import Flask
import mysql.connector
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
def money_to_co2(name):
    transfer = "2"
    sql = "update game set money = money / '" + transfer + "'"
    sql += " WHERE screen_name= '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()

    sql = "update game set co2_budget = co2_budget + money"
    sql += " WHERE screen_name= '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()

    sql = "update game set money = '0' where screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    return {"transfer": 'Transfer success'}

connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/transfer/<name>')
def transfer(name):
    response = money_to_co2(name)
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4005)