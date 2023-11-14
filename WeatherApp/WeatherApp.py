import requests

def get_weather(api_key, location):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        response.raise_for_status()

        weather_data = response.json()
           
        return weather_data

    except requests.exceptions.HTTPError as errh:
        text="This is not a Valid  City or ZIP, Enter Valid City Name or ZIP Code "
        print(f'HTTP Error: {text }')
   
    return None

def display_weather(weather_data):
    if weather_data:
        tocap=weather_data['name']
        print(f"Weather in {tocap.upper()}")#Get the city in uppercase formate
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather Conditions: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather data.")

if _name_ == "_main_":
    # the actual API key I obtained from OpenWeatherMap you can replace with your own api key from this openWeatherMap website
    api_key = 'fbcb6cfddcd28b4228e674a90bfa0632'
    
    # Get user input for the location (city or ZIP code)
    location = input("Enter city or ZIP code: ")

    # Fetch weather data
    weather_data = get_weather(api_key, location)

    # Display weather information
    display_weather(weather_data)