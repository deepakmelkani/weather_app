import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"


def get_weather_data(location):
    url = f"{API_BASE_URL}?q={location}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()


def get_temperature_for_date(weather_data, date):
    for entry in weather_data['list']:
        if date in entry['dt_txt']:
            return entry['main']['temp']
    return None


def get_wind_speed_for_date(weather_data, date):
    for entry in weather_data['list']:
        if date in entry['dt_txt']:
            return entry['wind']['speed']
    return None


def get_pressure_for_date(weather_data, date):
    for entry in weather_data['list']:
        if date in entry['dt_txt']:
            return entry['main']['pressure']
    return None


def main():
    location = input("Enter the location (e.g., London,us): ")
    weather_data = get_weather_data(location)

    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature_for_date(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("Temperature data not found for the given date.")
        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed_for_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Wind Speed data not found for the given date.")
        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure_for_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Pressure data not found for the given date.")
        elif option == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()