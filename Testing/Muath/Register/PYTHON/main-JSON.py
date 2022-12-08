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
app = Flask(__name__)
@app.route('/kentta/<nimi>')
def kentta(nimi):
    try:
        def newuser(nimi, location):
            sql = "select screen_name from game"
            kursori = yhteys.cursor()
            kursori.execute(sql)
            tulos = kursori.fetchall()
            if (nimi,) in tulos:
                print("Käyttäjänimi on jo olemassa. Kirjaudu sisään painamalla 2.")
            else:
                sql = "INSERT INTO game (id, co2_consumed, co2_budget, location, screen_name)  "
                sql += "VALUES ('" + id_funktio + "', '0', '0', '" + location + "', '" + nimi + "')"
                kursori = yhteys.cursor()
                kursori.execute(sql)
                tulos = kursori.fetchall()
                print(sql)
                budjetti(nimi)
            return

        def id():
            testi = []
            sql = "select id from game;"
            kursori = yhteys.cursor()
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

        def budjetti(nimi):
            import random
            random_budjetti = random.randint(3917, 7834)
            random_budjetti1 = str(random_budjetti)
            sql = "UPDATE game set co2_budget= '" + random_budjetti1 + "'"
            sql += "Where screen_name = '" + nimi + "'"
            kursori = yhteys.cursor()
            kursori.execute(sql)
            tulos = kursori.fetchall()
            return

        id_funktio = id()
        nimi = input("Syötä uusi käyttäjätunnus: ").lower()
        location = input("Aloitus ICAO-koodi: ").upper()
        newuser(nimi, location)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
