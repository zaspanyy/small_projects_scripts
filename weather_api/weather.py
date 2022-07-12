import requests
import pandas as pd
from pandas.io.json import json_normalize
import json

weather_key = "API_key"
weather_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Please input city name: ")

api_call = f"{weather_url}?q={city}&appid={weather_key}&units=metric&lang=pl"

response = requests.get(api_call)

if response.status_code == 200:
    data = response.json()
    df_all_current_weather = pd.DataFrame()


    current_time = []
    city = []
    country = []
    temperature = []
    temperature_feel = []
    temperature_min = []
    temperature_max = []
    pressure = []
    humidity = []
    main_description = []
    clouds = []
    wind_speed = []

    current_time.append(pd.Timestamp.now())
    city.append(data['name'])
    country.append(data['sys']['country'])
    temperature.append(data['main']['temp'])
    temperature_feel.append(data['main']['feels_like'])
    temperature_min.append(data['main']['temp_min'])
    temperature_max.append(data['main']['temp_max'])
    pressure.append(data['main']['pressure'])
    humidity.append(data['main']['humidity'])
    main_description.append(data['weather'][0]['description'])
    clouds.append(data['clouds']['all'])
    wind_speed.append(data['wind']['speed'])
    
    df_all_current_weather['current_time'] = current_time
    df_all_current_weather['city'] = city
    df_all_current_weather['country'] = country
    df_all_current_weather['temperature'] = temperature
    df_all_current_weather['temperature_feel'] = temperature_feel
    df_all_current_weather['temperature_min'] = temperature_min
    df_all_current_weather['temperature_max'] = temperature_max
    df_all_current_weather['pressure'] = pressure
    df_all_current_weather['humidity'] = humidity
    df_all_current_weather['main_description'] = main_description
    df_all_current_weather['clouds'] = clouds
    df_all_current_weather['wind_speed'] = wind_speed



    
    print(df_all_current_weather)