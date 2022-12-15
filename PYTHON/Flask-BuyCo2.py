from flask import Flask, Response, request
import mysql.connector

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
location_lista = []
city_lista = []
icao_lista = []
saa_id = []
saa = []
id_lista = [1]


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
        else:
            return {'empty_pockets': "You dont have enough money!"}


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
        else:
            return {'empty_pockets': "You dont have enough money!"}


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
        else:
            return {'empty_pockets': "You dont have enough money!"}


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
        else:
            return {'empty_pockets': "You dont have enough money!"}


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
        else:
            return {'empty_pockets': "You dont have enough money!"}


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
        else:
            return {'empty_pockets': "You dont have enough money!"}


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
    else:
        return {'wrong_name': "Give me a correct name"}


def co2budget(name):
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
    else:
        return {'wrong_country': "Give me a correct country!"}


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


def login(name):
    sql = f"select screen_name from game where screen_name= '{name}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        return {"correct": result_set[0]}
    else:
        return {"Error": "Give me a correct name"}
    return result_set[0]


def wallet(name):
    sql = f"select money from game where screen_name ='{name}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        return {"money": result_set[0]}
    else:
        return {"Error": "Give me a correct name"}


def calculator(nimi):
    sql = "SELECT latitude_deg, longitude_deg FROM airport, game"
    sql += " where location = ident and screen_name = '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    location1 = location_lista[0]
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident= '" + location1 + "'"
    kursori1 = connection.cursor()
    kursori1.execute(sql)
    tulos1 = kursori1.fetchall()

    sql = "UPDATE game set location= '" + location1 + "'"
    sql += "Where screen_name = '" + nimi + "'"
    kursori2 = connection.cursor()
    kursori2.execute(sql)
    tulos2 = kursori2.fetchall()

    from geopy.distance import geodesic
    newport_ri = tulos[0]
    cleveland_oh = tulos1[0]
    list1 = []
    etaisuus = geodesic(newport_ri, cleveland_oh).kilometers
    list1.append(etaisuus)
    for i in list1:
        print(i)
        if i < 1500:
            small = (i * 50) / 1000
            return str(int(small))
        elif i < 4800:
            medium = (i * 100) / 1000
            return str(int(medium))
        else:
            large = (i * 150) / 1000
            return str(int(large))


def co2_increase(nimi):
    sql = "update game set co2_consumed = co2_consumed + '" + calculator(nimi) + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    return


def next_location():
    args = request.args
    nimi = args.get("nimi")
    icao = args.get("icao")
    sql = "select ident from airport where scheduled_service =  'yes';"
    # print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if (icao.upper(),) not in tulos:
        return {'wrong_icao': "Give a correct & available icao-code!"}
    else:
        location_lista.append(icao)
    co2_increase(nimi)
    calculator(nimi)
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " where ident = '" + icao + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        answer = {"Latitude": + i[0], "Longitude": + i[1]}
        print(answer)
        location_lista.clear()
        response_json = json.dumps(answer)
        return Response(response=response_json, status=200, mimetype="application/json")


def user_check(user, icao):
    sql = "select screen_name from game"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if (user,) in tulos:
        return {'old': 'Username already taken'}
    else:
        sql = "select ident from airport where scheduled_service =  'yes';"
        kursori = connection.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if (icao.upper(),) not in tulos:
            return {'icao': 'icao not available'}
        else:
            newaccount(user, icao)
        return {'new': 'welcome to clearskies'}


def newaccount(user, icao):
    sql = "INSERT INTO game (id, co2_consumed, co2_budget, location, screen_name, money)  "
    sql += "VALUES ('" + id() + "', '0', '0', '" + icao + "', '" + user + "', '0')"
    print(id())
    kursori = connection.cursor()
    kursori.execute(sql)
    create_budget(user)


def id():
    testi = []
    sql = "select id from game;"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            moi = rivi[0] + 1
        # print(moi)
        testi.append(str(moi))
        # print(testi)
        for i in testi:
            # print(i)
            return i


def create_budget(user):
    import random
    random_budjetti = random.randint(3917, 7834)
    random_budjetti1 = str(random_budjetti)
    sql = "UPDATE game set co2_budget= '" + random_budjetti1 + "'"
    sql += "Where screen_name = '" + user + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return


def id_find(name):
    testi = []
    sql = "select id from game "
    sql += "Where screen_name = '" + name + "'"
    # print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            testi.append(str(rivi[0]))
        return str(rivi[0])


def restart(name):
    sql = "UPDATE game SET co2_consumed = '0', co2_budget= '0', location = 'efhk', money= '0'"
    sql += " WHERE screen_name= '" + name + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    create_budget(name)

    sql1 = "DELETE FROM goal_reached WHERE game_id = '" + id_find(name) + "'"
    kursori = connection.cursor()
    kursori.execute(sql1)


def weather(name):
    sql = "SELECT location FROM game"
    sql += " WHERE screen_name= '" + name + "'"
    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tuos = kursori.fetchall()
    for rivi in tuos:
        print(f"ICAO: {rivi[0]}")
        icao_lista.append(rivi[0])
    sql = "SELECT municipality FROM airport"
    sql += " WHERE ident= '" + icao_lista[-1] + "'"
    print(sql)
    kursori = connection.cursor()
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


def weather_id(saa):
    sql = "select id from goal "
    sql += "where main = '" + saa + "'"
    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(i)
    saa_id.append(i[0])


def name_id(nimi):
    testi = []
    sql = "select id from game "
    sql += "Where screen_name = '" + nimi + "'"
    # print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            testi.append(str(rivi[0]))
    return str(rivi[0])


def order_id():
    testi = []
    sql = "select jarjestys from goal_reached;"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            summa = rivi[-1] + 1
            return str(summa)


def push(nimi):
    sql = "INSERT INTO `goal_reached`"
    sql += "VALUES ('" + name_id(nimi) + "', '" + str(saa_id[-1]) + "', '" + str(id_lista[-1]) + "')"
    summa = id_lista[-1] + 1
    id_lista.append(summa)
    print(sql)
    print(id_lista)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    weatherachieved(nimi)


def addmoney(nimi):
    sql = "update game set money = money + '" + '50' + "'"  # Adding the amount into sql
    sql += " WHERE screen_name= '" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)


def weatherachieved(nimi):
    sql = "select main from goal left join goal_reached on goal.id = goal_id left join game on game.id = game_id where screen_name ='" + nimi + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if 'Thunderstorm' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Rain' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Drizzle' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Snow' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Clouds' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Clear' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Mist' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Smoke' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Haze' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Dust' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Fog' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Sand' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Ash' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    elif 'Squall' in tulos:
        print('lisätään 50')
        addmoney(nimi)
    else:
        print('lisätään 50')
        addmoney(nimi)


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
    response = co2budget(name)
    return response


@app.route('/airportsearch/<name>')
def airportsearchFlask(name):
    response = airportSearch(name)
    return response


@app.route('/leaderboard/')
def leaderboardFlask():
    response = leaderboard()
    return response


@app.route('/login/<name>')
def loginFlask(name):
    response = login(name)
    return response


@app.route('/wallet/<name>')
def walletFlask(name):
    response = wallet(name)
    return response


@app.route('/nextlocation/')
def nextlocationFlask():
    response = next_location()
    return response


@app.route('/signup/<user>/<icao>')
def signup(user, icao):
    response = user_check(user, icao)
    return response


@app.route('/restart/<name>')
def restartFlask(name):
    response = restart(name)
    return response


@app.route('/weather/<name>')
def weatherFlask(name):
    response = weather(name)
    return response


@app.route('/weathercard/')
def weathercard():
    try:
        args = request.args
        nimi = args.get("nimi")
        icao = args.get("icao")
        sql = "SELECT location FROM game"
        sql += " WHERE screen_name= '" + nimi + "'"
        print(sql)
        kursori = connection.cursor()
        kursori.execute(sql)
        tuos = kursori.fetchall()
        for rivi in tuos:
            print(f"ICAO: {rivi[0]}")
            icao_lista.append(rivi[0])
        sql = "SELECT municipality FROM airport"
        sql += " WHERE ident= '" + icao_lista[-1] + "'"
        print(sql)
        kursori = connection.cursor()
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
                transferData = i['main']
                print(transferData)
        temprature = (vastaus_json['main'])
        answer = {"Description": f"{i['main']}"}
        weather_id(transferData)
        push(nimi)
        print(answer)
        response_json = json.dumps(answer)
        list.clear()
        saa.clear()
        saa_id.clear()
        icao_lista.clear()
        city_lista.clear()
        return Response(response=response_json, status=200, mimetype="application/json")
    except ValueError:
        text = "Invalid input value, a not number"
        return Response(response=text, status=400)
    except TypeError:
        responseText = "Invalid parameter: missing?"
        return Response(response=responseText, status=400)


@app.route('/saa/<name>')
def code(name):
    try:
        sql = "select goal_id from goal_reached"
        sql += " where game_id = '" + id_find(name) + "'" + 'order by jarjestys'
        print(sql)
        kursori = connection.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            for i in tulos:
                saa_json = {"saa": i[-1]}
                print('alkaa')
                print(i)
                response_json = json.dumps(saa_json)
            return Response(response=response_json, status=200, mimetype="application/json")
    except ValueError:
        text = "Invalid input value, a not number"
        return Response(response=text, status=400)
    except TypeError:
        responseText = "Invalid parameter: missing?"
        return Response(response=responseText, status=400)


@app.route('/winner/<name>')
def winner(name):
    try:
        lista = []
        sql = "select count(*) from game, goal_reached where id = game_id"
        sql += " and screen_name= '" + name + "'"
        print(sql)
        kursori = connection.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        for rivi in tulos:
            lista.append(rivi[0])
        answer = {'tila': lista[0]}
        lista.clear()
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
    app.run(use_reloader=True, host='127.0.0.1', port=1029)
