from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load your fine-tuned model
model_path = "models/final_model"

tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

print("=" * 60)
print(" GPT-2 Text Generator ")
print("=" * 60)

while True:
    prompt = input("\nEnter a prompt (or type 'exit' to quit): ")

    if prompt.lower() == "exit":
        break

    inputs = tokenizer.encode(prompt, return_tensors="pt")

    outputs = model.generate(
        inputs,
        max_length=120,
        do_sample=True,
        temperature=0.8,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,
        pad_token_id=tokenizer.eos_token_id
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("\nGenerated Text:\n")
    print(generated_text)