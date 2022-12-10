from flask import Flask, Response, request
import mysql.connector
from flask_cors import CORS
import requests
import json
from flask_cors import CORS
lista = []
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ClearSkies',
         user='admin',
         password='12345',
         autocommit=True
         )

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def laskuri(nimi):
    sql = "SELECT latitude_deg, longitude_deg FROM airport, game"
    sql += " where location = ident and screen_name = '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    location1 = lista[0]
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident= '" + location1 + "'"
    kursori1 = yhteys.cursor()
    kursori1.execute(sql)
    tulos1 = kursori1.fetchall()

    sql = "UPDATE game set location= '" + location1 + "'"
    sql += "Where screen_name = '" + nimi + "'"
    kursori2 = yhteys.cursor()
    kursori2.execute(sql)
    tulos2 = kursori2.fetchall()

    from geopy.distance import geodesic
    newport_ri = tulos[0]
    cleveland_oh = tulos1[0]
    etaisuus = geodesic(newport_ri, cleveland_oh).kilometers
    paasot = (etaisuus * 102) / 1000
    return str(int(paasot))


def co2_lisaaminen(nimi):
    sql = "update game set co2_consumed = co2_consumed + '" + laskuri(nimi) + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return
@app.route('/location')
def code():
    try:
        args = request.args
        nimi = args.get("nimi")
        icao = args.get("icao")
        sql = "select ident from airport where scheduled_service =  'yes';"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if (icao.upper(),) not in tulos:
            print("Komento ei suoritettu!")
        else:
            lista.append(icao)
        co2_lisaaminen(nimi)
        laskuri(nimi)
        sql = "SELECT latitude_deg, longitude_deg FROM airport"
        sql += " where ident = '" + icao + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        for i in tulos:
            answer = {"Latitude": + i[0], "Longitude": + i[1]}
            print(answer)
            lista.clear()
            response_json = json.dumps(answer)
            return Response(response=response_json, status=200, mimetype="application/json")
    except ValueError:
        text = "Invalid input value, a not number"
        return Response(response=text, status=400)
    except TypeError:
        responseText = "Invalid parameter: missing?"
        return Response(response=responseText, status=400)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3070)



#SQL