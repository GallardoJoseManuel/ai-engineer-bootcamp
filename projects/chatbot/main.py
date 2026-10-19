import re
import json
import os
from datetime import datetime

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



# LOAD CONVERSATION HISTORY FROM JSON
def load_history():
    if not os.path.exists("history.json"):
        return []

    try:
        with open("history.json", "r", encoding="utf-8") as file:
            history = json.load(file)

        if isinstance(history, list):
            return history

        return []

    except (json.JSONDecodeError, OSError):
        return []


# SAVE CONVERSATION HISTORY TO JSON
def save_history(history):
    try:
        with open("history.json", "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4, ensure_ascii=False)
    except OSError:
        print("PyBot: Warning: Could not save conversation history.")


# CLEAR CONVERSATION HISTORY
def clear_history():
    history = []
    save_history(history)
    print("PyBot: Conversation history cleared.")
    return history



# DISPLAY CONVERSATION HISTORY
def show_history(history):
    if not history:
        print("PyBot: No conversation history yet.")
        return

    print("PyBot: Conversation history:")

    for entry in history:
        if entry["role"] == "user":
            speaker = "You"
        else:
            speaker = "PyBot"

        timestamp = entry.get("timestamp")

        if timestamp:
            print(f"[{timestamp}] {speaker}: {entry['message']}")
        else:
            print(f"{speaker}: {entry['message']}")


# DISPLAY AVAILABLE COMMANDS
def show_help():
    print("PyBot: Available commands:")
    print("- help: Show available commands")
    print("- history: Show conversation history")
    print("- clear history: Clear conversation history")
    print("- exit: End the conversation")


# HANDLE SPECIAL COMMANDS

def handle_command(user_message, history):
    command = user_message.lower().strip()

    if command == "help":
        show_help()
        return True, history

    elif command == "history":
        show_history(history)
        return True, history

    elif command == "clear history":
        history = clear_history()
        return True, history

    elif command == "exit":
        print("PyBot: See you soon!")
        return True, history

    return False, history





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
    history = load_history()

    print("PyBot: Hello! I'm PyBot.")
    print("PyBot: Type 'exit' to end the conversation.")
        
    while True:
        user_message = input("You: ").strip()

        is_command, history = handle_command(user_message, history)

        if is_command:
            if user_message.lower().strip() == "exit":
                break
            continue

        timestamp = datetime.now().isoformat(timespec="seconds")

        history.append({
            "role": "user",
            "message": user_message,
            "timestamp": timestamp,
        })

        response = generate_response(user_message, memory)
        print(f"PyBot: {response}")

        history.append({
            "role": "assistant",
            "message": response,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        })

        save_history(history)



if __name__ == "__main__":
    main()
