from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
import boto3

os.environ['AWS_ACCESS_KEY_ID'] = "AWS_ACCESS_KEY_ID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "AWS_SECRET_ACCESS_KEY"

BEDROCK_CLIENT = boto3.client("bedrock-runtime", 'us-east-1')



from langchain.llms import Bedrock

llm = Bedrock(
    client=BEDROCK_CLIENT, model_id="anthropic.claude-v2"
)

conversation = ConversationChain(
    llm=llm, verbose=True, memory=ConversationBufferMemory()
)

print(conversation.predict(input="What is AGI?"))