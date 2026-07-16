import requests
from config import WEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def execute(arguments: dict):
    city = arguments.get("city")

    if not city:
        return "Weather Error: City is required."

    try:
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        weather = data["weather"][0]["description"].title()

        wind_speed = data["wind"]["speed"]

        return (
            f"📍 City: {city_name}, {country}\n"
            f"🌤 Weather: {weather}\n"
            f"🌡 Temperature: {temperature}°C\n"
            f"🤗 Feels Like: {feels_like}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind Speed: {wind_speed} m/s"
        )

    except requests.exceptions.HTTPError:
        return f"Weather Error: City '{city}' not found."

    except Exception as e:
        return f"Weather Error: {e}"


if __name__ == "__main__":
    print(
        execute(
            {
                "city": "Delhi"
            }
        )
    )