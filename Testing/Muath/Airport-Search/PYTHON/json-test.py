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

lista_kentta = []
lista_icao = []
samples = []

def kentta(nimi):
    sql = "select airport.name, airport.ident from country inner join airport "
    sql += " on airport.iso_country = country.iso_country where country.name = '" + nimi + "' and scheduled_service = 'yes'"
    kursori = yhteys.cursor()
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



nimi = input("Anna nimi: ")
kentta(nimi)
print(samples)