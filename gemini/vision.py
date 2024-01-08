from langchain_google_genai import ChatGoogleGenerativeAI
from PIL import Image
import io
import base64
import os

os.environ['GOOGLE_API_KEY'] = "YOUR_API_KEY"

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

def pegar_bytes_imagem(caminho):
    image = Image.open(caminho)
    # Create a bytes buffer
    buffer = io.BytesIO()

    # Save image to the buffer
    image.save(buffer, format="PNG")

    # Get the buffer's content as a byte string
    buffered_png = buffer.getvalue()

    # Encode the byte string in Base64 and decode it to a UTF-8 string
    base64_encoded_string = base64.b64encode(buffered_png).decode("utf-8")

    # Format the Base64 string
    return f"data:image/png;base64,{base64_encoded_string}"
    
imagem = pegar_bytes_imagem("imagem.png")

llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")
# example
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Qual o remédio na imagem e a sua dosagem?",
        },  # You can optionally provide text parts
        {"type": "image_url", "image_url": "https://www.youtube.com/watch?v=y9WeJ4GJ5gs"},
    ]
)
print(llm.invoke([message]))