
import requests

def get_location(latitude, longitude):
    url = f'https://api.weather.gov/points/{latitude},{longitude}'

    response = requests.get(url)

    #print (response.text)
    if response.ok:
        office = str(response.json()['properties']['gridId'])
        gridx = str(response.json()['properties']['gridX'])
        gridy = str(response.json()['properties']['gridY'])
        location = [office, gridx, gridy]
        return location
    
    else:
        raise Exception('Failed to fetch forecast.')


def get_forecast(office,gridX,gridY):
    # Construct the API URL for the given latitude and longitude
    url = f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast'

    # Send a GET request to the API URL
    response = requests.get(url)

    #print(response.text)

     

    # If the response is successful, extract the forecast data
    if response.ok:
        forecast = str(response.json()['properties']['periods'][2]['temperature'])
        forecast += "F "+ str(response.json()['properties']['periods'][2]['temperatureTrend'])
        forecast += " - "+ str(response.json()['properties']['periods'][2]['shortForecast'])
        return forecast

    # If the response is not successful, raise an exception
    else:
        raise Exception('Failed to fetch forecast.')

# Example usage information to Boston, MA
def main():
    lat = float(input("Enter a latitude(negative values for Southern hemisphere): "))
    long = float(input("Enter a longitude(negative values for Western hemisphere): "))
    location = get_location(lat, long)
    print (location)
    office = location[0]
    gridX = location[1]
    gridY = location[2]
    forecast = get_forecast(office, gridX, gridY)
    print(forecast)

main()
