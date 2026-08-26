# EXP-25: Text Generation Based on a Given Prompt

def generate_text(prompt):
    prompt = prompt.lower()

    if "artificial intelligence" in prompt or "ai" in prompt:
        return (
            "Artificial Intelligence is a branch of computer science that "
            "enables machines to perform tasks that normally require human "
            "intelligence. It is used in education, healthcare, automation, "
            "and many other fields."
        )

    elif "natural language processing" in prompt or "nlp" in prompt:
        return (
            "Natural Language Processing is a field of Artificial Intelligence "
            "that enables computers to understand, process, and generate human "
            "language. It is used in chatbots, translation, sentiment analysis, "
            "and text classification."
        )

    elif "machine learning" in prompt:
        return (
            "Machine Learning is a technique that allows computers to learn "
            "patterns from data and make predictions or decisions without "
            "being explicitly programmed for every task."
        )

    elif "python" in prompt:
        return (
            "Python is a popular high-level programming language known for "
            "its simple syntax and wide range of applications. It is commonly "
            "used in web development, data science, AI, and automation."
        )

    else:
        return (
            "This is generated text based on the given prompt. "
            "The system analyzes the input prompt and produces a "
            "relevant textual response."
        )


print("====================================")
print("       TEXT GENERATION SYSTEM")
print("====================================")

prompt = input("Enter your prompt: ")

result = generate_text(prompt)

print("\nGenerated Text:")
print(result)

print("\n====================================")