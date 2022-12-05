import mysql.connector
from flask_cors import CORS
import requests
from flask import Flask, request, Response
import json



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


def newuser(nimi, location):
    sql = "select screen_name from game"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if (nimi,) in tulos:
        print("Käyttäjänimi on jo olemassa. Kirjaudu sisään painamalla 2.")
    else:
        sql = "INSERT INTO game (id, co2_consumed, co2_budget, location, screen_name, money)  "
        sql += "VALUES ('" + id_funktio + "', '0', '0', '" + location + "', '" + nimi + "', '0')"
        kursori = connection.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        print(sql)
        budjetti(nimi)
    return


def id():
    testi = []
    sql = "select id from game;"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            moi = rivi[0] + 1
        # print(moi)
        testi.append(str(moi))
        # print(testi)
        for i in testi:
            # print(i)
            return i


def budjetti(nimi):
    import random
    random_budjetti = random.randint(3917, 7834)
    random_budjetti1 = str(random_budjetti)
    sql = "UPDATE game set co2_budget= '" + random_budjetti1 + "'"
    sql += "Where screen_name = '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return


id_funktio = id()

@app.route('/signup')
def signup():
    args = request.args
    nimi = args.get("nimi")
    icao = args.get("icao")
    print(nimi)
    print(icao)
    newuser(nimi, icao)
    json_function = {'nimi': nimi, 'icao': icao}
    respone_json = json.dumps(json_function)
    return respone_json

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4320)

