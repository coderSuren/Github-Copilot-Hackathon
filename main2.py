""" fetch weather data from openweathermap.org and display weather data based on user input """

import requests

from datetime import datetime

from config import API_KEY

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

def display_weather_data(data):
    """ display weather data based on user input """
    if data['cod'] == '404':
        print('City not found')
    else:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
        print(f'Weather data for {city}, {country}:')
        print(f'Temperature: {temp}°C')
        print(f'Feels like: {feels_like}°C')
        print(f'Minimum temperature: {temp_min}°C')
        print(f'Maximum temperature: {temp_max}°C')
        print(f'Pressure: {pressure} hPa')
        print(f'Humidity: {humidity}%')
        print(f'Wind speed: {wind_speed} m/s')
        print(f'Wind direction: {wind_deg}°')
        print(f'Sunrise: {sunrise}')
        print(f'Sunset: {sunset}')

def main():
    """ main function """
    city = input('Enter city: ')
    data = get_weather_data(city)
    display_weather_data(data)

if __name__ == '__main__':
    main()

