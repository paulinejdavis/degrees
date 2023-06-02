
### EXERCISE 1 ###
"""
TASK: Writing a log file to monitor the movement of ISS

Make a call to the API to get the current location for the International Space Station
See what data you get back
Convert the 'timestamp' from the response into readable date and time format
Write a log to the new file that captures time and ISS's location.
"""
import requests
from datetime import datetime
from pprint import pprint as pp

# This endpoint tells the current location for the International Space Station
endpoint = 'http://api.open-notify.org/iss-now.json'

# Make a call to the API to get the current location of the ISS
response = requests.get(endpoint)
data = response.json()
pp(data)

# Convert the 'timestamp' from the response into a readable date and time format
timestamp = data['timestamp']
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

msg = "At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}".format(
    dt=dt_object,
    lat=data['iss_position']['latitude'],
    lon=data['iss_position']['longitude']
)

# Write a log record to a file
with open('iss_log.txt', 'a') as file:
    file.write(msg + '\n')


