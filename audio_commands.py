import requests
import datetime

API_KEY = "146f426718334ac99e881949889859bd"
headers = {"Authorization": f"Bearer {API_KEY}"}
OPENMETEO_API_URL = "https://api.open-meteo.com/v1/forecast"
LATITUDE = "50.726758"  # Replace with actual latitude
LONGITUDE = "-3.523003"  # Replace with actual longitude

def get_weather():
    # Set parameters for weather forecast
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current_weather": True
    }
    response = requests.get(OPENMETEO_API_URL, params=params)
    if response.status_code == 200:
        weather_data = response.json()["current_weather"]
        temperature = weather_data["temperature"]
        conditions = weather_data["weathercode"]
        return f"The current temperature is {temperature}°C with {conditions}."
    else:
        return "I couldn't retrieve the weather information."

def respond(command):
    if "time" in command.lower():
        response_text = f"The time is {datetime.datetime.now().strftime('%I:%M %p')}."
    elif "weather" in command.lower():
        response_text = get_weather()
    else:
        response_text = "I'm sorry, I didn't understand the command."
    
    # Convert response text to speech
    tts_url = "https://aimlapi.com/api/text-to-speech"
    tts_response = requests.post(tts_url, headers=headers, json={"text": response_text})
    if tts_response.status_code == 200:
        audio_url = tts_response.json().get("audio_url")
        print("Response audio:", audio_url)
    else:
        print("Error in TTS:", tts_response.text)

# Example usage
command = "What's the weather?"
respond(command)


