from flask import Flask
import mysql.connector
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

connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/sql/<name>')
def money(name):
    def id_find(name):
        testi = []
        sql = "select id from game "
        sql += "Where screen_name = '" + name + "'"
        # print(sql)
        kursori = connection.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            for rivi in tulos:
                testi.append(str(rivi[0]))

        return str(rivi[0])

    sql = "UPDATE game SET co2_consumed = '0', co2_budget= '2000', location = 'efhk', money= '0'"
    sql += " WHERE screen_name= '" + name + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    sql1 = "DELETE FROM goal_reached WHERE game_id = '" + id_find(name) + "'"
    kursori = connection.cursor()
    kursori.execute(sql1)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3033)

#SQL
