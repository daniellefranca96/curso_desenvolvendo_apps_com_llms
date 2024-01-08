from langchain.llms import KoboldApiLLM

llm = KoboldApiLLM(endpoint="http://localhost:5001", max_length=500)

print(llm("### Instruction:\nWhat is AGI?\n### Response:"))