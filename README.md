# Clear Skies

## Tekijät

- [@isakovero](https://www.github.com/isakovero)
- [@MuathOthman](https://www.github.com/MuathOthman)
- [@Agrinsadon](https://www.github.com/Agrinsadon)
- [@muhissadik](https://www.github.com/muhissadik)

## Discord

https://discord.gg/srNM26xz

# HTML toteutus

## Webpage Colors

| Hex             | Color                                                                |
| ----------------- | ------------------------------------------------------------------ |
| #FFA69E | <img valign='middle' alt='FFA69E' src='https://readme-swatches.vercel.app/FFA69E'/> |
| #FAF3DD | <img valign='middle' alt='FAF3DD' src='https://readme-swatches.vercel.app/FAF3DD'/> |
| #B8F2E6 | <img valign='middle' alt='B8F2E6' src='https://readme-swatches.vercel.app/B8F2E6'/> |
| #AED9E0 | <img valign='middle' alt='AED9E0' src='https://readme-swatches.vercel.app/AED9E0'/> |






# Python toteutus

## Python Packages

#### mysql-connector-python

https://dev.mysql.com/doc/connector-python/en/

#### tabulate

https://pypi.org/project/tabulate/

#### geopy
https://pypi.org/project/geopy/

#### flask

https://flask.palletsprojects.com/en/2.2.x/

#### json

https://www.json.org/json-en.html

#### responeses

https://pypi.org/project/responses/

## Johdanto

Projekti toteutetaan syksyllä 2022 laaditun projektisuunnitelman mukaisesti. Tässä dokumentissa käsitellään suunnittelemamme lentopelin yleisideaa ja toiminnallisia- sekä laadullisia vaatimuksia. Määrittelydokumentti on suunnattu ohjaamaan ryhmäämme toteutuksen aikana sekä helpottamaan pelin ymmärrystä asiakasta.

## Visio

Pelin tavoite on matkustaa eri lentokenttien välillä ja saavuttaa kahdeksan eri säätilaa aiheuttaen mahdollisimman vähän CO2-päästöjä. Peli määrittää pelaajalle CO2-päästöjen ylärajan. Lentokenttien välillä matkustetaan syöttämällä lentokent-tien nimiä tai ICAO-koodeja. Pelaajan saapuessa kohteeseen pelaajan on mahdollista saavuttaa uusi säätila ja mikäli säätila on jo saavutettu aikaisemmin pelaaja ei kerää kyseistä säätilaa uudelleen vaan joutuu siirtymään seuraavaan kohteeseen. Jokaisella lennolla pelaajan CO2-kapasiteetti pienenee riippuen matkan pituudes-ta. Jos CO2-päästöt ylittyvät siitä seuraa (Game over), joka tarkoittaa, että peli on hävitty ja joudut aloittamaan alusta. Kun saavutat tavoitetut säätilat ylittämättä CO2-kapasiteettia, läpäiset pelin. Tämän jälkeen ohjelma tulostaa pelaajalle hänen saavutuksensa pelin sijoituslistaan muita pelaajia vastaan.

![image](https://user-images.githubusercontent.com/111856849/193012953-f8fe41c7-f0c9-4789-a8ed-ea9203a48af8.png)


## Toiminnalliset vaatimukset

Käyttäjä aloittaa pelin, jolloin käyttäjälle annetaan kaksi vaihtoehtoa. Käyttäjä valitsee joko vaihtoehdon 1 ”uusi käyttäjä” tai vaihtoehdon 2 ”vanha käyttäjä”.

![image](https://user-images.githubusercontent.com/111856849/193012999-268dd6eb-eafd-463c-8480-7a8a5883fa68.png)


Pelaaja valitsee uuden käyttäjän, jolloin ohjelma kysyy pelaajalta käyttäjänimen ja käyttäjänimi tallentuu tietokantaan. Pelaaja määrittää pelille sen aloitussijainnin (airport.scheduled_service), jolloin ohjelma printtaa ohjeet & säännöt. Jos pelaaja valitsee vanhan käyttäjän, ohjelma kysyy pelaajalta käyttäjänimen. Tietokannan avulla tulostetaan jo saavutetut säätilat, lentokentät ja ilmoittaa jäljellä olevan CO2-päästökiintiön. Tämän jälkeen ohjelmaa antaa pelaajalle kolme vaihtoehtoa. 1. Ohjeet 2. Jatka viimeisintä suorituskertaa 3. Aloita alusta. 

Kun pelaaja on valinnut käyttäjätyypin hän voi aloittaa säätilojen keruun pelille asettamastaan aloitussijainnista. Kohteisiin matkustetaan syöttämällä peliin joko kohteen lentoaseman nimi tai kyseisen lentoaseman ICAO-koodi. Kunkin kohtee-seen siirtymisen jälkeen ohjelma kertoo pelaajalle jäljellä olevan hiilidioksidimäärän pelin hiilidioksidipäästökapasiteetista. Jokaisen lennon jälkeen pelaajalta kysytään kolme vaihtoehtoa: tallenna peli, lopeta peli ja jatka peliä (syötä seuraava kohde). Jos pelaaja ylittää asetetun CO2-rajan peli loppuu (game over). Ohjelma näyttää pelaajalle saavutetut säätilat sekä vieraillut lentokentät (tulokset). Jos pe-laaja saavuttaa kaikki kahdeksan säätilaa ylittämättä asetettua CO2 rajaa.

## Laadulliset vaatimukset
Pelaaja saa tiedon kuluttamastaan CO2-päästöistä sekä jäljellä olevasta CO2 määrästä. Pelaajan on saatava välitön palaute jokaisesta tekemästään toimenpiteestä. Lentokentän tietojen haku tietokannasta saa kestää korkeintaan kaksi sekuntia.


## Tietokannan rakenne
![lentopeliRelaatio (1)](https://user-images.githubusercontent.com/111856849/193352889-548ed744-4220-45e3-b214-606fbb93b933.png)

# JavaScript toteutus

## JavaScript Packages

#### Flask

https://flask.palletsprojects.com/en/2.2.x/

#### Requests

https://pypi.org/project/requests/

# Uudet Ominaisuudet
![Aicrafttoteutus](https://user-images.githubusercontent.com/111856849/204092352-3a8ed1b7-1487-475e-b7f1-31857b429b47.png)
![CO2OSTO](https://user-images.githubusercontent.com/111856849/204092361-de95f5a2-7d63-43bd-8def-8b7563de0f06.png)
![Round1](https://user-images.githubusercontent.com/111856849/204092371-7cd7c468-020d-4e20-8812-753df4c94cb4.png)
