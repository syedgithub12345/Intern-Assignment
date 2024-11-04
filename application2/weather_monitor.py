import requests
import time

API_KEY = 'your_openweathermap_api_key'  # Replace with your API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def get_weather_data(city):
    url = BASE_URL.format(city, API_KEY)
    response = requests.get(url)
    data = response.json()
    return data

def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def main():
    for city in cities:
        weather_data = get_weather_data(city)
        temp_celsius = kelvin_to_celsius(weather_data['main']['temp'])
        print(f"Current temperature in {city}: {temp_celsius}°C")

if __name__ == "__main__":
    main()
