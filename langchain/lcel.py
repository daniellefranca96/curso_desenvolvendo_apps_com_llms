from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.llms import Bedrock
import boto3
import os

os.environ['AWS_ACCESS_KEY_ID'] = "AWS_ACCESS_KEY_ID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "AWS_SECRET_ACCESS_KEY"


BEDROCK_CLIENT = boto3.client("bedrock-runtime", 'us-east-1')
llm = Bedrock(
    client=BEDROCK_CLIENT, model_id="anthropic.claude-v2",
    model_kwargs={"max_tokens_to_sample": 1000}
)


synopsis_prompt = ChatPromptTemplate.from_template(
    """You are a playwright. Given the title of play, it is your job to write a synopsis for that title.

Title: {title}
Playwright: This is a synopsis for the above play:"""
)

writer_prompt = ChatPromptTemplate.from_template(
    """You are a experient play writer. Given the synopsis of play, it is your job to write a the script for it.

Play Synopsis:
{synopsis}
Script of the above play:"""
)

synopsis_chain  = synopsis_prompt | llm | StrOutputParser()
writer_chain    = (
            {"synopsis": synopsis_chain}
            | writer_prompt
            | llm
            | StrOutputParser()
)


print(writer_chain.invoke({"title": "Zombie invade New York"}))