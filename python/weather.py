import requests
import os 
from dotenv import load_dotenv
load_dotenv('/Users/Asus/Desktop/console-applications/.env.local')
api_key=os.environ.get("OPENWEATHER_API_KEY")
city_entered= input("Enter a city : ")
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_entered}&units=metric&APPID={api_key}")
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    #print(weather_data.json()) (Contains all the data being fetched by the api , extract the data you want)
    print(f"The weather in {city_entered} is: {weather}")
    print(f"The temperature in {city_entered} is: {temp}ºC")