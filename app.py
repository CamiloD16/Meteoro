from flask import Flask, render_template, request
import requests
import json
from datetime import date
from datetime import timedelta

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():
    today = date.today()
    tomorrow = today + timedelta(days=1)
    overmorrow = tomorrow + timedelta(days=1)

    weather_url_bogota = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?id=3688689&appid=f62b4de10d24119e0ef2a24f0cea1158"
    )
    weather_url_tokyo = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?id=1850147&appid=f62b4de10d24119e0ef2a24f0cea1158"
    )
    weather_url_paris = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?id=2968815&appid=f62b4de10d24119e0ef2a24f0cea1158"
    )
    weather_url_miami = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?id=4164138&appid=f62b4de10d24119e0ef2a24f0cea1158"
    )

    weather_data_bogota = weather_url_bogota.json()
    weather_data_tokyo = weather_url_tokyo.json()
    weather_data_paris = weather_url_paris.json()
    weather_data_miami = weather_url_miami.json()

    temp_bogota = int(round(weather_data_bogota["main"]["temp"]) - 273.15)
    temp_tokyo = int(round(weather_data_tokyo["main"]["temp"]) - 273.15)
    temp_paris = int(round(weather_data_paris["main"]["temp"]) - 273.15)
    temp_miami = int(round(weather_data_miami["main"]["temp"]) - 273.15)

    if request.method == "POST":
        city = request.form["city"]
        # INFORMACION CLIMATICA HOY
        weather_url_city_today = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f62b4de10d24119e0ef2a24f0cea1158"
        )
        weather_data_city_today = weather_url_city_today.json()
        temp_city_today = int((round(weather_data_city_today["main"]["temp"]) - 273.15))
        feelslike_city_today = int(
            (round(weather_data_city_today["main"]["feels_like"]) - 273.15)
        )
        humidity_city_today = int((round(weather_data_city_today["main"]["humidity"])))
        main_city_today = weather_data_city_today["weather"][0]["main"]
        icon_city_today = weather_data_city_today["weather"][0]["icon"]

        # INFORMACION CLIMATICA GENERAL Y GRAFICAS CHART JS
        weather_url_city = requests.get(
            f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=f62b4de10d24119e0ef2a24f0cea1158"
        )
        weather_data_city = weather_url_city.json()

        # Sensación términa hoy, mañana y pasado
        feels_like_day_1 = int(
            round(weather_data_city_today["main"]["feels_like"]) - 273.15
        )
        feels_like_day_2 = int(
            round(weather_data_city["list"][2]["main"]["feels_like"]) - 273.15
        )
        feels_like_day_3 = int(
            round(weather_data_city["list"][10]["main"]["feels_like"]) - 273.15
        )
        # temperatura minima hoy, mañana y pasado
        temp_min_day_1 = int(
            round(weather_data_city_today["main"]["temp_min"]) - 273.15
        )
        temp_min_day_2 = int(
            round(weather_data_city["list"][2]["main"]["temp_min"]) - 273.15
        )
        temp_min_day_3 = int(
            round(weather_data_city["list"][10]["main"]["temp_min"]) - 273.15
        )
        # temperatura maxima hoy, mañana y pasado
        temp_max_day_1 = int(
            round(weather_data_city_today["main"]["temp_max"]) - 273.15
        )
        temp_max_day_2 = int(
            round(weather_data_city["list"][2]["main"]["temp_max"]) - 273.15
        )
        temp_max_day_3 = int(
            round(weather_data_city["list"][10]["main"]["temp_max"]) - 273.15
        )
        # Mañana hora 6 am
        temp_city_1 = int(
            (round(weather_data_city["list"][2]["main"]["temp"]) - 273.15)
        )
        main_city_1 = weather_data_city["list"][2]["weather"][0]["main"]
        icon_city_1 = weather_data_city["list"][2]["weather"][0]["icon"]
        day_city_1 = weather_data_city["list"][2]["dt_txt"]
        # Mañana hora 12 pm
        temp_city_2 = int(
            (round(weather_data_city["list"][4]["main"]["temp"]) - 273.15)
        )
        main_city_2 = weather_data_city["list"][4]["weather"][0]["main"]
        icon_city_2 = weather_data_city["list"][4]["weather"][0]["icon"]
        day_city_2 = weather_data_city["list"][4]["dt_txt"]
        # Mañana hora 6pm
        temp_city_3 = int(
            (round(weather_data_city["list"][6]["main"]["temp"]) - 273.15)
        )
        main_city_3 = weather_data_city["list"][6]["weather"][0]["main"]
        icon_city_3 = weather_data_city["list"][6]["weather"][0]["icon"]
        day_city_3 = weather_data_city["list"][6]["dt_txt"]
        # Pasado hora 6 am
        temp_city_4 = int(
            (round(weather_data_city["list"][10]["main"]["temp"]) - 273.15)
        )
        main_city_4 = weather_data_city["list"][10]["weather"][0]["main"]
        icon_city_4 = weather_data_city["list"][10]["weather"][0]["icon"]
        day_city_4 = weather_data_city["list"][10]["dt_txt"]
        # Pasado hora 12 pm
        temp_city_5 = int(
            (round(weather_data_city["list"][12]["main"]["temp"]) - 273.15)
        )
        main_city_5 = weather_data_city["list"][12]["weather"][0]["main"]
        icon_city_5 = weather_data_city["list"][12]["weather"][0]["icon"]
        day_city_5 = weather_data_city["list"][12]["dt_txt"]
        # Pasado hora 6pm
        temp_city_6 = int(
            (round(weather_data_city["list"][14]["main"]["temp"]) - 273.15)
        )
        main_city_6 = weather_data_city["list"][14]["weather"][0]["main"]
        icon_city_6 = weather_data_city["list"][14]["weather"][0]["icon"]
        day_city_6 = weather_data_city["list"][14]["dt_txt"]

        return render_template(
            "index.html",
            city=city,
            temp_bogota=temp_bogota,
            temp_tokyo=temp_tokyo,
            temp_paris=temp_paris,
            temp_miami=temp_miami,
            today=today,
            tomorrow=tomorrow,
            overmorrow=overmorrow,
            temp_city_today=temp_city_today,
            feelslike_city_today=feelslike_city_today,
            main_city_today=main_city_today,
            icon_city_today=icon_city_today,
            humidity_city_today=humidity_city_today,
            temp_city_1=temp_city_1,
            main_city_1=main_city_1,
            icon_city_1=icon_city_1,
            day_city_1=day_city_1,
            temp_city_2=temp_city_2,
            main_city_2=main_city_2,
            icon_city_2=icon_city_2,
            day_city_2=day_city_2,
            temp_city_3=temp_city_3,
            main_city_3=main_city_3,
            icon_city_3=icon_city_3,
            day_city_3=day_city_3,
            temp_city_4=temp_city_4,
            main_city_4=main_city_4,
            icon_city_4=icon_city_4,
            day_city_4=day_city_4,
            temp_city_5=temp_city_5,
            main_city_5=main_city_5,
            icon_city_5=icon_city_5,
            day_city_5=day_city_5,
            temp_city_6=temp_city_6,
            main_city_6=main_city_6,
            icon_city_6=icon_city_6,
            day_city_6=day_city_6,
            feels_like_day_1=feels_like_day_1,
            feels_like_day_2=feels_like_day_2,
            feels_like_day_3=feels_like_day_3,
            temp_min_day_1=temp_min_day_1,
            temp_min_day_2=temp_min_day_2,
            temp_min_day_3=temp_min_day_3,
            temp_max_day_1=temp_max_day_1,
            temp_max_day_2=temp_max_day_2,
            temp_max_day_3=temp_max_day_3,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
