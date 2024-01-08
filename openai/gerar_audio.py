from pathlib import Path
from openai import OpenAI


api_key='YOUR_API_KEY'

client = OpenAI(api_key=api_key)


speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="nova",
  input="Hoje nos vamos sair para uma festa!"
)

response.stream_to_file(speech_file_path)