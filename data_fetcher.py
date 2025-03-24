import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv('API_KEY')  # Get the API key from the environment variable
BASE_URL = "https://api.api-ninja.com/v1/animals"  # Replace with the actual API endpoint


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    response = requests.get(f"{BASE_URL}?name={animal_name}", headers={"X-Api-Key": API_KEY})

    if response.status_code == 200:
        return response.json()  # Return the JSON response as a list of dictionaries
    else:
        return []  # Return an empty list if the request failed