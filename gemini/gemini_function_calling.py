import requests
from vertexai.preview.generative_models import (
    Content,
    FunctionDeclaration,
    GenerativeModel,
    Part,
    Tool,
)

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "YOUR_CREDENTIALS_FILE.json"


model = GenerativeModel("gemini-pro")

get_current_weather_func = FunctionDeclaration(
    name="get_current_weather",
    description="Get the current weather in a given location",
    parameters={
    "type": "object",
    "properties": {
        "location": {
            "type": "string",
            "description": "Location"
        }
    }
},
)

weather_tool = Tool(
    function_declarations=[get_current_weather_func],
)

prompt = "What is the weather like in Boston?"

response = model.generate_content(
    prompt,
    generation_config={"temperature": 0},
    tools=[weather_tool],
)
print(response)