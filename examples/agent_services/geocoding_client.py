# File: src/services/geocoding_client.py
# Description: A client to fetch coordinates for a city name from Open-Meteo's geocoding API.

import httpx


class GeocodingClient:
    """Client for the Open-Meteo Geocoding API."""

    def __init__(self):
        self.base_url = "https://geocoding-api.open-meteo.com/v1/search"

    def fetch_coordinates(self, city_name: str) -> dict:
        """
        Fetches the coordinates for the first and most relevant result for a given city name.
        """
        params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
        with httpx.Client() as client:
            response = client.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            data = response.json()

            # The API returns a list under the 'results' key. Handle case where it's empty.
            if not data.get("results"):
                raise ValueError(
                    f"Could not find coordinates for city '{city_name}'. Please try a different name."
                )

            # Return the first result from the list
            return data["results"][0]
