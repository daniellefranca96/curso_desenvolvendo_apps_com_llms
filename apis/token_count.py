import tiktoken

string = """Orca 2 is a new, innovative language model developed by Microsoft, focusing on enhancing the reasoning abilities of smaller language models (LMs), it is designed to be a smaller model, with versions having 7 billion and 13 billion parameters.
Orca 2 has made significant strides in both efficiency and performance, matching or even surpassing the capabilities of larger models like Meta's Llama-2 Chat-70B in complex reasoning tasks and zero-shot scenarios.
Another interesting discovery on the research of this model is the possibility of use of AI generated data for model trainning, Orca 2 was
only trained with generated data from GPT4 and shown great results and performance on its tasks proving the the use of AI generated text for trainning is as good as using human data content."""

enc = tiktoken.encoding_for_model("gpt-4")
result = enc.encode(string)
print(len(result))