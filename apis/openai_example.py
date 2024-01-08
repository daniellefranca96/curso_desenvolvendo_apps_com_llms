import openai
from structure import generate_project_structure_json


api_key='YOUR_API_KEY'

from openai import OpenAI

client = OpenAI(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explique o que é AGI",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)