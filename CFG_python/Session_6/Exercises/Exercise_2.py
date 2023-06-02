
### EXERCISE 2 ###
"""
 Get the height and weight of a specific Pokemon and print the output

!!! Extension !!!: Print the names of all of a specific Pokemon's moves
"""

import requests


def get_pokemon_info(pokemon_name):
    # Make a GET request to the PokeAPI to retrieve Pokemon information
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if response.status_code == 200:
        pokemon_data = response.json()
        height = pokemon_data['height']
        weight = pokemon_data['weight']
        moves = [move['move']['name'] for move in pokemon_data['moves']]

        # Print the height and weight
        print(f"Pokemon: {pokemon_name}")
        print(f"Height: {height}")
        print(f"Weight: {weight}")

        # Print the names of all moves
        print("Moves:")
        for move in moves:
            print(move)
    else:
        print("Error: Pokemon not found")


# Specify the Pokemon name
pokemon_name = "charizard"

# Call the function to get and print the Pokemon information
get_pokemon_info(pokemon_name)
