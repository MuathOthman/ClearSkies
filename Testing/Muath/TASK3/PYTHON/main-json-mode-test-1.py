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
         database='lentopeli',
         user='testi',
         password='12345',
         autocommit=True
         )

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/saa/<name>')
def code(name):
    try:
        sql = "SELECT latitude_deg, longitude_deg FROM airport, game"
        sql += " where location = ident and screen_name = '" + name + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        for i in tulos:
            print(i)
            answer = {"Latitude": f"{i[0]}", "Longitude": f"{i[1]}"}
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
    app.run(use_reloader=True, host='127.0.0.1', port=3050)



#RUN