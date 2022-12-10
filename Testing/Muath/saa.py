# (1,'HOT','Temperature over +25C','01d','TEMP',25.00,9999.00,NULL),

lista = ["thunderstorm with light rain", "thunderstorm with rain", "thunderstorm with heavy rain", "light thunderstorm", "thunderstorm", "heavy thunderstorm", "ragged thunderstorm", "thunderstorm with light drizzle", "thunderstorm with drizzle", "thunderstorm with heavy drizzle"]
lista1 = ["light intensity drizzle", "drizzle", "heavy intensity drizzle", "light intensity drizzle rain", "drizzle rain", "heavy intensity drizzle rain", "shower rain and drizzle", "heavy shower rain and drizzle", "shower drizzle"]
rain = ["light rain", "moderate rain", "heavy intensity rain", "very heavy rain",
        "extreme rain", "freezing rain", "light intensity shower rain", "shower rain", "heavy intensity shower rain", "ragged shower rain"]
snow = ["light snow", "Snow", "Heavy snow", "Sleet",
        "Light shower sleet", "Shower sleet", "Light rain and snow", "Rain and snow", "Light shower snow", "Shower snow", "Heavy shower snow"]

clouds = ["few clouds: 11-25%", "scattered clouds: 25-50%", "broken clouds: 51-84%", "overcast clouds: 85-100%"]
clear = ["clear sky"]

isa = ["mist", "Smoke", "Haze", "sand/ dust whirls",
        "fog", "sand", "dust", "volcanic ash", "squalls", "tornado"]
id = 46

for i in isa:
    lause = f"({id},'Phenomenon','{i}'),"
    id = id + 1
    print(lause)