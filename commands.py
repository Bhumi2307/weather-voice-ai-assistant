import datetime
import requests
from speech_engine import speak

def get_weather(city="London"):
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("main"):
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {desc}."
    else:
        return "City not found."

def execute_command(intent, query):
    if intent == "time":
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif intent == "weather":
        city = "London"
        report = get_weather(city)
        speak(report)
    elif intent == "exit":
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure how to help with that.")