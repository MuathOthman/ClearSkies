from flask import Flask, Response, request
import mysql.connector
from flask_cors import CORS
import requests
import json
from flask_cors import CORS

list = []
saa = []
saa_id = []
icao_lista = []
city_lista = []
samples = []

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ClearSkies',
         user='admin',
         password='12345',
         autocommit=True
         )

def id_find(nimi):
    testi = []
    sql = "select id from game "
    sql += "Where screen_name = '" + nimi + "'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            testi.append(str(rivi[0]))

    return str(rivi[0])

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/saa/<name>')
def code(name):
    try:
        sql = "select goal_id from goal_reached"
        sql += " where game_id = '" + id_find(name) + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            for i in tulos:
                saa_json = {"saa": i[0]}
                print(i[0])
                response_json = json.dumps(saa_json)
            return Response(response=response_json, status=200, mimetype="application/json")
    except ValueError:
        text = "Invalid input value, a not number"
        return Response(response=text, status=400)
    except TypeError:
        responseText = "Invalid parameter: missing?"
        return Response(response=responseText, status=400)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3678)
