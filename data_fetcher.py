import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv('API_KEY')  # Get the API key from the environment variable
BASE_URL = "https://api.api-ninja.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    try:
        response = requests.get(f"{BASE_URL}?name={animal_name}", headers={"X-Api-Key": API_KEY}, timeout=10)
        response.raise_for_status()  # Raises an error for bad responses
        return response.json()  # Return the JSON response as a list of dictionaries
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []  # Return an empty list if the request failed