import re
import json
import os


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


# HANDLE JSON MEMORY FILE

def load_memory():
    if not os.path.exists("memory.json"):
        return {}

    try:
        with open("memory.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


# CONVERT MEMORY DICTIONARY TO JSON AND SAVE TO FILE

def save_memory(memory):
    try:
        with open("memory.json", "w", encoding="utf-8") as file:
            json.dump(memory, file, indent=4, ensure_ascii=False)   # memory is saved in a human-readable format with proper indentation and without escaping non-ASCII characters
    except OSError:
        print("PyBot: Warning: Could not save memory.")


# SEARCH FOR PHRASES IN MESSAGES

def contains_phrase(message, phrase):
    pattern = rf"\b{re.escape(phrase)}\b"
    return re.search(pattern, message) is not None


# DETECT INTENT BASED ON MESSAGE

def detect_intent(message):
    message = message.lower().strip()

    for intent_name, intent_data in INTENTS.items():
        for pattern in intent_data["patterns"]:
            if contains_phrase(message, pattern):
                return intent_name

    return "unknown"


# GENERATE RESPONSE BASED ON MESSAGE AND MEMORY

def generate_response(message, memory):
    name = extract_name(message)

    if name:
        memory["name"] = name
        save_memory(memory)
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



# EXTRACT NAME FROM MESSAGE

def extract_name(message):
    pattern = r"my name is ([A-Za-z]+)"

    match = re.search(pattern, message, re.IGNORECASE)

    if match:
        return match.group(1)

    return None



def main():
    memory = load_memory()

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
