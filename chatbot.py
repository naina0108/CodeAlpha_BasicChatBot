def get_response(user_input):
    """Returns a predefined reply based on keywords in the user's input."""
    text = user_input.lower().strip()


# Greetings
    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hi!"

    elif "good morning" in text:
        return "Good morning! Hope you have a great day."

    elif "good night" in text:
        return "Good night! Sleep well."

    elif "how are you" in text:
        return "I'm fine, thank you for asking! How about you?"


# About the bot
    elif "your name" in text:
        return "I'm a simple predefined rule-based chatbot built in Python."

    elif "who made you" in text or "who built you" in text:
        return "I was built using Python programming by my developer."

    elif "what can you do" in text:
        return "I can chat about a few predefined basic topics - try asking me something!"

    elif "are you human" in text or "are you real" in text:
        return "Nope, just a chatbot- no feelings, running on code and rules."

    elif "how old are you" in text or "your age":
        return "I don't have an age - I was just written into existence."



# Small talk
    elif "what is python" in text:
        return "Python is a popular, beginner-friendly programming language used for Web Development,AI,Data Science and Automation."

    elif "weather" in text:
        return "I can't check live weather, but I hope it's nice where you are!"

    elif "favorite color" in text or "favourite colour" in text:
        return "I'd say royale blue,."

    elif "joke" in text:
        return "Why did the maths book look so sad? Because it has too many problems!"

    elif "sing" in text:
        return "I'd sing, but my voice is just text!"


# Gratitude and farewell
    elif "thank" in text:
        return "You're welcome!"

    elif "help" in text:
        return "Just type something like 'hello', 'joke', or 'what can you do'."

    elif text in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye, Have a wonderful day!"

    else:
        return "Sorry, I didn't understand that."


def chat():
    print("Chatbot: Hi! How can I assist you?")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if response == "Goodbye!":
            break


chat()
