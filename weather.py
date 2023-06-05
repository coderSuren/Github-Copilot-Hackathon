""" using argparser get city input from arguments and display weather data by fetching data from openweathermap.org"""

import argparse
import main2

def main():
    """ main function """
    parser = argparse.ArgumentParser(description='Fetch weather data from openweathermap.org and display weather data based on user input', prog='weather', usage='%(prog)s city [options] ', epilog='Enjoy the program! :)', prefix_chars='-+/')
    gen = parser.add_argument_group('subcommands')
    gen.add_argument('-st', '--store', help='storing weather data in new file', action='store_true')
    parser.add_argument('city', help='city name')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-t', '--temperature', help='temperature in °C', action='store_true')
    parser.add_argument('-p', '--pressure', help='pressure in hPa', action='store_true')
    parser.add_argument('-hu', '--humidity', help='humidity in %%', action='store_true')
    parser.add_argument('-w', '--wind', help='wind speed in m/s and wind direction in °', action='store_true')
    parser.add_argument('-s', '--sun', help='sunrise and sunset time in HH:MM:SS', action='store_true')

    """add an argument to get  history data"""
    """if hi choosen get data from get_weather_history function and display it"""
    parser.add_argument('-hi', '--history', help='get 5 day weather history', action='store_true')
    args = parser.parse_args()

    if args.history:
        data = main2.get_weather_history(args.city)
        
        print(data)   
    
    a=[]
        
    d = list(args.city.split(','))
    for city in d:
        data = main2.get_weather_data(city)
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
            sunrise = main2.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
            sunset = main2.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
            print(f'Sunrise: {sunrise}')
            print(f'Sunset: {sunset}')
        if args.store:
            a.append(data)

    file_path = "args.txt"  # Specify the file path where you want to store the values
    with open(file_path, "a") as file:
        file.write("\n")
            file.write(str(a))

if __name__ == '__main__':
    main()

