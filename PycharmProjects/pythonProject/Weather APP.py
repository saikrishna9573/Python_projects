import requests
from tkinter import Tk, Label, Entry, Button, StringVar


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    response = requests.get(complete_url)
    return response.json()


def show_weather():
    city = city_var.get()
    api_key = "2b098bfe86250dbd948d3a0650ab8e78"  # Replace with your OpenWeatherMap API key
    weather_data = get_weather(api_key, city)

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather_data["weather"][0]["description"]

        result.set(f"Temperature: {temperature}°C\n"
                   f"Pressure: {pressure} hPa\n"
                   f"Humidity: {humidity}%\n"
                   f"Description: {weather_description}")
    else:
        result.set("City Not Found!")


# Setting up the GUI
root = Tk()
root.title("Weather App")

city_var = StringVar()
result = StringVar()

Label(root, text="Enter City Name:").grid(row=0, column=0, padx=10, pady=10)
Entry(root, textvariable=city_var).grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Get Weather", command=show_weather).grid(row=0, column=2, padx=10, pady=10)
Label(root, textvariable=result, justify='left').grid(row=1, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
