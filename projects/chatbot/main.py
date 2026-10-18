
def generate_response(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hello! How are you?"

    elif "what is your name" in message:
        return "I'm PyBot, your first chatbot."

    elif "what can you do" in message:
        return "For now, I can respond to a few messages."

    elif message in ["goodbye", "bye", "see you later"]:
        return "See you soon!"

    else:
        return "I don't know how to respond to that yet."


def main():
    print("PyBot: Hello! I'm PyBot.")
    print("PyBot: Type 'exit' to end the conversation.")

    while True:
        user_message = input("You: ")

        if user_message.lower().strip() == "exit":
            print("PyBot: See you soon!")
            break

        response = generate_response(user_message)
        print(f"PyBot: {response}")


if __name__ == "__main__":
    main()
