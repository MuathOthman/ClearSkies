from flask import Flask, request, Response
import json
import mysql.connector
import requests
from flask_cors import CORS



yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='Flight_game',
         user='khaleel673',
         password='muath2003',
         autocommit=True
         )

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/kentta/')
def code():
    try:
        sql = "select location from game "
        sql += "Where screen_name = 'Muath'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        for rivi in tulos:
            print(rivi[0])
            answer = {"Location": f"{rivi[0]}"}
        response_json = json.dumps(answer)
        return Response(response=response_json, status=200, mimetype="application/json")
    except ValueError:
        text = "Invalid input value, a not number"
        return Response(response=text, status=400)
    except TypeError:
        responseText = "Invalid parameter: missing?"
        return Response(response=responseText, status=400)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4000)


