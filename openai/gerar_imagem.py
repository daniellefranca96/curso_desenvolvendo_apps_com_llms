from openai import OpenAI


api_key='YOUR_API_KEY'

client = OpenAI(api_key=api_key)


response = client.images.generate(
  model="dall-e-2",
  prompt="a house build in the fall of a waterfall",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)