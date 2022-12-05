#Add this to main !!

def laskuri(nimi):
    sql = "SELECT latitude_deg, longitude_deg FROM airport, game"
    sql += " where location = ident and screen_name = '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    # location = input("Aloitus ICAO-koodi: ")
    location1 = str(airports_old_user())
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident= '" + location1 + "'"
    kursori1 = yhteys.cursor()
    kursori1.execute(sql)
    tulos1 = kursori1.fetchall()

    sql = "UPDATE game set location= '" + location1 + "'"
    sql += "Where screen_name = '" + nimi + "'"
    kursori2 = yhteys.cursor()
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