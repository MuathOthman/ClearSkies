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

samples = []

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

def location(name):
    sql = "SELECT latitude_deg, longitude_deg FROM airport, game"
    sql += " where location = ident and screen_name = '" + name + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(i)
        print(i[0])
        answer = {"Latitude": + i[0], "Longitude": + i[1]}
        print(answer)
        response_json = json.dumps(answer)
        return Response(response=response_json, status=200, mimetype="application/json")

def budget(name):
    sql = f"select co2_consumed, co2_budget from game where screen_name ='{name}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    print(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        print(result_set[0])
        return {"co2consumed": result_set[0], "co2budget": result_set[1]}
    else:
        return {"Error": "Give me a correct name"}


def airportSearch(nimi):
    sql = "select airport.name, airport.ident from country inner join airport "
    sql += " on airport.iso_country = country.iso_country where country.name = '" + nimi + "' and scheduled_service = 'yes'"
    kursori = connection.cursor()
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
        samples.clear()
    return Response(response=response_json, status=200, mimetype="application/json")

def leaderboard():
    samples = []
    sql = "select screen_name, count(*), co2_consumed from game, goal_reached where id = game_id group by co2_consumed ASC having (count(*)=4)"
    kursori = connection.cursor()
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

@app.route('/location/<name>')
def locationFlask(name):
    response = location(name)
    return response

@app.route('/budget/<name>')
def budgetFlask(name):
    response = budget(name)
    return response

@app.route('/airportsearch/<name>')
def airportsearchFlask(name):
    response = airportSearch(name)
    return response

@app.route('/leaderboard/')
def leaderboardFlask():
    response = leaderboard()
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=1029)
