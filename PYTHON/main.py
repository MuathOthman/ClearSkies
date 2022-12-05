import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='ClearSkies',
    user='admin',
    password='12345',
    autocommit=True
)

def airports(location):
    sql = "select ident from airport where scheduled_service =  'yes';"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    while True:

        if (location, ) not in tulos:
            print("Anna oikea ICAO-koodi!")
            #location = input("Syötä käytössä olevan lentoaseman ICAO-koodi: ")
        elif (location, ) in tulos:
            newuser(nimi, location)
            break
        location = input("Syötä käytössä olevan lentoaseman ICAO-koodi: ").upper()
    return

def airports_old_user():
    testi = []
    sql = "select ident from airport where scheduled_service =  'yes';"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    while True:
        location = same_airport()
        if (location, ) not in tulos:
            print("Anna oikea ICAO-koodi!")
        elif (location, ) in tulos:
            break
    return location

def icao2():
    location = input("Syötä käytössä olevan lentoaseman ICAO-koodi: ").upper()
    return location

def same_airport():
    testi = []
    sql = "select location from game "
    sql += "Where screen_name = '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    while True:
        #location = input("Syötä käytössä olevan lentoaseman ICAO-koodi: ").upper()
        location = icao2()
        if (location, ) in tulos:
            print(f"Mistä: {location}\nMihin: {location}")
            print("Etsintä lähtö- ja paluukaupungin ollessa sama ei ole mahdollinen.")
            print("--------------------")
            #airports_old_user(location)
        elif (location, ) not in tulos:
            break
    return location
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
        budjetti(nimi)
        ohjeet_newuser(nimi)
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
def ohjeet_newuser(nimi):
    sql = "select co2_budget from game "
    sql += "Where screen_name = '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for i in tulos:
            print(f"--------------------\nTervetuloa lentopeliin {nimi}!\nYhdistyneet Kansakunnat ovat asettaneet määräyksen, "
                  f"jonka avulla pyritään vähentämään\nCO2-päästöjä maailmanlaajuisesti. "
                  f"Matkustajien vuosittainen CO2-päästökapasiteetti on asetettu {i[0]} kilogrammaksi vuodessa.\n"
                  f"Tavoitteena on siirtyä lentokoneella lentoasemien välillä syöttäen peliin ICAO-lentokenttäkoodeja "
                  f"sekä kerätä kahdeksan erilaista\nsäätilaa ylittämättä YK:n kestävän kehityksen asetusta. "
                  f"Tieto säätilasaavutuksesta sekä kulutetuista CO2-päästöistä ilmoitetaan\njokaisen pelikierroksen jälkeen. "
                  f"CO2-budjetin rajoissa pelaaja voi matkustaa rajattomasti eri lentokenttien välillä.\nCO2-päästökapasiteetin "
                  f"ylittyessä peli joudutaan aloittamaan alusta. Kerättyäsi kahdeksan haluttua säätilaa annetun budjetin\nrajoissa "
                  f"olet läpäissyt pelin onnistuneesti.\n--------------------")
        while True:
            print("1, Lentokenttien haku")
            print("2, Aloita peli")
            print("--------------------")
            valinta = input("Valitse numero: ")
            print("--------------------")
            if valinta == "1":
                kenttahaku()
            elif valinta == "2":
                mainask(nimi)
            else:
                print("Valitse 1-2!")
def kenttahaku():
    print("Kirjoita maan nimi englanniksi.")
    nimi = 0
    while nimi != "":
        nimi = input("Anna maan nimi. Paina enter, jos haluat lopettaa: ")
        sql = "select airport.ident , airport.name from country inner join airport "
        sql += " on airport.iso_country = country.iso_country where country.name = '" + nimi + "' and scheduled_service = 'yes'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            for i in tulos:
                print(f"{i[1]} ({i[0]})")
        elif nimi == "":
            print("--------------------")
            break
        else:
            print("Kirjoita nimi englanniksi!")

def co2_consumed(nimi):
    while True:
        lista = []
        sql1 = "select co2_consumed from game "
        sql1 += "Where screen_name = '" + nimi + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql1)
        tulos1 = kursori.fetchall()
        if kursori.rowcount > 0:
            for i in tulos1:
                lista.append(i)
        return i[0]

def olduser(nimi):
    sql = "SELECT screen_name FROM game"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if (nimi,) in tulos:

            while True:
                pelikortti()
                print("1, Aloita alusta")
                print("2, Ohjeet")
                print("3, Jatka peliä")
                print("--------------------")
                valinta = input("Valitse numero: ")
                print("--------------------")
                if valinta == "1":
                    restart(nimi)
                elif valinta == "2":
                    ohjeet_old_user(nimi)
                elif valinta == "3":
                    mainask(nimi)
                else:
                   print("Valitse 1-3 väliltä!")
    elif (nimi,) not in tulos:
        print("Käyttäjä ei ole olemassa! Tee uusi käyttäjä painamalla 1.")
    return
def ohjeet_old_user(nimi):
    sql = "select co2_budget from game "
    sql += "Where screen_name = '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for i in tulos:
            print(f"--------------------\nTervetuloa lentopeliin {nimi}!\nYhdistyneet Kansakunnat ovat asettaneet määräyksen, "
                  f"jonka avulla pyritään vähentämään\nCO2-päästöjä maailmanlaajuisesti. "
                  f"Matkustajien vuosittainen CO2-päästökapasiteetti on asetettu {i[0]} kilogrammaksi vuodessa.\n"
                  f"Tavoitteena on siirtyä lentokoneella lentoasemien välillä syöttäen peliin ICAO-lentokenttäkoodeja "
                  f"sekä kerätä kahdeksan erilaista\nsäätilaa ylittämättä YK:n kestävän kehityksen asetusta. "
                  f"Tieto säätilasaavutuksesta sekä kulutetuista CO2-päästöistä ilmoitetaan\njokaisen pelikierroksen jälkeen. "
                  f"CO2-budjetin rajoissa pelaaja voi matkustaa rajattomasti eri lentokenttien välillä.\nCO2-päästökapasiteetin "
                  f"ylittyessä peli joudutaan aloittamaan alusta. Kerättyäsi kahdeksan haluttua säätilaa annetun budjetin\nrajoissa "
                  f"olet läpäissyt pelin onnistuneesti.\n--------------------")
        while True:
            print("1, Lentokenttien haku")
            print("2, Jatka peliä")
            print("--------------------")
            valinta = input("Valitse numero: ")
            print("--------------------")
            if valinta == "1":
                kenttahaku()
            elif valinta == "2":
                mainask(nimi)
            else:
                print("Valitse 1-2!")

        return

def airports_old_user_restart():
    testi = []
    sql = "select ident from airport where scheduled_service =  'yes';"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    while True:
        location = input("Syötä käytössä olevan lentoaseman ICAO-koodi: ").upper()
        if (location, ) not in tulos:
            print("Anna oikea ICAO-koodi!")
        elif (location, ) in tulos:
            break
    return location

def restart(nimi):
    #icao1 = input("Aloitus ICAO-koodi: ")
    location1 = str(airports_old_user_restart())
    sql = "UPDATE game SET co2_consumed = '0', co2_budget= '0', location = '" + location1 + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    budjetti(nimi)
    sql1 = "DELETE FROM goal_reached WHERE game_id = '" + id_find(nimi) + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql1)
    tulos1 = kursori.fetchall()
    #olduser(nimi)
    return
def pelikortti():
    sql = "SELECT co2_consumed, co2_budget, location FROM game"
    sql += " WHERE screen_name= '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"--------------------\nPelikorttisi:\nKulutettu CO2: {rivi[0]}\nCO2 budjetti: {rivi[1]}"
                  f"\nSijaintisi: {rivi[2]}\n--------------------")
def saa_reached(nimi):
    while True:
        lista = []
        sql1 = "select count(*) from game, goal_reached "
        sql1 += "where id = game_id and screen_name='" + nimi + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql1)
        tulos1 = kursori.fetchall()
        if kursori.rowcount > 0:
            for i in tulos1:
                lista.append(i)
        return i[0]
def mainask(nimi):
    testi = []
    i = co2_consumed(nimi)
    s = saa_reached(nimi)
    sql = "select co2_budget from game "
    sql += "Where screen_name = '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            while i < rivi[0] and s != 8:
                sql = "select count(*), co2_consumed from game, goal_reached where id = game_id"
                sql += " and screen_name= '" + nimi + "'"
                #print(sql)
                kursori = yhteys.cursor()
                kursori.execute(sql)
                tulos = kursori.fetchall()
                for m in tulos:
                    co2_lisaaminen(nimi)
                    saa(nimi)
                    tallenna()
                    i = m[1]
                    s = m[0]
                    break
            else:
                tulokset(nimi)
                break

def leaderborad():
    testi = []
    from tabulate import tabulate
    sql = "select screen_name, count(*), co2_consumed from game, goal_reached where id = game_id group by co2_consumed ASC having (count(*)=8);;"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print("Voitit!. WINNER WINNER BUTTER CHICKEN DINNER!")
    print("SIJOITUSLISTA: ")
    header = ["NIMI",  "SÄÄTILAT", "CO2-PÄÄSTÖT"]
    print(tabulate(tulos, headers=header))
    return
def tulokset(nimi):
    i = co2_consumed(nimi)
    s = saa_reached(nimi)
    sql = "select count(*), co2_consumed from game, goal_reached where id = game_id"
    sql += " and screen_name= '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        if s == 8:
            win(nimi)
        elif s != 8:
            luuseri(nimi)

def luuseri(nimi):
    print("HÄVISIT!. YLITIT RAJAN")
    print("1, Aloita peli alusta")
    print("2, Lopeta peli")
    valinta = input("Valitse numero: ")
    while True:
        if valinta == "1":
            restart(nimi)
            olduser(nimi)
        elif valinta == "2":
            print("Ohjelma sammuu!")
            exit()
        else:
            print("--------------------")
            print("Valitse 1-2!")
            valikko_loser()


def win(nimi):
    #print("Voitit!. WINNER WINNER CHICKEN DINNER!")
    leaderborad()
    print("--------------------")
    print("1, Aloita peli alusta")
    print("2, Lopeta peli")
    valinta = input("Valitse numero: ")
    while True:
        if valinta == "1":
            restart(nimi)
            olduser(nimi)
        elif valinta == "2":
            print("Ohjelma sammuu!")
            exit()
        else:
            print("--------------------")
            print("Valitse 1-2!")
            valikko_win()


def valikko_win():
    print("--------------------")
    print("1, Aloita peli alusta")
    print("2, Lopeta peli")
    valinta = input("Valitse numero: ")
    if valinta == "1":
        restart(nimi)
    elif valinta == "2":
        print("Ohjelma sammuu!")
        exit()
    else:
        valikko_win

def valikko_loser():
    print("--------------------")
    print("1, Aloita peli alusta")
    print("2, Lopeta peli")
    valinta = input("Valitse numero: ")
    if valinta == "1":
        restart(nimi)
    elif valinta == "2":
        print("Ohjelma sammuu!")
        exit()
    else:
        valikko_loser()

def saa_budjetti(nimi):
    testi = []
    sql = "select name from goal left join goal_reached on goal.id = goal_id  left join game on game.id = game_id "
    sql += " where screen_name = '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print("--------------------")
    print("Saavutetut säätilat:")
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(rivi[0])
    print("--------------------")
    return
def tallenna():
    while True:
        print("--------------------")
        print("1, Tallenna ja lopeta")
        print("2, Näytä pelikortti")
        print("3, Näytä sääkortti")
        print("4, Jatka peliä")
        print("--------------------")
        valinta = input("Valitse numero: ")
        if valinta == "1":
            print("Tallennus onnistui!")
            print("Ohjelma sammuu! :)")
            exit()
            break
        elif valinta == "2":
            pelikortti()
            tallenna()
        elif valinta == "3":
            saa_budjetti(nimi)
        elif valinta == "4":
            mainask(nimi)
        else:
            print("Valitse 1-4 väliltä!")
def co2_lisaaminen(nimi):
    sql = "update game set co2_consumed = co2_consumed + '" + laskuri(nimi) + "'"
    sql += " WHERE screen_name= '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return
def laskuri(nimi):
    sql = "SELECT latitude_deg, longitude_deg FROM airport, game"
    sql += " where location = ident and screen_name = '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    #location = input("Aloitus ICAO-koodi: ")
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
    etaisuus = geodesic(newport_ri, cleveland_oh).kilometers
    paasot = (etaisuus * 102) / 1000
    return str(int(paasot))
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
def saa(nimi):
    import random
    sql = "select goal_id from goal_reached where game_id = '" + id_find(nimi) + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    saa_id = random.randint(1, 8)
    if (saa_id,) in tulos:
        sql1 = "select name from goal "
        sql1 += "where id ='" + str(saa_id) + "'"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql1)
        tulos = kursori.fetchall()
        for i in tulos:
            print(f"Määränpään säätila on {i[0]}")
            print("Tämä säätila on jo saavutettu")
    elif (saa_id,) not in tulos:
        sql = "INSERT INTO `goal_reached`"
        sql += "VALUES ('" + id_find(nimi) + "', '" + str(saa_id) + "')"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        sql1 = "select name from goal "
        sql1 += "where id ='" + str(saa_id) + "'"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql1)
        tulos = kursori.fetchall()
        for i in tulos:
            print(f"Määränpään säätila on {i[0]}")
            print("Keräsit uuden säätilan!")

    return

id_funktio = id()
print("Tervetuloa lentopeliin!")
print("--------------------")
while True:
    print("1, Rekisteröidy")
    print("2, Kirjaudu sisään")
    print("--------------------")
    valinta = input("Valitse numero: ")
    print("--------------------")
    if valinta == "1":
        nimi = input("Syötä uusi käyttäjätunnus: ").lower()
        location = input("Aloitus ICAO-koodi: ").upper()
        airports(location)
    elif valinta == "2":
        nimi = input("Syötä käyttäjätunnus: ").lower()
        olduser(nimi)
    else:
        print("Valitse 1-2!")




