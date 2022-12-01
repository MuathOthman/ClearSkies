# Clear Skies

## Porttinumerot (HUOM! PYTHON)

- CO2-budget (http://127.0.0.1:3000/)
- Login (http://127.0.0.1:3010/)
- Main (http://127.0.0.1:3020/)
- Money (http://127.0.0.1:3030/)
- Weather (http://127.0.0.1:3040/)


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

# JavaScript toteutus

## JavaScript Packages

#### Flask

https://flask.palletsprojects.com/en/2.2.x/

#### Requests

https://pypi.org/project/requests/

# Määrittelydokumentti


## Johdanto

Tässä dokumentissa käsitellään suunnittelemamme lentopelin yleis-ideaa, toiminnallisia- ja laadullisia vaatimuksia. Dokumentti sisältää pe-lin vision, läpäisykuvauksen, poikkeavat suorituspolut ja toiminnalliset- sekä laadulliset vaatimukset. Määrittelydokumentti on suunnattu oh-jaamaan ryhmäämme toteutuksen aikana sekä helpottamaan pelin ymmärrystä. 

## Visio

Pelin tavoite on matkustaa eri lentokenttien välillä ja saavuttaa kah-deksan eri säätilaa aiheuttaen mahdollisimman vähän CO2-päästöjä. Peli määrittää pelaajalle CO2-päästöjen ylärajan. Lentokenttien välillä matkustetaan syöttämällä lentokenttien ICAO-koodeja. Pelaajan saa-puessa kohteeseen pelaajan on mahdollista saavuttaa uusi säätila ja mikäli säätila on jo saavutettu aikaisemmin pelaaja ei kerää kyseistä säätilaa uudelleen vaan joutuu siirtymään seuraavaan kohteeseen. Jokaisella lennolla pelaajan CO2-kapasiteetti pienenee riippuen mat-kan pituudesta sekä lentokoneen mallista, joka määräytyy matkan pi-tuuden mukaan. Jos CO2-päästöt ylittyvät peli loppuu (game over), joka tarkoittaa, että peli on hävitty ja pelaaja joutuu aloittamaan alusta. Pelaajalla on kuitenkin mahdollisuus ostaa lisää CO2-kapasiteettia ansaitsemallaan rahalla, jonka avulla hän pystyy mahdollisesti lentä-mään lisää. Pelaajan rahan määrä kasvaa aina 50 dollarilla uuden säätilan keräämisen myötä. 50 dollarin pelaaja voi vaihtaa 25 kilo-grammaan CO2-kapasiteettia. Kun pelaaja tavoittaa säätilat ylittämättä CO2-kapasiteettia, läpäisee hän pelin. Lopussa käyttämätön raha muutetaan CO2-kapasiteetiksi ja miinustetaan aiheutetuista päästöis-tä, jolloin sijoituslistan järjestys saattaa vielä muuttua. Tämän jälkeen ohjelma tulostaa pelaajalle hänen saavutuksensa pelin sijoituslistaan muita pelaajia vastaan. Sijoituslista järjestää pelaajat hiilidioksidipääs-töjen mukaan: ensimmäinen sijoitus pienin CO2 kulutus + kahdeksan säätilaa. 

<img width="1023" alt="Nayttokuva_2022-11-28_kello_17 34 24" src="https://user-images.githubusercontent.com/111856755/204318560-b9dbf273-4f0d-4889-9d5f-2413a45a28df.png">

## Toiminnalliset vaatimukset

Käyttäjä aloittaa pelin, jolloin käyttäjälle annetaan kaksi vaihtoehtoa. Käyttäjä joko luo uuden käyttäjän keksimällään käyttäjätunnuksella tai jatkaa pelaamista jo aikaisemmin luodulla käyttäjällä. Pelaaja siis joko kirjautuu sisään tai luo uuden käyttäjän.
Pelaaja valitsee uuden käyttäjän, jolloin ohjelma kysyy pelaajalta käyt-täjänimen ja käyttäjänimi tallentuu tietokantaan. Pelaaja määrittää pe-lille sen aloitussijainnin (airport.scheduled_service), ja ohjelma näyttää pelin ohjeet sekä säännöt. Kaikki peliin liittyvä tieto ja info on pelaajan saatavilla sivupalkista läpi pelin. Jos pelaaja valitsee vanhan käyttäjän ja kirjautuu sisälle, hänelle tulostetaan tietokannan avulla jo saavutetut säätilat ja jäljellä olevan CO2-päästökiintiö. Tämän jälkeen ohjelma antaa pelaajalle kolme vaihtoehtoa. 1. Ohjeet 2. Jatka viimeisintä suo-rituskertaa 3. Aloita alusta. 
Kun pelaaja on valinnut käyttäjätyypin hän voi aloittaa säätilojen ke-ruun pelille asettamastaan aloitussijainnista. Kohteisiin matkustetaan syöttämällä peliin halutun lentoaseman ICAO-koodi. Kunkin kohtee-seen siirtymisen jälkeen ohjelma kertoo pelaajalle jäljellä olevan hiilidi-oksidimäärän pelin hiilidioksidipäästökapasiteetista. Pelaajalla on aina mahdollisuus tallentaa ja lopettaa peli pelisuorituksen aikana. Jos pe-laaja kerää uuden säätilan hänelle tallentuu +50$ joka vastaa -25kg CO2. Jos pelaajan hiilidioksidikiintiö on loppumassa, voi hän muuntaa lompakossa ansaitsemansa rahansa CO2-kiintiöksi. Jos pelaaja ylit-tää asetetun CO2-rajan peli loppuu (game over). Lopussa peli näyttää pelaajalle saavutetut säätilat. Jos pelaaja saavuttaa kaikki kahdeksan säätilaa ylittämättä asetettua CO2-rajaa hän voittaa pelin. 


## Laadulliset vaatimukset
Pelaaja saa tiedon kuluttamastaan CO2-päästöistä sekä jäljellä ole-vasta CO2 määrästä. Pelaajan on saatava välitön palaute jokaisesta tekemästään toimenpiteestä. Peli toimii virheettömästi ja pelaaja ei pysty antamaan virheellistä syöttöä niin, että peli lakkaisi toimimasta vaan mahdolliset virhesyötöt ovat otettu huomioon. Pelaaja näkee se-laimessa graafisen satelliittikartan. Ulkoasu selaimessa on ymmärret-tävä ja siisti. Pelin toinen API tuo realistista dataa säätilasta pelaajan syöttämästä kohteesta. Kestävä kehitys on huomioitu sekä pelin sisäl-lössä, että koodissa. Käyttäjiä kehotetaan liikkumaan mahdollisimman vähillä hiilidioksidipäästöillä sekä ohjelmointiryhmä ymmärtää, ettei pe-lin taustapalvelukieli (Python, energy 75.88 (huom. JavaScript 4.45)) ole niin vihreää koodia kuin olisi mahdollista.

## Poikkeavat suorituspolut

1.	Pelaaja kirjautuu sisään tai tekee uuden käyttäjän ja syöttää aloi-tuslentokentän ICAO-koodin. Vanha käyttäjä kirjautuu sisään ja joko jatkaa viimeisintä suorituskertaa tai aloittaa pelin alusta.
2.	Pelaaja syöttää lentokenttien ICAO-koodeja peliin ja saa ilmoi-tuksen kohteen senhetkisestä säätilasta.
3.	Jos säätila vastaa yhtä kahdeksasta tavoitellusta säätilasta ja käyttäjällä ei sitä vielä ole, kerää hän uuden säätilan ja ansaitsee 50 dollaria.
4.	Pelaaja toistaa kohtaa 3 niin kauan kun kahdeksan säätilaa on tavoitettu tai pelaajan hiilidioksidipäästökiintiö ylittyy.
5.	Pelaaja voi halutessaan muuttaa ansaitsemansa valuutan hiili-dioksidikiintiöksi. Pelaajan tulee kuitenkin tehdä tämä ennen pe-lin loppumista.
6.	Lopussa pelaaja näkee viimeisen pelikierroksen sijoituksensa si-joituslistassa.



## Tietokannan rakenne
![lentopeliRelaatio (1)](https://user-images.githubusercontent.com/111856849/193352889-548ed744-4220-45e3-b214-606fbb93b933.png)

# Uudet Ominaisuudet
![Aicrafttoteutus](https://user-images.githubusercontent.com/111856849/204092352-3a8ed1b7-1487-475e-b7f1-31857b429b47.png)
![CO2OSTO](https://user-images.githubusercontent.com/111856849/204092361-de95f5a2-7d63-43bd-8def-8b7563de0f06.png)
![Round1](https://user-images.githubusercontent.com/111856849/204092371-7cd7c468-020d-4e20-8812-753df4c94cb4.png)
