def season_check(season):
    """
    Function to provide advice based on what season user inputs
    """

    season_advice = {
        "summer": "Water your plants regularly and provide some shade. \n",
        "winter": "protect your plants from frost with covers. \n",
        "spring": "Great time for planting!, Prepare soil and seeds. \n",
        "autumn": "Mulch your garden. \n.",
    }

    return season_advice.get(season.lower(), "No advice for this season. \n")


def plant_check(plant_type):
    """
    Function to provide advice based on what flower user inputs
    """
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Harvest regularly to encourage growth."
    }

    return plant_advice.get(plant_type.lower(), "No advice for this type of plant.")


# Get user input for season
season = input(str("Please enter what season: "))
season_result = season_check(season)
print(season_result)

# Get user input for plant type
plant_type = input(str("Please enter your plant type: "))
plant_result = plant_check(plant_type)
print(plant_result)


# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
