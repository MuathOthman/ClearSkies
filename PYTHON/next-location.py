from flask import Flask, Response
import mysql.connector
from flask_cors import CORS
import requests
import json
from flask_cors import CORS

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='',
         autocommit=True
         )

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/location/<name>')
def code(name):
    try:
        sql = "SELECT latitude_deg, longitude_deg FROM airport"
        sql += " where ident = '" + name + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        for i in tulos:
            print(i)
            print(i[0])
            answer = {"Latitude": + i[0], "Longitude": + i[1]}
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
    app.run(use_reloader=True, host='127.0.0.1', port=3070)



#RUN