""" using argparser get city input from arguments and display weather data by fetching data from openweathermap.org"""

import argparse
from weather_forecast.api import *
from weather_forecast.utils import *
def main():
    """ main function """
    """add an argument to get  forecast data"""
    """if hi choosen get data from get_weather_history function and display it"""
    
    parser = argparse.ArgumentParser(description='Fetch weather data from openweathermap.org and display weather data based on user input', prog='weather', usage='%(prog)s city/cities [options] ', epilog='Enjoy the weather! :)', prefix_chars='-+/')
    gen = parser.add_argument_group('subcommands')
    parser.add_argument('-st', '--store', help='store the weather data in json file')
    parser.add_argument('city', help='city name', nargs='*')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-t', '--temperature', help='temperature in °C', action='store_true')
    parser.add_argument('-p', '--pressure', help='pressure in hPa', action='store_true')
    parser.add_argument('-hu', '--humidity', help='humidity in %%', action='store_true')
    parser.add_argument('-w', '--wind', help='wind speed in m/s and wind direction in °deg', action='store_true')
    parser.add_argument('-s', '--sun', help='sunrise and sunset time in HH:MM:SS', action='store_true')
    parser.add_argument('-a', '--all', help='display complete weather data', action='store_true')
    parser.add_argument('-f', '--forecast', help='get 5 day weather forecast', action='store_true')
    args = parser.parse_args()
    storedata = []
    if args.forecast:
        for city in args.city:
            data = get_weather_history(city)
            storedata.append(data)
            display_weather_history(data, args)
    elif args.all:
        for city in args.city:
            data = get_weather_data(city)
            storedata.append(data)
            display_full_weather_data(data)
    elif args.city:
        for city in args.city:
            data = get_weather_data(city)
            storedata.append(data)  
            display_weather_data(data, city, args)
    else:
        parser.print_help()
        return

    if args.store:
        print("Storing data in {}.json file".format(args.store))
        to_json(storedata,args)
    
    
if __name__ == '__main__':
    main()

