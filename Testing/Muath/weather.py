import mysql.connector
import requests
from flask import Flask, Response, request
import mysql.connector
from flask_cors import CORS
import requests

list = []
saa = []
saa_id = []

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ClearSkies',
         user='admin',
         password='12345',
         autocommit=True
         )

def api():
    api_koodi = "155ede50dd2196d8e713fcae93acae99"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    kaupunki = input("Anna kaupunki: ")
    koko_url = url + "appid=" + api_koodi + "&q=" + kaupunki
    # print(koko_url)
    print(f"{kaupunki}'s weather:")
    vastaus = requests.get(koko_url)
    if vastaus.status_code == 200:
        print(koko_url)
        vastaus_json = vastaus.json()
        for i in vastaus_json["weather"]:
            print(i["main"])
            #print(f"('{i['main']}',)")
            testi = f"'{i['main']}'"
            testi1 = f"({i['main']})"
            list.append(testi)

        return

api()


#select id from goal where main = 'Clouds';

def id():
    sql = "select id from goal "
    sql += "where main =" + list[0]
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(i)
    saa_id.append(i[0])

def id_find(nimi):
    testi = []
    sql = "select id from game "
    sql += "Where screen_name = '" + nimi + "'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            testi.append(str(rivi[0]))

    return str(rivi[0])


def push():
    sql = "INSERT INTO `goal_reached`"
    sql += "VALUES ('" + id_find(nimi) + "', '" + str(saa_id[0]) + "')"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

id()
print(saa_id)

nimi = input("Nimi: ")
push()



