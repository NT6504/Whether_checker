import requests
import json
cityName = input("Enter your City : ")
completeURL = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=7b8ea94e8e2b733eeea9e5a5c986f12b"
response = requests.get(completeURL)
data = response.json()
kelvien_temp = (data["main"]["temp"])
celsius_temp = (kelvien_temp - 273.15)
print(celsius_temp , "°C")
