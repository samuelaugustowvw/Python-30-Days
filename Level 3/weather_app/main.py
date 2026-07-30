import os
import requests
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
def display_title():
    print("\n========================")
    print("      WEATHER APP")
    print("========================")
def get_city():
    while True:
        city = input("Enter a city (or 0 to exit): ").strip()
        if city:
            return city
        print("Please type a city name.")
def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en",
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("Network error. Check your internet connection.")
        return None
    if response.status_code==200:
        return response.json()
    elif response.status_code==404:
        print("City not found. Check the spelling and try again.")
    elif response.status_code==401:
        print("Invalid API key. Check your OPENWEATHER_API_KEY.")
    else:
        print(f"Something went wrong (code {response.status_code}).")
    return None
def display_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    condition = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    print("\n========================")
    print(f"     {city}, {country}")
    print("========================")
    print(f"Condition:    {condition}")
    print(f"Temperature:  {temp:.1f}°C (feels like {feels_like:.1f}°C)")
    print(f"Humidity:     {humidity}%")
    print(f"Wind:         {wind} m/s")
    print("========================")
def main():
    if not API_KEY:
        print("No API key found.")
        print("Set it with:  export OPENWEATHER_API_KEY=your_key_here")
        return
    display_title()
    while True:
        city = get_city()
        if city=="0":
            print("Goodbye!")
            break
        print("\nFetching weather...")
        data = fetch_weather(city)
        if data:
            display_weather(data)
        print()
if __name__ == "__main__":
    main()