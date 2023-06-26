from datetime import datetime
from prettytable import PrettyTable
        
import json


def to_json(data,args):
    """ store weather data in json format """
    dictionary = {
        "weather":[]
    }

    if args.forecast:
        for city in data:
            for i in city['list']: 
                dictionary['weather'].append({
                    'date':datetime.fromtimestamp(i['dt']).strftime('%Y-%m-%d %H:%M:%S'),
                    'description':i['weather'][0]['description'],
                    'temperature':i['main']['temp'],
                    'pressure':i['main']['pressure'],
                    'humidity':i['main']['humidity'],
                    'wind_speed':i['wind']['speed'],
                    'wind_direction':i['wind']['deg']
                })
    else:
        for city in data:
            dictionary['weather'].append({
                'date':datetime.fromtimestamp(city['dt']).strftime('%Y-%m-%d %H:%M:%S'),
                'description':city['weather'][0]['description'],
                'temperature':city['main']['temp'],
                'pressure':city['main']['pressure'],
                'humidity':city['main']['humidity'],
                'wind_speed':city['wind']['speed'],
                'wind_direction':city['wind']['deg']
            })

    path=args.store+".json"
    with open(path, "w") as outfile:
        json.dump(dictionary, outfile)

def to_csv(data):
        pass

def display_weather_data(data, city, args):
    if data['cod'] == '404':
            print(f'\nWeather data for {city} not found')
            return
    else:
        """ display weather description """
        print(f'\nWeather data for {data["name"]}, {data["sys"]["country"]}:')
        print(f'Weather description: {data["weather"][0]["description"]}')
    
    if args.temperature:
        print(f'Temperature: {data["main"]["temp"]}°C')
    if args.pressure:
        print(f'Pressure: {data["main"]["pressure"]} hPa')
    if args.humidity:
        print(f'Humidity: {data["main"]["humidity"]}%')
    if args.wind:
        print(f'Wind speed: {data["wind"]["speed"]} m/s')
        print(f'Wind direction: {data["wind"]["deg"]}°')

    if args.sun:
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
        print(f'Sunrise: {sunrise}')
        print(f'Sunset: {sunset}')
    print()

def display_full_weather_data(data):
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
        print()

def display_weather_history(data,args):
     
    if data['cod'] == '404':
        print('City not found')
    else:
        city = data['city']['name']
        country = data['city']['country']
        print(f'Weather forecast of {city}, {country} for next 5 days:')
        """use prettytable to display data in tabular format"""
        table = PrettyTable()
        fields=['Date', 'Description']
        """change append to extend to add multiple items to list"""
        if args.temperature:
            fields.append('Temperature')
        if args.pressure:
            fields.append('Pressure')
        if args.humidity:
            fields.append('Humidity')
        if args.wind:
            fields.append('Wind speed')
            fields.append('Wind direction')
        if args.all:
            fields=['Date', 'Description','Temperature','Pressure','Humidity','Wind speed','Wind direction']
        table.field_names = fields

        # print(table.field_names)
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S')
            temperature = item['main']['temp']
            description = item['weather'][0]['description']
            Pressure=item['main']['pressure']
            Humidity=item['main']['humidity']
            Wind_speed=item['wind']['speed']
            Wind_direction=item['wind']['deg']
            row = [date,description]
            if args.temperature:
                row.append(temperature)
            if args.pressure:
                row.append(Pressure)
            if args.humidity:
                row.append(Humidity)
            if args.wind:
                row.append(Wind_speed)
                row.append(Wind_direction)
            if args.all:
                row=[date,description,temperature,Pressure,Humidity,Wind_speed,Wind_direction]
            table.add_row(row)
            
        print(table)
