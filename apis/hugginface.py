#from transformers import pipeline

#pipe = pipeline("text2text-generation", model="google/flan-t5-base")
#print(pipe("Translate to Spanish:  My name is Arthur"))

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

prompt = "Translate to Spanish:  My name is Arthur"

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

input_ids = tokenizer.encode(prompt, return_tensors='pt')
generated_ids = model.generate(input_ids, max_length=1024, do_sample=True)

generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
print(generated_text)