'''
This program gives you the weather report of regions of USA.
I could not afford the API key and every website in India demanded it.
But forecast.weather.gov (USA-BASED) didn't.

'''

from bs4 import BeautifulSoup
import requests
import geopy

geolocator = geopy.Nominatim(user_agent = 'my-application')

zipcode = input("Enter Zip Code (USA-ONLY): ")
location = geolocator.geocode(zipcode)
latitude = location.latitude
longitude = location.longitude

site = f'https://forecast.weather.gov/MapClick.php?lon={longitude}&lat={latitude}'
source = requests.get(site).text
soup = BeautifulSoup(source, 'lxml')

try:
    location = soup.find('h2', class_ = 'panel-title').text
    forecast = soup.find('p', class_ = 'myforecast-current').text
    temp = soup.find('p', class_ = 'myforecast-current-sm').text

    print(f'Weather for {location}')
    print(forecast)
    print(temp)

except AttributeError:
    print('Invalid Location')