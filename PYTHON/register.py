import mysql.connector
from flask_cors import CORS
from flask import Flask


def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='ClearSkies',
        user='admin',
        password='12345',
        autocommit=True
    )


connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def newuser(user, location):
    sql = f"select screen_name from game where screen_name= '{user}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        return {"old": result_set[0]}
    else:
        newaccount(user, location)
        return {"new": "welcome to clearskies"}


def newaccount(user, location):
    sql = "INSERT INTO game (id, co2_consumed, co2_budget, location, screen_name, money)  "
    sql += "VALUES ('" + id_funktio + "', '0', '0', '" + location + "', '" + user + "', '0')"
    print(id_funktio)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    budjetti(user)


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


def budjetti(user):
    import random
    random_budjetti = random.randint(3917, 7834)
    random_budjetti1 = str(random_budjetti)
    sql = "UPDATE game set co2_budget= '" + random_budjetti1 + "'"
    sql += "Where screen_name = '" + user + "'"
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return


id_funktio = id()


@app.route('/signup/<user>/<location>')
def signup(user, location):
    response = newuser(user, location)
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4400)
