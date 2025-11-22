

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools import tool
from dotenv import load_dotenv
load_dotenv()
import os
import requests
import json
from datetime import datetime
from typing import Any
# Description of Project #
# I need to fetch weather of any city of Pakistan and then when i say to my LLm that please fetch this city weather for me and then store it in a weather_file 

@tool
def get_weather(city:str)->str:
    """This tool will fetch the weather of a city in Pakistan using an api. """
    api_key = os.getenv("Weather_API_KEY")
    if api_key is None:
        return "Weather API key is not set."

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response=requests.get(url)
    return json.dumps(response.json())

# now i need to create a tool to save the weather data in a file
@tool
def save_weather_info(city: str, weather_json_string: str) -> str:
    """This tool will save the weather data to a file.
    
    Args:
        city: The name of the city
        weather_json_string: Weather data as a JSON string
    """
    try:
        # Parse the JSON string back to dict
        weather_data = json.loads(weather_json_string)
    except json.JSONDecodeError:
        return "Error: Invalid weather data format"
    
    os.makedirs("weather_data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"weather_data/{city}_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(weather_data, indent=4, fp=f)# t
    return f"Weather data saved to {filename}"
 
# Intializing our LLm model


llm=Groq(id="llama-3.3-70b-versatile")

agent= Agent(
    model=llm,
    tools=[get_weather,save_weather_info],
instructions="""You are a helpful AI assistant that can fetch weather and save weather data. 
    When user asks to save weather:
    1. First call get_weather(city) - this returns a JSON string
    2. Then call save_weather_info(city, weather_json_string) with the exact string returned from get_weather and only save the temperature and Humidity information.
    """,
    markdown=True,
    debug_mode=True
)
# Running the agent 

result=agent.print_response("what is the current weather in Lahore also save the weather information into file ",stream=True)

print(result)