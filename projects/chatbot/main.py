
import re


INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "response": "Hello! How are you?",
    },
    "name": {
        "patterns": ["what is your name", "who are you"],
        "response": "I'm PyBot, your first chatbot.",
    },
    "capabilities": {
        "patterns": ["what can you do", "help me"],
        "response": "For now, I can respond to a few messages.",
    },
    "goodbye": {
        "patterns": ["goodbye", "bye", "see you later"],
        "response": "See you soon!",
    },
    "creator": {
        "patterns": ["who created you", "who made you"],
        "response": "I was created by José Manuel Gallardo."
    }
}


def contains_phrase(message, phrase):
    pattern = rf"\b{re.escape(phrase)}\b"
    return re.search(pattern, message) is not None


def detect_intent(message):
    message = message.lower().strip()

    for intent_name, intent_data in INTENTS.items():
        for pattern in intent_data["patterns"]:
            if contains_phrase(message, pattern):
                return intent_name

    return "unknown"



def generate_response(message, memory):
    name = extract_name(message)

    if name:
        memory["name"] = name
        return f"Nice to meet you, {name}!"

    normalized_message = message.lower().strip()

    if contains_phrase(normalized_message, "what is my name"):
        if "name" in memory:
            return f"Your name is {memory['name']}."

        return "I don't know your name yet. Tell me by saying 'my name is ...'."

    intent = detect_intent(message)

    if intent == "unknown":
        return "I don't know how to respond to that yet."

    return INTENTS[intent]["response"]




def extract_name(message):
    pattern = r"my name is ([A-Za-z]+)"

    match = re.search(pattern, message, re.IGNORECASE)

    if match:
        return match.group(1)

    return None



def main():
    memory = {}

    print("PyBot: Hello! I'm PyBot.")
    print("PyBot: Type 'exit' to end the conversation.")

    while True:
        user_message = input("You: ")

        if user_message.lower().strip() == "exit":
            print("PyBot: See you soon!")
            break

        response = generate_response(user_message, memory)
        print(f"PyBot: {response}")


if __name__ == "__main__":
    main()
