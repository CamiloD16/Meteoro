from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def registro():
    weather_url_bogota = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?id=3688689&appid=f62b4de10d24119e0ef2a24f0cea1158"
    )
    weather_url_tokyo = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?id=1850147&appid=f62b4de10d24119e0ef2a24f0cea1158"
    )

    weather_data_bogota = weather_url_bogota.json()
    weather_data_tokyo = weather_url_tokyo.json()

    temp_bogota = round(weather_data_bogota["main"]["temp"]) - 273.15
    temp_tokyo = round(weather_data_tokyo["main"]["temp"]) - 273.15

    # city = request.form["city"]
    if request.method == "POST":
        city = request.form["city"]

        # humidity = weather_data["main"]["humidity"]
        # wind_speed = weather_data["wind"]["speed"]

        return render_template(
            "index.html", city=city, temp_bogota=temp_bogota, temp_tokyo=temp_tokyo
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
