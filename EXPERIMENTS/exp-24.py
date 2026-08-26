def recognize_dialog_act(sentence):
    text = sentence.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey", "good morning"]):
        return "Greeting"

    elif text.endswith("?"):
        return "Question"

    elif any(word in text for word in ["thank you", "thanks"]):
        return "Thanking"

    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Goodbye"

    elif any(word in text for word in ["yes", "no", "correct"]):
        return "Answer"

    else:
        return "Statement"


print("Dialog Act Recognition")
print("----------------------")

while True:
    sentence = input("Enter dialog sentence: ")

    if sentence.lower() == "exit":
        break

    act = recognize_dialog_act(sentence)

    print("Dialog Act:", act)
