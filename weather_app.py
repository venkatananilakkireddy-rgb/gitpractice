weather = {
    "Puttur": "Sunny",
    "Chennai": "Cloudy",
    "Hyderabad": "Rainy",
    "Bangalore": "Windy"
}

city = input("Enter city name: ")

if city in weather:
    print("Weather:", weather[city])
else:
    print("City not found")