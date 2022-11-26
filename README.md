# Clear Skies

## Tekijät

- [@isakovero](https://www.github.com/isakovero)
- [@MuathOthman](https://www.github.com/MuathOthman)
- [@Agrinsadon](https://www.github.com/Agrinsadon)
- [@muhissadik](https://www.github.com/muhissadik)


## Python Packages

#### mysql-connector-python

https://dev.mysql.com/doc/connector-python/en/

#### tabulate

https://pypi.org/project/tabulate/

#### geopy
https://pypi.org/project/geopy/
## Webpage Colors

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Primary #1 | ![#FFA69E](https://via.placeholder.com/10/FFA69E?text=+) #FFA69E |
| Primary #2 | ![#FAF3DD](https://via.placeholder.com/10/FAF3DD?text=+) #FAF3DD |
| Primary #3 | ![#B8F2E6](https://via.placeholder.com/10/B8F2E6?text=+) #B8F2E6 |
| Primary #4 | ![#AED9E0](https://via.placeholder.com/10/AED9E0?text=+) #AED9E0 |


# Python toteutus



## Käytetyt PYTHON PACKAGES

- mysql-connector-python https://dev.mysql.com/doc/connector-python/en/
- tabulate https://pypi.org/project/tabulate/
- geopy https://pypi.org/project/geopy/

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
