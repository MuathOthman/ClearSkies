import requests

url = "http://127.0.0.1:4000/kentta/"
kaupunki = input("Anna kaupunki: ")
koko_url = url + kaupunki
print(koko_url)
print(f"{kaupunki}'s weather:")

try:
    vastaus = requests.get(koko_url)
    if vastaus.status_code==200:
        print(koko_url)
        vastaus_json = vastaus.json()
        #print(vastaus_json["weather"])
        for i in vastaus_json["weather"]:
            #print(i["main"])
            print(f"Description: {i['main']}")
        temprature = (vastaus_json['main']['temp']- 273.15)
        print(f"Temprature: {int(temprature)} °C")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")