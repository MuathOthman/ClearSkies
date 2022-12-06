from flask import Flask, request, Response
import json
import mysql.connector
from flask_cors import CORS


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='ClearSkies',
    user='admin',
    password='12345',
    autocommit=True
)

lista_kentta = []
lista_icao = []
samples = []


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/leaderboard/')
def leaderboard():
    try:
        sql = "select screen_name, count(*), co2_consumed from game, goal_reached where id = game_id group by co2_consumed ASC having (count(*)=7)"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            for i in tulos:
                print(i[-1])
                print(i[-2])
                print([-3])
                airport_json = {"name": None, "coconsumed": None, "weathercard": None}
                airport_json["name"] = i[-3]
                airport_json["coconsumed"] = i[-1]
                airport_json["weathercard"] = i[-2]
                samples.append(airport_json)
        response_json = json.dumps(samples)
        samples.clear()
        return Response(response=response_json, status=200, mimetype="application/json")
    except ValueError:
        text = "Invalid input value, a not number"
        return Response(response=text, status=400)
    except TypeError:
        responseText = "Invalid parameter: missing?"
        return Response(response=responseText, status=400)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3090)

#SQL
