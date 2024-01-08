import chainlit as cl
from langchain.chains import LLMChain
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.llms import Bedrock
from chainlit import make_async
import re
import boto3
import os

os.environ['AWS_ACCESS_KEY_ID'] = "AWS_ACCESS_KEY_ID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "AWS_SECRET_ACCESS_KEY"

BEDROCK_CLIENT = boto3.client("bedrock-runtime", 'us-east-1')
llm = Bedrock(
    client=BEDROCK_CLIENT, model_id="anthropic.claude-v2",
    model_kwargs={"max_tokens_to_sample": 1000}
)


prompt = PromptTemplate.from_template(
    """Summarize this text:

{output_text}

Summary:"""
)

map_chain = LLMChain(llm=llm, prompt=prompt)

prompt_c = PromptTemplate.from_template(
    """Join all these summaries in a final coherent answer:

{output_text}

Summary:"""
)

combine_chain = LLMChain(llm=llm, prompt=prompt_c)

text_splitter = CharacterTextSplitter(
    separator = ".",
    chunk_size = 1000,
    chunk_overlap  = 50,
    length_function = len,
    is_separator_regex = False,
)


def proccess_document(document_path):
    loader = PyPDFLoader(document_path)
    pages = loader.load_and_split()
    
    texto_final_resumos = ""
    for text in pages:
        texto_final_resumos+= "\n\n"+text.page_content
        
    return map_chain.run(texto_final_resumos)
    
    
async_proccess_document = make_async(proccess_document)



@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):

    texto_final = await async_proccess_document(message.content)

    await cl.Message(content=texto_final).send()
        
        
        
