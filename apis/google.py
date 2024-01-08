from vertexai.language_models import TextGenerationModel
from langchain.llms import VertexAI
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "YOUR_CREDENTIALS_FILE.json"

llm = VertexAI()
print(llm.predict('Hi'))
exit()



model = TextGenerationModel.from_pretrained("text-bison@001")

print(model.predict(
    "What is the best recipe for banana bread? Recipe:",
    # The following are optional parameters:
    #max_output_tokens=128,
    #temperature=0,
    #top_p=1,
    #top_k=5,
))