from geopy.geocoders import Nominatim
from flask import Flask, request
import json , requests


'''
Set your server route and port below. This will be the location for the POST request to be sent from the client.
'''
SERVER_PORT = 5000
SERVER_ROUTE = '/Short_Term_Weather'


def coord_maker(City):
    '''
    This function takes a City string as an input and returns a tuple with lat , long of that city.
    It can be just the city or city and state it is pretty smart.
    '''

    geolocator = Nominatim(user_agent="Weather_Checker_SL")

    location = geolocator.geocode(City)

    lat_long = location.latitude,location.longitude

    return lat_long


def short_term_forecast(coords):
    '''
    Input a tuple with (lat,long)
    '''

    # The Raw_data holds an interim request from the weather api. The Full_forecast is the specific medium term
    # forcast from the final API.
    Raw_data = requests.get(f"https://api.weather.gov/points/{coords[0]},{coords[1]}")
    Full_forecast = requests.get(Raw_data.json()["properties"]["forecast"]).json()

    # This strips all the irrelivant information from the Full_forecast .json.
    want = ["name", "detailedForecast"]
    shortened_ls = []
    full_ls = []

    # If you want more days increase 3 if you want only one day set the range to 1,2.
    for each in range(1, 3):
        for each_want in want:
            shortened_ls.append(f"{Full_forecast['properties']['periods'][each][each_want]}")
        full_ls.append(shortened_ls)
        shortened_ls = []

    # These are just to add a space at the end of the day in the final output.
    full_ls[0][0] += " "
    full_ls[1][0] += " "
    return full_ls

def main():

    #If you would like to input on startup.
    # SERVER_ROUTE = input("Please input the route for your server (Ex: /Weather_Forecast): ")
    # SERVER_PORT = input("Please input the port that your server will run on(Ex: 5000): ")

    app = Flask(__name__)

    @app.route(SERVER_ROUTE, methods=['POST'])
    def Weather():
        '''
        This takes a double as a (lat, lon) in the body of a POST request.
        body: {"lat_lon": (lat, lon)}
        '''
        Lat_Long = request.get_json()

        message = json.dumps({"result": short_term_forecast(Lat_Long)})
        # print(message)
        # Return data in json format
        return message


    app.run(port= SERVER_PORT)

if __name__ =='__main__':
    main()