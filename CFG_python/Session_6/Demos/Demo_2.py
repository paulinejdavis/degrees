
###  DEMO 2 (as requires Authentication key ###
"""
This API is called 'Open Weather Map' http://api.openweathermap.org
It gives access to data about weather at different locations in the world and much more!
This API DOES require authentication! But it is FREE to register.
In order to get some data back, you need to use a unique 'Authentication Key'
It is VERY COMMON for many APIs to use authentication, especially in the professional world.
# b8fcdef82a03d5bfb55d99065e673068

Also introduce idea of PAYLOAD and different types of it. For this API the payload is a dictionary consisting of:
 location q, unit and appid which is your personal API key.
"""

import requests
from pprint import pprint as pp

appid = '9a47229abfbe24d8da8f514199f17195'  # key to connect to the API --> create a free account and paste your OWN key here

endpoint = 'http://api.openweathermap.org/data/2.5/weather' # see doc to customise your payload

payload = {
    'q': 'London,UK',
    'unit': 'metrics',
    'appid': appid,
}

response = requests.get(url=endpoint, params=payload)

data = response.json()

weather = data['weather']
new_dic = {}
new_dic = weather[0]
pp(weather)
#pp(weather[0]['id'])
pp(weather[0]['description'])

# pp(data['name'])
# pp(data['weather'])

# pp(data)

# import requests
# from pprint import pprint as pp
#
# appid = '9a47229abfbe24d8da8f514199f17195'  # key to connect to the API --> create a free account and paste your OWN key here
#
# endpoint = 'http://api.openweathermap.org/data/2.5/weather'  # see doc to customise your payload
#
# payload = {
#     'q': 'London,UK',
#     'units': 'metric',  # corrected typo from 'unit' to 'units'
#     'appid': appid,
# }
#
# response = requests.get(url=endpoint, params=payload)
#
# if response.status_code == 200:
#     data = response.json()
#     if 'name' in data:
#         pp(data['name'])
#     else:
#         print("City name not found in the response.")
#
#     if 'weather' in data:
#         pp(data['weather'])
#     else:
#         print("Weather information not found in the response.")
#
#     pp(data)
# else:
#     print("Error:", response.status_code, response.content)

