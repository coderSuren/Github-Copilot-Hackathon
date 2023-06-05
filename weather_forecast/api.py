""" fetch weather data from openweathermap.org and display weather data based on user input """

import requests
from weather_forecast.config import API_KEY

def get_weather_data(city):
    """ fetch weather data from openweathermap.org """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

""" function to get 5 day weather history from openweathermap.org """

def get_weather_history(city):
    """ fetch weather history from openweathermap.org """
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()
