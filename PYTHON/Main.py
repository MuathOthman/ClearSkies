import mysql.connector
import requests
import json
from flask_cors import CORS
from flask import Flask, Response, request


def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='ClearSkies',
        user='admin',
        password='12345',
        autocommit=True
    )


# Game-lists
samples = []
location_list = []
city_list = []
icao_list = []
weather_id_list = []
weather_list = []
id_lista = [1]


class Airplane:
    def __init__(self, name, range, co2):
        self.name = name
        self.range = range
        self.co2 = co2

    # Updates CO2 consumed column after a round
    def co2increase(self, distance, name):
        consumed = (self.co2 * distance) / 1000
        calculator = str(consumed)
        print(calculator)
        sql = "update game set co2_consumed = co2_consumed + '" + calculator + "'"
        sql += " WHERE screen_name= '" + name + "'"
        cursor = connection.cursor()
        cursor.execute(sql)


atr72 = Airplane('atr72', 1500, 50)
b737 = Airplane('b737', 4800, 100)
A350 = Airplane('A350', 30000, 150)


# First product-card
def first(name):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    print(result_set[0])
    for i in result_set:
        if i[0] > 50 or i[0] == 50:
            sql = "update game set money = money - '" + "50" + "'"
            sql += " WHERE screen_name= '" + name + "'"
            sql1 = "update game set co2_budget = co2_budget + '" + "25" + "'"
            sql1 += " WHERE screen_name= '" + name + "'"
            cursor = connection.cursor()
            cursor.execute(sql)
            cursor1 = connection.cursor()
            cursor1.execute(sql1)
            answer = {"Data": 'Transferred'}
            print(answer)
            response_json = json.dumps(answer)
            return Response(response=response_json, status=200, mimetype="application/json")
        else:
            return {'empty_pockets': "You dont have enough money!"}


# Second product-card
def second(name):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    print(result_set[0])
    for i in result_set:
        if i[0] > 100 or i[0] == 100:
            sql = "update game set money = money - '" + "100" + "'"
            sql += " WHERE screen_name= '" + name + "'"
            sql1 = "update game set co2_budget = co2_budget + '" + "50" + "'"
            sql1 += " WHERE screen_name= '" + name + "'"
            cursor = connection.cursor()
            cursor.execute(sql)
            cursor1 = connection.cursor()
            cursor1.execute(sql1)
            answer = {"Data": 'Transferred'}
            print(answer)
            response_json = json.dumps(answer)
            return Response(response=response_json, status=200, mimetype="application/json")
        else:
            return {'empty_pockets': "You dont have enough money!"}


# Third product-card
def third(name):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    print(result_set[0])
    for i in result_set:
        if i[0] > 150 or i[0] == 150:
            sql = "update game set money = money - '" + "150" + "'"
            sql += " WHERE screen_name= '" + name + "'"
            sql1 = "update game set co2_budget = co2_budget + '" + "75" + "'"
            sql1 += " WHERE screen_name= '" + name + "'"
            cursor = connection.cursor()
            cursor.execute(sql)
            cursor1 = connection.cursor()
            cursor1.execute(sql1)
            answer = {"Data": 'Transferred'}
            print(answer)
            response_json = json.dumps(answer)
            return Response(response=response_json, status=200, mimetype="application/json")
        else:
            return {'empty_pockets': "You dont have enough money!"}


# Fourth product-card
def fourth(name):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    print(result_set[0])
    for i in result_set:
        if i[0] > 200 or i[0] == 200:
            sql = "update game set money = money - '" + "200" + "'"
            sql += " WHERE screen_name= '" + name + "'"
            sql1 = "update game set co2_budget = co2_budget + '" + "100" + "'"
            sql1 += " WHERE screen_name= '" + name + "'"
            cursor = connection.cursor()
            cursor.execute(sql)
            cursor1 = connection.cursor()
            cursor1.execute(sql1)
            answer = {"Data": 'Transferred'}
            print(answer)
            response_json = json.dumps(answer)
            return Response(response=response_json, status=200, mimetype="application/json")
        else:
            return {'empty_pockets': "You dont have enough money!"}


# Fifth product-card
def fifth(name):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    print(result_set[0])
    for i in result_set:
        if i[0] > 250 or i[0] == 250:
            sql = "update game set money = money - '" + "250" + "'"
            sql += " WHERE screen_name= '" + name + "'"
            sql1 = "update game set co2_budget = co2_budget + '" + "125" + "'"
            sql1 += " WHERE screen_name= '" + name + "'"
            cursor = connection.cursor()
            cursor.execute(sql)
            cursor1 = connection.cursor()
            cursor1.execute(sql1)
            answer = {"Data": 'Transferred'}
            print(answer)
            response_json = json.dumps(answer)
            return Response(response=response_json, status=200, mimetype="application/json")
        else:
            return {'empty_pockets': "You dont have enough money!"}


# Sixth product-card
def sixth(name):
    sql = "SELECT money FROM game"
    sql += " where screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    print(result_set[0])
    for i in result_set:
        if i[0] > 300 or i[0] == 300:
            sql = "update game set money = money - '" + "300" + "'"
            sql += " WHERE screen_name= '" + name + "'"
            sql1 = "update game set co2_budget = co2_budget + '" + "150" + "'"
            sql1 += " WHERE screen_name= '" + name + "'"
            cursor = connection.cursor()
            cursor.execute(sql)
            cursor1 = connection.cursor()
            cursor1.execute(sql1)
            answer = {"Data": 'Transferred'}
            print(answer)
            response_json = json.dumps(answer)
            return Response(response=response_json, status=200, mimetype="application/json")
        else:
            return {'empty_pockets': "You dont have enough money!"}


# Flight page location
def location(name):
    sql = "SELECT latitude_deg, longitude_deg FROM airport, game"
    sql += " where location = ident and screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    for i in result_set:
        print(i)
        print(i[0])
        answer = {"Latitude": + i[0], "Longitude": + i[1]}
        print(answer)
        response_json = json.dumps(answer)
        return Response(response=response_json, status=200, mimetype="application/json")
    else:
        return {'wrong_name': "Give me a correct name"}


# Printing CO2-budget to the dashboard
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


# Airport search for airport page
def airportSearch(nimi):
    sql = "select airport.name, airport.ident from country inner join airport "
    sql += " on airport.iso_country = country.iso_country where country.name = '" + nimi + "' and scheduled_service = 'yes'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    if cursor.rowcount > 0:
        for i in result_set:
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


# Printing winners to the leaderboard
def leaderboard():
    samples = []
    sql = "select screen_name, count(*), co2_consumed from game, goal_reached where id = game_id group by co2_consumed ASC having (count(*)=4)"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    if cursor.rowcount > 0:
        for i in result_set:
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


# Checks if name already exists in database
def login(name):
    sql = f"select screen_name from game where screen_name= '{name}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        return {"correct": result_set[0]}
    else:
        return {"Error": "Give me a correct name"}


# Printing wallet to the dashboard
def wallet(name):
    sql = f"select money from game where screen_name ='{name}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        return {"money": result_set[0]}
    else:
        return {"Error": "Give me a correct name"}


# Calculates the distance between two icao codes
def calculator(name):
    sql = "SELECT latitude_deg, longitude_deg FROM airport, game"
    sql += " where location = ident and screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()

    location1 = location_list[0]
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident= '" + location1 + "'"
    cursor1 = connection.cursor()
    cursor1.execute(sql)
    result_set1 = cursor1.fetchall()

    sql = "UPDATE game set location= '" + location1 + "'"
    sql += "Where screen_name = '" + name + "'"
    cursor2 = connection.cursor()
    cursor2.execute(sql)
    result_set2 = cursor2.fetchall()

    # The calculation of CO2 emissions for different airplane types
    from geopy.distance import geodesic
    newport_ri = result_set[0]
    cleveland_oh = result_set1[0]
    list1 = []
    distance = geodesic(newport_ri, cleveland_oh).kilometers
    list1.append(distance)
    for i in list1:
        print('Etäisyys:')
        print(i)
        if i < 1500:
            atr72.co2increase(i, name)
        elif i < 4800:
            b737.co2increase(i, name)
        else:
            A350.co2increase(i, name)

# Function to travel to next location available
def next_location():
    args = request.args
    name = args.get("name")
    icao = args.get("icao")
    sql = "select ident from airport where scheduled_service =  'yes';"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    if (icao.upper(),) not in result_set:
        return {'wrong_icao': "Give a correct & available icao-code!"}
    else:
        location_list.append(icao)
    calculator(name)
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " where ident = '" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    for i in result_set:
        answer = {"Latitude": + i[0], "Longitude": + i[1]}
        print(answer)
        location_list.clear()
        response_json = json.dumps(answer)
        return Response(response=response_json, status=200, mimetype="application/json")


# Checks if user already exists in database during registration and checks if icao code is valid
def user_check(user, icao):
    sql = "select screen_name from game"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    if (user,) in result_set:
        return {'old': 'Username already taken'}
    else:
        sql = "select ident from airport where scheduled_service =  'yes';"
        cursor = connection.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        if (icao.upper(),) not in result_set:
            return {'icao': 'icao not available'}
        else:
            newaccount(user, icao)
        return {'new': 'welcome to clearskies'}


# Creates a new account to database
def newaccount(user, icao):
    sql = "INSERT INTO game (id, co2_consumed, co2_budget, location, screen_name, money)  "
    sql += "VALUES ('" + id() + "', '0', '0', '" + icao + "', '" + user + "', '0')"
    print(id())
    cursor = connection.cursor()
    cursor.execute(sql)
    create_budget(user)


# Creates a new id every time a new user is created
def id():
    test = []
    sql = "select id from game;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result_set:
            add = row[0] + 1
            test.append(str(add))
            for i in test:
                return i


# Creates a random CO2 budget for a new user
def create_budget(user):
    import random
    random_budget = random.randint(3917, 7834)
    random_budget1 = str(random_budget)
    sql = "UPDATE game set co2_budget= '" + random_budget1 + "'"
    sql += "Where screen_name = '" + user + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    return


# Finds players id
def id_find(name):
    test1 = []
    sql = "select id from game "
    sql += "Where screen_name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result_set:
            test1.append(str(row[0]))
            return str(row[0])


# Resets player's data
def restart(name):
    sql = "UPDATE game SET co2_consumed = '0', co2_budget= '0', location = 'efhk', money= '0'"
    sql += " WHERE screen_name= '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    create_budget(name)

    sql1 = "DELETE FROM goal_reached WHERE game_id = '" + id_find(name) + "'"
    cursor = connection.cursor()
    cursor.execute(sql1)


# Brings current weather using API to dashboard
def weather(name):
    sql = "SELECT location FROM game"
    sql += " WHERE screen_name= '" + name + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    for row in result_set:
        print(f"ICAO: {row[0]}")
        icao_list.append(row[0])
    sql = "SELECT municipality FROM airport"
    sql += " WHERE ident= '" + icao_list[-1] + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    for row in result_set:
        print(f"Municipality: {row[0]}")
        city_list.append(row[0])
    api_code = "155ede50dd2196d8e713fcae93acae99"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    all_url = url + "appid=" + api_code + "&q=" + city_list[-1]
    answer1 = requests.get(all_url)
    if answer1.status_code == 200:
        print(all_url)
        answer1_json = answer1.json()
        # print(answer1_json["weather"])
        for i in answer1_json["weather"]:
            print(f"Description: {i['main']}")
            temprature = (answer1_json['main']['temp'] - 273.15)
            print(f"Temprature: {int(temprature)} °C")
            answer = {"Description": f"{i['main']}", "Temperature": f"{round(answer1_json['main']['temp'] - 273.15)}"}
            print(answer)
            response_json = json.dumps(answer)
            return Response(response=response_json, status=200, mimetype="application/json")


#
def weather_id(saa):
    sql = "select id from goal "
    sql += "where main = '" + saa + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    for i in result_set:
        print(i)
        weather_id_list.append(i[0])


def name_id(name):
    test3 = []
    sql = "select id from game "
    sql += "Where screen_name = '" + name + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result_set:
            test3.append(str(row[0]))
            return str(row[0])


# Brings the latest achieved weather id
def order_id():
    sql = "select jarjestys from goal_reached;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result_set:
            amount = row[-1] + 1
            return str(amount)


# Adds into goal_reached table reached weather conditions
def push(name):
    sql = "INSERT INTO `goal_reached`"
    sql += "VALUES ('" + name_id(name) + "', '" + str(weather_id_list[-1]) + "', '" + str(id_lista[-1]) + "')"
    value = id_lista[-1] + 1
    id_lista.append(value)
    print(sql)
    print(id_lista)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    weatherachieved(name)


# Adding money to the database
def addmoney(name):
    sql = "update game set money = money + '" + '50' + "'"
    sql += " WHERE screen_name= '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)


# Adds money from collected weather conditions into sql
def weatherachieved(name):
    sql = "select main from goal left join goal_reached on goal.id = goal_id left join game on game.id = game_id where screen_name ='" + nimi + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    if 'Thunderstorm' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Rain' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Drizzle' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Snow' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Clouds' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Clear' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Mist' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Smoke' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Haze' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Dust' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Fog' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Sand' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Ash' in result_set:
        print('Adding 50$')
        addmoney(name)
    elif 'Squall' in result_set:
        print('Adding 50$')
        addmoney(name)
    else:
        print('Adding 50$')
        addmoney(name)


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
        name = args.get("name")
        icao = args.get("icao")
        sql = "SELECT location FROM game"
        sql += " WHERE screen_name= '" + name + "'"
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        for row in result_set:
            print(f"ICAO: {row[0]}")
            icao_list.append(row[0])
        sql = "SELECT municipality FROM airport"
        sql += " WHERE ident= '" + icao_list[-1] + "'"
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        for row in result_set:
            print(f"Municipality: {row[0]}")
            city_list.append(row[0])
        api_code = "155ede50dd2196d8e713fcae93acae99"
        url = "http://api.openweathermap.org/data/2.5/weather?"
        all_url = url + "appid=" + api_code + "&q=" + city_list[-1]
        answer1 = requests.get(all_url)
        if answer1.status_code == 200:
            print(all_url)
            answer1_json = answer1.json()
            # print(answer1_json["weather"])
            for i in answer1_json["weather"]:
                print(f"Description: {i['main']}")
                transferData = i['main']
                print(transferData)
                temprature = (answer1_json['main'])
                answer = {"Description": f"{i['main']}"}
                weather_id(transferData)
                push(name)
                print(answer)
                response_json = json.dumps(answer)
                list.clear()
                weather_list.clear()
                weather_id_list.clear()
                icao_list.clear()
                city_list.clear()
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
        cursor = connection.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        if cursor.rowcount > 0:
            for i in result_set:
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
        list4 = []
        sql = "select count(*) from game, goal_reached where id = game_id"
        sql += " and screen_name= '" + name + "'"
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        for row in result_set:
            list4.append(row[0])
        answer = {'tila': list4[0]}
        list4.clear()
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
