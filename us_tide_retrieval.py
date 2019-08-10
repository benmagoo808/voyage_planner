"""
This script will take a dictionary with way points as keys and estimated
arrival times as values, make the appropriate API calls to NOAA, receive the
tide and current predictions, parse them and return a dictionary of
way points: {tide: height, ebb/flood: tidal stage, current: speed,
direction: direction of flow in degrees true}
"""



import requests
from datetime import datetime, timedelta

# Define our variables for this test script
station_id = '9447130'
waypoint = 'Seattle'
eta = '20180808 12:00'
eta2 = '20180808 13:00'


url = 'https://tidesandcurrents.noaa.gov/api/datagetter'
params = {'begin_date': eta, 'end_date': eta2, 'station': station_id,
          'product': 'predictions',
          'datum': 'STND', 'units': 'english', 'time_zone': 'lst_ldt',
          'format': 'json', 'Application': 'Web_Services'}
response = requests.get(url, params=params)  # Include a timeout,
# but a long one

if response:  # Print a connection status for each call in the terminal
    print('Successful connection to tide server.')
else:
    print('An error has occurred in connecting to the tide server.')
#json_response = response.json()  # Convert the response to formatted Json
print(response.text)

print(response.url)