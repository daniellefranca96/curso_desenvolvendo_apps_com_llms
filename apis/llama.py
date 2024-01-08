from llama_cpp import Llama

query = "Call me an Uber ride type \"Plus\" in Berkeley at zipcode 94704 in 10 minutes"
functions = [
    {
        "name": "Uber Carpool",
        "api_name": "uber.ride",
        "description": "Find suitable ride for customers given the location, type of ride, and the amount of time the customer is willing to wait as parameters",
        "parameters":  [{"name": "loc", "description": "location of the starting place of the uber ride"}, {"name":"type", "enum": ["plus", "comfort", "black"], "description": "types of uber ride user is ordering"}, {"name": "time", "description": "the amount of time in minutes the customer is willing to wait"}]
    }
]

llm = Llama(model_path="gorilla-openfunctions-v1.Q4_K_M.gguf")
template = """
USER: <<question>> {prompt} <<function>> {functions_string}\nASSISTANT:"""
print(llm(template.replace('{prompt}', query).replace('{functions_string}', str(functions))))