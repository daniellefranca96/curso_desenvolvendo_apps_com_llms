from openai import OpenAI
import base64
import pathlib
import os

folder = str(pathlib.Path(__file__).parent.resolve())

api_key='YOUR_API_KEY'

client = OpenAI(api_key=api_key)

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return "data:image/jpeg;base64,"+ str(base64.b64encode(image_file.read()).decode('utf-8'))

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "describe the image"},
        {
          "type": "image_url",
          "image_url": {
            "url": encode_image(folder+"\\imagem.png")
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])