import requests
import os 
api_key=os.environ.get('OPENWEATHER_API_KEY')
city_entered= input("Enter a city : ")
print(city_entered)