from openai import OpenAI


api_key='YOUR_API_KEY'

client = OpenAI(api_key=api_key)

audio_file= open("example.mp3", "rb")
transcript = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file,
  response_format="srt"
)

print(transcript)

with open("subtitle.srt", "w") as file:
    file.write(transcript)