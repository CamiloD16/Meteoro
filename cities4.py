import requests

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
