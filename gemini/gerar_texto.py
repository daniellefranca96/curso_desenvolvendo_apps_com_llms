from google.generativeai import GenerativeModel
import google.generativeai as genais
import os


os.environ['GOOGLE_API_KEY'] = "YOUR_API_KEY"

genais.configure(api_key=os.environ["GOOGLE_API_KEY"])

def generate():
  model = GenerativeModel("gemini-pro")
  response = model.generate_content(
    """O que é AGI?""",
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    },
  )
  
  return response
  
  


print(generate().text)