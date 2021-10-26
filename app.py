from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

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

    temp_bogota = round(weather_data_bogota["main"]["temp"]) - 273.15
    temp_tokyo = round(weather_data_tokyo["main"]["temp"]) - 273.15
    temp_paris = round(weather_data_paris["main"]["temp"]) - 273.15
    temp_miami = round(weather_data_miami["main"]["temp"]) - 273.15

    if request.method == "POST":
        city = request.form["city"]
        weather_url_city = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f62b4de10d24119e0ef2a24f0cea1158"
        )
        weather_data_city = weather_url_city.json()
        temp_city = round(weather_data_city["main"]["temp"]) - 273.15

        return render_template(
            "index.html",
            city=city,
            temp_bogota=temp_bogota,
            temp_tokyo=temp_tokyo,
            temp_paris=temp_paris,
            temp_miami=temp_miami,
            temp_city=temp_city,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
