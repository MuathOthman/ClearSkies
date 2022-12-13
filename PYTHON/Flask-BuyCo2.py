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
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos[0])
    for i in tulos:
        if i[0] > 100 or i[0] == 100:
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

def second(nimi):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos[0])
    for i in tulos:
        if i[0] > 100 or i[0] == 100:
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
            return Response(response=response_json, status=200, mimetype="application/json")

def third(nimi):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos[0])
    for i in tulos:
        if i[0] > 150 or i[0] == 150:
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
            return Response(response=response_json, status=200, mimetype="application/json")

def fourth(nimi):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos[0])
    for i in tulos:
        if i[0] > 200 or i[0] == 200:
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


def fifth(nimi):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos[0])
    for i in tulos:
        if i[0] > 250 or i[0] == 250:
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
            return Response(response=response_json, status=200, mimetype="application/json")

def sixth(nimi):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos[0])
    for i in tulos:
        if i[0] > 300 or i[0] == 300:
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
            return Response(response=response_json, status=200, mimetype="application/json")


connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/first/<name>')
def firstFlask(name):
    response = first(name)
    return response

@app.route('/second/<name>')
def secondFlask(name):
    response = second(name)
    return response

@app.route('/third/<name>')
def thirdFlask(name):
    response = third(name)
    return response

@app.route('/fourth/<name>')
def fourthFlask(name):
    response = fourth(name)
    return response

@app.route('/fifth/<name>')
def fifthFlask(name):
    response = fifth(name)
    return response

@app.route('/sixth/<name>')
def sixthFlask(name):
    response = sixth(name)
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=1029)
