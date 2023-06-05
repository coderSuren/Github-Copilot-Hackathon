""" using argparser get city input from arguments and display weather data by fetching data from openweathermap.org"""

import argparse
from weather_forecast.api import *
from weather_forecast.utils import *
def main():
    """ main function """
    """add an argument to get  history data"""
    """if hi choosen get data from get_weather_history function and display it"""
    
    parser = argparse.ArgumentParser(description='Fetch weather data from openweathermap.org and display weather data based on user input', prog='weather', usage='%(prog)s city [options] ', epilog='Enjoy the program! :)', prefix_chars='-+/')
    gen = parser.add_argument_group('subcommands')
    gen.add_argument('-st', '--store', help='store the weather data in a file', nargs='?', default='json', choices=['json', 'csv'])
    parser.add_argument('city', help='city name', nargs='*', default='Chennai')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-t', '--temperature', help='temperature in °C', action='store_true')
    parser.add_argument('-p', '--pressure', help='pressure in hPa', action='store_true')
    parser.add_argument('-hu', '--humidity', help='humidity in %%', action='store_true')
    parser.add_argument('-w', '--wind', help='wind speed in m/s and wind direction in °', action='store_true')
    parser.add_argument('-s', '--sun', help='sunrise and sunset time in HH:MM:SS', action='store_true')
    parser.add_argument('-a', '--all', help='display full weather data', action='store_true')
    parser.add_argument('-hi', '--history', help='get 5 day weather history', action='store_true')
    
    args = parser.parse_args()
    storedata = []
    if args.history:
        for city in args.city:
            data = get_weather_history(city)
            storedata.append(data)
            display_weather_history(data, args)
    elif args.all:
        for city in args.city:
            data = get_weather_data(city)
            storedata.append(data)
            display_full_weather_data(data)
    else:
        for city in args.city:
            data = get_weather_data(city)
            storedata.append(data)  
            display_weather_data(data, city, args)
    
    if args.store:
        print("Storing data in {} file".format(args.store))
        if args.store=='json':
            to_json(storedata,args)
        elif args.store=='csv':
            to_csv(storedata,args)
        else:
            print("Invalid file format {}".format(args.store))
    
    
if __name__ == '__main__':
    main()

