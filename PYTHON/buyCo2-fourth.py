from flask import Flask, Response, request
import mysql.connector
from flask_cors import CORS
import requests
import json
from flask_cors import CORS


def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='ClearSkies',
        user='admin',
        password='12345',
        autocommit=True
    )

def first(nimi):
    sql = "update game set money = money - '" + "50" + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    sql1 = "update game set co2_budget = co2_budget + '" + "25" + "'"
    sql1 += " WHERE screen_name= '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    kursori1 = connection.cursor()
    kursori1.execute(sql1)
    answer = {"Data": 'viety'}
    print(answer)
    response_json = json.dumps(answer)
    return Response(response=response_json, status=200, mimetype="application/json")

def first(nimi):
    sql = "update game set money = money - '" + "50" + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    sql1 = "update game set co2_budget = co2_budget + '" + "25" + "'"
    sql1 += " WHERE screen_name= '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    kursori1 = connection.cursor()
    kursori1.execute(sql1)
    answer = {"Data": 'viety'}
    print(answer)
    response_json = json.dumps(answer)
    return Response(response=response_json, status=200, mimetype="application/json")

def first(nimi):
    sql = "update game set money = money - '" + "200" + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    sql1 = "update game set co2_budget = co2_budget + '" + "100" + "'"
    sql1 += " WHERE screen_name= '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    kursori1 = connection.cursor()
    kursori1.execute(sql1)
    answer = {"Data": 'viety'}
    print(answer)
    response_json = json.dumps(answer)
    return Response(response=response_json, status=200, mimetype="application/json")

connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/co2_budget/<name>')
def co2budget(name):
    response = first(name)
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4049)
