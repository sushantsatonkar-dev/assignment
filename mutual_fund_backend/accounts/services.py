import requests
from django.conf import settings

RAPIDAPI_URL = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"
RAPIDAPI_KEY = settings.RAPIDAPI_KEY  # Store API key in settings.py

def fetch_open_ended_mutual_funds():
    """Fetch open-ended mutual funds from RapidAPI."""
    headers = {
        "x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com",
        "x-rapidapi-key": RAPIDAPI_KEY,
    }

    params = {"Scheme_Type": "Open"}

    response = requests.get(RAPIDAPI_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()  # Ensure API returns structured JSON data
    else:
        return {"error": f"Failed to fetch data, Status Code: {response.status_code}"}
