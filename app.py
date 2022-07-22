from flask import (
    Flask,
    render_template,
    request,
    redirect,
)
import requests
from datetime import date, timedelta
from cities4 import temp_bogota, temp_tokyo, temp_paris, temp_miami
from infSection2 import (
    main_city_init,
    icon_city_init,
    day_city_init,
    city_init,
    temp_city_today_init,
    temp_max_city_today_init,
    temp_min_city_today_init,
    humidity_city_today_init,
    feelslike_city_today_init,
    main_city_today_init,
    icon_city_today_init,
    temp_city_init,
    temp_min_day_init,
    temp_max_day_init,
    feels_like_day_init,
    co_init,
    no_init,
    no2_init,
    o3_init,
    so2_init,
    pm2_5_init,
    pm10_init,
    nh3_init,
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

    today = date.today()
    tomorrow = today + timedelta(days=1)
    overmorrow = tomorrow + timedelta(days=1)
    day3 = overmorrow + timedelta(days=1)
    day4 = day3 + timedelta(days=1)
    day5 = day4 + timedelta(days=1)

    if request.method == "POST":
        if "submit_button_1" in request.form:
            city = request.form["city"]
            # # INFORMACION CLIMATICA HOY
            weather_url_city_today = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=es&appid=f62b4de10d24119e0ef2a24f0cea1158"
            )
            weather_data_city_today = weather_url_city_today.json()
            fail = False
            if weather_data_city_today["cod"] != 200:
                weather_url_city_today = requests.get(
                    f"http://api.openweathermap.org/data/2.5/weather?q=bogota&lang=es&appid=f62b4de10d24119e0ef2a24f0cea1158"
                )
                weather_data_city_today = weather_url_city_today.json()
                fail = True
            if city.upper() in weather_data_city_today["name"].upper():
                city = weather_data_city_today["name"]
            else:
                city = "BOGOTA"

            temp_city_today = int(
                (round(weather_data_city_today["main"]["temp"]) - 273.15)
            )
            feelslike_city_today = int(
                (round(weather_data_city_today["main"]["feels_like"]) - 273.15)
            )
            temp_max_city_today = int(
                round(weather_data_city_today["main"]["temp_max"]) - 273.15
            )
            temp_min_city_today = int(
                round(weather_data_city_today["main"]["temp_min"]) - 273.15
            )
            humidity_city_today = int(
                (round(weather_data_city_today["main"]["humidity"]))
            )
            main_city_today = weather_data_city_today["weather"][0]["description"]
            icon_city_today = weather_data_city_today["weather"][0]["icon"]

            # INFORMACION GENERAL SOBRE LA CONTAMINACION DEL AIRE

            latitud = float(weather_data_city_today["coord"]["lat"])
            longitud = float(weather_data_city_today["coord"]["lon"])
            inf_url_city_air = requests.get(
                f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitud}&lon={longitud}&appid=f62b4de10d24119e0ef2a24f0cea1158"
            )
            inf_city_air = inf_url_city_air.json()
            co = inf_city_air["list"][0]["components"]["co"]
            no = inf_city_air["list"][0]["components"]["no"]
            no2 = inf_city_air["list"][0]["components"]["no2"]
            o3 = inf_city_air["list"][0]["components"]["o3"]
            so2 = inf_city_air["list"][0]["components"]["so2"]
            pm2_5 = inf_city_air["list"][0]["components"]["pm2_5"]
            pm10 = inf_city_air["list"][0]["components"]["pm10"]
            nh3 = inf_city_air["list"][0]["components"]["nh3"]
            # INFORMACION CLIMATICA GENERAL Y GRAFICAS CHART JS
            weather_url_city = requests.get(
                f"http://api.openweathermap.org/data/2.5/forecast?q={city}&lang=es&appid=f62b4de10d24119e0ef2a24f0cea1158"
            )
            weather_data_city = weather_url_city.json()
            main_city = []
            icon_city = []
            day_city = []
            temp_city = []
            temp_min_day = []
            temp_max_day = []
            feels_like_day = []

            for j in range(5, 40, 2):
                if j != 11 and j != 19 and j != 27 and j != 35:
                    main_city.append(
                        weather_data_city["list"][j]["weather"][0]["description"]
                    )
                    icon_city.append(weather_data_city["list"][j]["weather"][0]["icon"])
                    day_city.append(weather_data_city["list"][j]["dt_txt"])
                    temp_city.append(
                        int(
                            (
                                round(weather_data_city["list"][j]["main"]["temp"])
                                - 273.15
                            )
                        )
                    )
                    temp_min_day.append(
                        int(
                            round(weather_data_city["list"][j]["main"]["temp_min"])
                            - 273.15
                        )
                    )
                    temp_max_day.append(
                        int(
                            round(weather_data_city["list"][j]["main"]["temp_max"])
                            - 273.15
                        )
                    )
                    feels_like_day.append(
                        int(
                            round(weather_data_city["list"][j]["main"]["feels_like"])
                            - 273.15
                        )
                    )

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
                co=co,
                no=no,
                no2=no2,
                o3=o3,
                so2=so2,
                pm2_5=pm2_5,
                pm10=pm10,
                nh3=nh3,
                day3=day3,
                day4=day4,
                day5=day5,
                fail=fail,
            )

    return render_template(
        "index.html",
        today=today,
        tomorrow=tomorrow,
        overmorrow=overmorrow,
        day3=day3,
        day4=day4,
        day5=day5,
        city=city_init,
        main_city=main_city_init,
        icon_city=icon_city_init,
        day_city=day_city_init,
        temp_city=temp_city_init,
        temp_bogota=temp_bogota,
        temp_tokyo=temp_tokyo,
        temp_paris=temp_paris,
        temp_miami=temp_miami,
        temp_city_today=temp_city_today_init,
        feelslike_city_today=feelslike_city_today_init,
        temp_max_city_today=temp_max_city_today_init,
        temp_min_city_today=temp_min_city_today_init,
        humidity_city_today=humidity_city_today_init,
        main_city_today=main_city_today_init,
        icon_city_today=icon_city_today_init,
        temp_min_day=temp_min_day_init,
        temp_max_day=temp_max_day_init,
        feels_like_day=feels_like_day_init,
        co=co_init,
        no=no_init,
        no2=no2_init,
        o3=o3_init,
        so2=so2_init,
        pm2_5=pm2_5_init,
        pm10=pm10_init,
        nh3=nh3_init,
    )


@app.route("/conocenos", methods=["GET", "POST"])
def project():
    return render_template("knowUs.html")


@app.route("/contactanos", methods=["GET", "POST"])
def contactUs():
    if request.method == "POST":
        return redirect("mailto:meteoroweather@gmail.com")
    return render_template("contactUs.html")


if __name__ == "__main__":
    app.run(debug=True)
