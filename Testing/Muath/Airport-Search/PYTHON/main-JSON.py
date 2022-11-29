from flask import Flask, request, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='lentopeli',
    user='testi',
    password='12345',
    autocommit=True
)

lista_kentta = []
lista_icao = []
samples = []


app = Flask(__name__)
@app.route('/kentta/<nimi>')
def kentta(nimi):
    try:
        sql = "select airport.name, airport.ident from country inner join airport "
        sql += " on airport.iso_country = country.iso_country where country.name = '" + nimi + "' and scheduled_service = 'yes'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            for i in tulos:
                print(i[-1])
                print(i[-2])
                airport_json = {"name": None, "icao": None}
                airport_json["name"] = i[-2]
                airport_json["icao"] = i[-1]
                samples.append(airport_json)
        response_json = json.dumps(samples)
        return Response(response=response_json, status=200, mimetype="application/json")
    except ValueError:
        text = "Invalid input value, a not number"
        return Response(response=text, status=400)
    except TypeError:
        responseText = "Invalid parameter: missing?"
        return Response(response=responseText, status=400)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
