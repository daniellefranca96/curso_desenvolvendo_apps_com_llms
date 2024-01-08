from openai import OpenAI
import pathlib
import os

folder = str(pathlib.Path(__file__).parent.resolve())

api_key='YOUR_API_KEY'

client = OpenAI(api_key=api_key)


response = client.images.create_variation(
  model="dall-e-2",
  image=open(folder+"\\imagem.png", "rb"),
  size="512x512",
  n=2,
)

image_url = response.data[0].url
print(image_url)