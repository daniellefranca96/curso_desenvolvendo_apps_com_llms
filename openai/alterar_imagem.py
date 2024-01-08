from openai import OpenAI
import pathlib
import os

folder = str(pathlib.Path(__file__).parent.resolve())

api_key='YOUR_API_KEY'

client = OpenAI(api_key=api_key)


response = client.images.create_variation(
  model="dall-e-2",
  prompt="a house build in the fall of a waterfall with BLACK birds flying on the top right side",
  image=open(folder+"\\imagem.png", "rb"),
  image=open(folder+"\\mask.png", "rb"),
  size="512x512",
  n=2,
)

image_url = response.data[0].url
print(image_url)