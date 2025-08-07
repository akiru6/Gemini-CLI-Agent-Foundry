# File: src/services/open_meteo_client.py
# Description: Updated to accept a structured Location object, improving type safety and clarity.

import httpx
from src.models import Location  # Import the Location model


class OpenMeteoClient:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def fetch_hourly_forecast(self, location: Location) -> dict:
        """
        Fetches the hourly forecast for a given Location object.
        """
        params: dict[str, str | float] = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            # CRITICAL: We request 'apparent_temperature' here to be used in our analysis.
            "hourly": "apparent_temperature,relativehumidity_2m,precipitation_probability,windspeed_10m,uv_index",
            "timezone": location.timezone,
        }
        with httpx.Client() as client:
            response = client.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
