#!/usr/bin/env python3

import json
import urllib.request

# sign in at https://openweathermap.org/api to get an API KEY
APPID = "xxx"

# get you city ID at http://bulk.openweathermap.org/sample/
CITYID = "2968815"

# {
#     "coord": {
#         "lon": 2.3486,
#         "lat": 48.853401
#     },
#     "weather": [
#         {
#             "id": 804,
#             "main": "Clouds",
#             "description": "overcast clouds",
#             "icon": "04n"
#         }
#     ],
#     "base": "stations",
#     "main": {
#         "temp": 17.53,
#         "feels_like": 17.58,
#         "temp_min": 16,
#         "temp_max": 19.44,
#         "pressure": 1019,
#         "humidity": 72
#     },
#     "visibility": 10000,
#     "wind": {
#         "speed": 1,
#         "deg": 280
#     },
#     "clouds": {
#         "all": 94
#     },
#     "dt": 1592597109,
#     "sys": {
#         "type": 1,
#         "id": 6547,
#         "country": "FR",
#         "sunrise": 1592538405,
#         "sunset": 1592596757
#     },
#     "timezone": 7200,
#     "id": 2968815,
#     "name": "Paris",
#     "cod": 200
# }
with urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?id=" + CITYID + "&units=metric&appid=" + APPID) as url:
  data = json.loads(url.read().decode())
  str = " " + str(data['main']['temp']) + "°C "
  # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
  if int(data['weather'][0]['id']) >= 200 and int(data['weather'][0]['id']) < 300: # Group 2xx: Thunderstorm
    str += "" # yes, it's a thunder poo ;)
  elif int(data['weather'][0]['id']) >= 300 and int(data['weather'][0]['id']) < 500: # Group 3xx: Drizzle
    str += ""
  elif int(data['weather'][0]['id']) >= 500 and int(data['weather'][0]['id']) < 600: # Group 5xx: Rain
    str += ""
  elif int(data['weather'][0]['id']) >= 600 and int(data['weather'][0]['id']) < 700: # Group 6xx: Snow
    str += ""
  elif int(data['weather'][0]['id']) >= 700 and int(data['weather'][0]['id']) < 800: # Group 7xx: Atmosphere
    str += ""
  elif int(data['weather'][0]['id']) == 800: # Group 800: Clear
    str += ""
  elif int(data['weather'][0]['id']) > 800: # Group 80x: Clouds
    str += ""
  print(str, end='')
