import requests

city_init = "bogota"
weather_url_city = requests.get(
    f"http://api.openweathermap.org/data/2.5/forecast?q={city_init}&lang=es&appid=f62b4de10d24119e0ef2a24f0cea1158"
)
weather_data_city = weather_url_city.json()
main_city_init = []
icon_city_init = []
day_city_init = []
temp_city_init = []
for j in range(5, 40, 2):
    if j != 11 and j != 19 and j != 27 and j != 35:
        main_city_init.append(weather_data_city["list"][j]["weather"][0]["description"])
        icon_city_init.append(weather_data_city["list"][j]["weather"][0]["icon"])
        day_city_init.append(weather_data_city["list"][j]["dt_txt"])
        temp_city_init.append(
            int((round(weather_data_city["list"][j]["main"]["temp"]) - 273.15))
        )

##TODAY
weather_url_city_today = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={city_init}&lang=es&appid=f62b4de10d24119e0ef2a24f0cea1158"
)
weather_data_city_today = weather_url_city_today.json()

temp_city_today_init = int((round(weather_data_city_today["main"]["temp"]) - 273.15))
feelslike_city_today_init = int(
    (round(weather_data_city_today["main"]["feels_like"]) - 273.15)
)
temp_max_city_today_init = int(
    round(weather_data_city_today["main"]["temp_max"]) - 273.15
)
temp_min_city_today_init = int(
    round(weather_data_city_today["main"]["temp_min"]) - 273.15
)
humidity_city_today_init = int((round(weather_data_city_today["main"]["humidity"])))
main_city_today_init = weather_data_city_today["weather"][0]["description"]
icon_city_today_init = weather_data_city_today["weather"][0]["icon"]


##SECTION 04/11/2012
temp_min_day_init = []
temp_max_day_init = []
feels_like_day_init = []
for j in range(5, 40, 2):
    if j != 11 and j != 19 and j != 27 and j != 35:
        temp_min_day_init.append(
            int(round(weather_data_city["list"][j]["main"]["temp_min"]) - 273.15)
        )
        temp_max_day_init.append(
            int(round(weather_data_city["list"][j]["main"]["temp_max"]) - 273.15)
        )
        feels_like_day_init.append(
            int(round(weather_data_city["list"][j]["main"]["feels_like"]) - 273.15)
        )
##CALIDAD DE AIRE
latitud = float(weather_data_city_today["coord"]["lat"])
longitud = float(weather_data_city_today["coord"]["lon"])
inf_url_city_air = requests.get(
    f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitud}&lon={longitud}&appid=f62b4de10d24119e0ef2a24f0cea1158"
)
inf_city_air = inf_url_city_air.json()
co_init = inf_city_air["list"][0]["components"]["co"]
no_init = inf_city_air["list"][0]["components"]["no"]
no2_init = inf_city_air["list"][0]["components"]["no2"]
o3_init = inf_city_air["list"][0]["components"]["o3"]
so2_init = inf_city_air["list"][0]["components"]["so2"]
pm2_5_init = inf_city_air["list"][0]["components"]["pm2_5"]
pm10_init = inf_city_air["list"][0]["components"]["pm10"]
nh3_init = inf_city_air["list"][0]["components"]["nh3"]
