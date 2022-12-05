from flask import Flask, Response
import mysql.connector
from flask_cors import CORS
lista = []
icao_lista = []
city_lista = []
import requests
import json
from flask_cors import CORS

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
@app.route('/saa/<name>')
def code(name):
    try:
            sql = "SELECT location FROM game"
            sql += " WHERE screen_name= '" + name + "'"
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
            temprature = (vastaus_json['main']['temp'] - 273.15)
            print(f"Temprature: {int(temprature)} °C")
            answer = {"Description": f"{i['main']}", "Temperature": f"{round(vastaus_json['main']['temp'] - 273.15)}"}
            print(answer)
            response_json = json.dumps(answer)
            return Response(response=response_json, status=200, mimetype="application/json")
    except ValueError:
        text = "Invalid input value, a not number"
        return Response(response=text, status=400)
    except TypeError:
        responseText = "Invalid parameter: missing?"
        return Response(response=responseText, status=400)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3040)



#RUN


