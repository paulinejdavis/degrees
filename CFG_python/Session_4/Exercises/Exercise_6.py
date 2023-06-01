### EXERCISE 6 ###
"""
Print the values of name, post_code and street_number from the dictionary
"""

person = {
    "name": "John Smith",
    "post_code": "12345",
    "street_number": "10",
    "location":{
        'longitude':127,
        'latitude': 63,
    }

}

print("Name:", person["name"])
print("Post Code:", person["post_code"])
print("Street Number:", person["street_number"])

print("Location:", person["location"]["longitude"])
print("Location:", person["location"]["latitude"])