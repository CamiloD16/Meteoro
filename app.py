from flask import Flask, render_template, request
import requests
import json
from datetime import date, timedelta
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "123"
app.config["MYSQL_DATABASE_DB"] = "climadb"
mysql.init_app(app)


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
        temp_max_city_today = int(
            round(weather_data_city_today["main"]["temp_max"]) - 273.15
        )
        temp_min_city_today = int(
            round(weather_data_city_today["main"]["temp_min"]) - 273.15
        )
        humidity_city_today = int((round(weather_data_city_today["main"]["humidity"])))
        main_city_today = weather_data_city_today["weather"][0]["main"]
        icon_city_today = weather_data_city_today["weather"][0]["icon"]

        # INFORMACION CLIMATICA GENERAL Y GRAFICAS CHART JS
        weather_url_city = requests.get(
            f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=f62b4de10d24119e0ef2a24f0cea1158"
        )
        weather_data_city = weather_url_city.json()

        main_city = []
        icon_city = []
        day_city = []
        temp_city = []
        temp_min_day = []
        temp_max_day = []
        feels_like_day = []

        for j in range(2, 40, 2):
            if j <= 7 or j >= 9:
                main_city.append(weather_data_city["list"][j]["weather"][0]["main"])
                icon_city.append(weather_data_city["list"][j]["weather"][0]["icon"])
                day_city.append(weather_data_city["list"][j]["dt_txt"])
                temp_city.append(
                    int((round(weather_data_city["list"][j]["main"]["temp"]) - 273.15))
                )
                temp_min_day.append(
                    int(
                        round(weather_data_city["list"][j]["main"]["temp_min"]) - 273.15
                    )
                )
                temp_max_day.append(
                    int(
                        round(weather_data_city["list"][j]["main"]["temp_max"]) - 273.15
                    )
                )
                feels_like_day.append(
                    int(
                        round(weather_data_city["list"][j]["main"]["feels_like"])
                        - 273.15
                    )
                )

        cur1 = mysql.connect().cursor()
        cur1.execute("DELETE FROM tabla_temp")

        cur2 = mysql.connect().cursor()
        for i in range(len(temp_city)):
            cur2.execute(
                "INSERT INTO tabla_temp"
                "(fecha,temperatura,temperaturaMinima,temperaturaMaxima,sensacionTermica)"
                "VALUES (%s,%s,%s,%s,%s)",
                (
                    day_city[i],
                    temp_city[i],
                    temp_min_day[i],
                    temp_max_day[i],
                    feels_like_day[i],
                ),
            )
        cur3 = mysql.connect().cursor()
        cur3.execute("SELECT * FROM tabla_temp")

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
            temp_max_city_today=temp_max_city_today,
            main_city_today=main_city_today,
            icon_city_today=icon_city_today,
            humidity_city_today=humidity_city_today,
            temp_city=temp_city,
            main_city=main_city,
            icon_city=icon_city,
            day_city=day_city,
            feels_like_day=feels_like_day,
            temp_min_city_today=temp_min_city_today,
            temp_min_day=temp_min_day,
            temp_max_day=temp_max_day,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
