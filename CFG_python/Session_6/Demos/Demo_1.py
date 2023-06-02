### DEMO 1 ###
"""
This API is called 'Open Notify' http://open-notify.org/
It gives access to data about the Intrnational Space NASA station!
This API DOES NOT require authentication,

TASK: Make a call to the API endpoint to get live information about astronauts in space

"""

import requests
from pprint import pprint as pp

endpoint1 = 'http://api.open-notify.org/astros.json'  # this endpoint returns data about astronauts currently in space

response = requests.get(endpoint1) # making a call to the API

print(response.status_code)  # make sure that your connection status code is 200, which means success!

data = response.json()  # lets see what data about people in space we get back from the API response
pp(data)
#
#
# # let's extract data from the response and write it to a file
# # we need section 'people' from json, which is a list of dict, so...
# # we also need to extract name from each dict item in that list
#
with open('astranouts.txt', 'w') as text_file:
    for item in data['people']:
        text_file.write(item['name'] + '\n') # added new line character, so each name appears on a new line.

