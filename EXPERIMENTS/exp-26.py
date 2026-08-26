from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("English to French Translation")
print("------------------------------")

model_name = "Helsinki-NLP/opus-mt-en-fr"

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded successfully!")

text = input("Enter English text: ")

inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(**inputs)

translation = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("\nEnglish:", text)
print("French:", translation)
