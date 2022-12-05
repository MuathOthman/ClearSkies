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

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ClearSkies',
         user='admin',
         password='12345',
         autocommit=True
         )

def api():
    api_koodi = "155ede50dd2196d8e713fcae93acae99"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    kaupunki = input("Anna kaupunki: ")
    koko_url = url + "appid=" + api_koodi + "&q=" + kaupunki
    # print(koko_url)
    print(f"{kaupunki}'s weather:")
    vastaus = requests.get(koko_url)
    if vastaus.status_code == 200:
        print(koko_url)
        vastaus_json = vastaus.json()
        for i in vastaus_json["weather"]:
            print(i["main"])
            #print(f"('{i['main']}',)")
            testi = f"'{i['main']}'"
            testi1 = f"({i['main']})"
            list.append(testi)

        return



#select id from goal where main = 'Clouds';

def id(saa):
    sql = "select id from goal "
    sql += "where main = '" + saa + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(i)
    saa_id.append(i[0])

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


def push(nimi):
    sql = "INSERT INTO `goal_reached`"
    sql += "VALUES ('" + id_find(nimi) + "', '" + str(saa_id[-1]) + "')"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/location')
def code():
    try:
        args = request.args
        nimi = args.get("nimi")
        icao = args.get("icao")
        sql = "SELECT location FROM game"
        sql += " WHERE screen_name= '" + nimi + "'"
        print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tuos = kursori.fetchall()
        for rivi in tuos:
            print(f"ICAO: {rivi[0]}")
            icao_lista.append(rivi[0])
        sql = "SELECT municipality FROM airport"
        sql += " WHERE ident= '" + icao_lista[-1] + "'"
        print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tuos = kursori.fetchall()
        for rivi in tuos:
            print(f"Municipality: {rivi[0]}")
            city_lista.append(rivi[0])
        api_koodi = "155ede50dd2196d8e713fcae93acae99"
        url = "http://api.openweathermap.org/data/2.5/weather?"
        koko_url = url + "appid=" + api_koodi + "&q=" + city_lista[-1]
        vastaus = requests.get(koko_url)
        if vastaus.status_code == 200:
            print(koko_url)
            vastaus_json = vastaus.json()
            # print(vastaus_json["weather"])
            for i in vastaus_json["weather"]:
                print(f"Description: {i['main']}")
                transferData = i['main']
                print(transferData)
        temprature = (vastaus_json['main'])
        answer = {"Description": f"{i['main']}"}
        id(transferData)
        push(nimi)
        print(answer)
        response_json = json.dumps(answer)
        list.clear()
        saa.clear()
        saa_id.clear()
        icao_lista.clear()
        city_lista.clear()
        return Response(response=response_json, status=200, mimetype="application/json")
    except ValueError:
        text = "Invalid input value, a not number"
        return Response(response=text, status=400)
    except TypeError:
        responseText = "Invalid parameter: missing?"
        return Response(response=responseText, status=400)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3078)
