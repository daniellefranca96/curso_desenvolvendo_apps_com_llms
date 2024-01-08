from openai import OpenAI


api_key='YOUR_API_KEY'

client = OpenAI(api_key=api_key)

audio_file= open("example.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcript)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful translation assistant."},
    {"role": "user", "content": "translate this:"+transcript.text},

  ]
)

print(response)