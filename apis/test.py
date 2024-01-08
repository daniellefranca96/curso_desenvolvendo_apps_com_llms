from vertexai.language_models import TextGenerationModel
import os
import sys
import os

# Add the path to the 'langchain2' folder to sys.path
# Assuming 'langchain2' is in the same directory as your 'test.py' file
langchain2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'langchain2'))
sys.path.insert(0, langchain2_path)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "ia-test-382713-19c6702bfd0c.json"

from langchain2.llms import VertexAI

llm = VertexAI()
print(llm("What are some of the pros and cons of Python as a programming language?"))