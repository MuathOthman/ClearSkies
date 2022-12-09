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
    return response_json

def second(nimi):
    sql = "update game set money = money - '" + "100" + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    sql1 = "update game set co2_budget = co2_budget + '" + "50" + "'"
    sql1 += " WHERE screen_name= '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    kursori1 = connection.cursor()
    kursori1.execute(sql1)
    answer = {"Data": 'viety'}
    print(answer)
    response_json = json.dumps(answer)
    return response_json

def third(nimi):
    sql = "update game set money = money - '" + "150" + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    sql1 = "update game set co2_budget = co2_budget + '" + "75" + "'"
    sql1 += " WHERE screen_name= '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    kursori1 = connection.cursor()
    kursori1.execute(sql1)
    answer = {"Data": 'viety'}
    print(answer)
    response_json = json.dumps(answer)
    return response_json

def fourth(nimi):
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
    return response_json

def fifth(nimi):
    sql = "update game set money = money - '" + "250" + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    sql1 = "update game set co2_budget = co2_budget + '" + "125" + "'"
    sql1 += " WHERE screen_name= '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    kursori1 = connection.cursor()
    kursori1.execute(sql1)
    answer = {"Data": 'viety'}
    print(answer)
    response_json = json.dumps(answer)
    return response_json

def sixth(nimi):
    sql = "update game set money = money - '" + "300" + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    sql1 = "update game set co2_budget = co2_budget + '" + "150" + "'"
    sql1 += " WHERE screen_name= '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    kursori1 = connection.cursor()
    kursori1.execute(sql1)
    answer = {"Data": 'viety'}
    print(answer)
    response_json = json.dumps(answer)
    return response_json

connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/first/<name>')
def first(name):
    response = first(name)
    return response

@app.route('/second/<name>')
def second(name):
    response = second(name)
    return response

@app.route('/third/<name>')
def third(name):
    response = third(name)
    return response

@app.route('/fourth/<name>')
def fourth(name):
    response = fourth(name)
    return response

@app.route('/fifth/<name>')
def fifth(name):
    response = fifth(name)
    return response

@app.route('/sixth/<name>')
def sixth(name):
    response = sixth(name)
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4099)
