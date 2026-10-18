
# PyBot — Python Chatbot

## Overview

PyBot is a rule-based chatbot built from scratch in Python
as part of the AI Engineer Bootcamp.

The project follows an incremental learning approach:
starting with basic Python programming and gradually
introducing more advanced chatbot techniques, machine
learning, and generative AI.

## Current Features

- Interactive conversations through the terminal.
- Text normalization using `lower()` and `strip()`.
- Rule-based responses using conditional statements.
- A default response for unrecognized messages.
- Conversation termination using the `exit` command.

## Requirements

- Python 3.12 or a compatible version.
- No external libraries required.

## Project Structure

```text
chatbot/
├── main.py
└── README.md
```

## How to Run

From the root directory of the repository, run:

```bash
python projects/chatbot/main.py
```

## Example Conversation

```text
PyBot: Hello! I'm PyBot.
PyBot: Type 'exit' to end the conversation.
You: hello
PyBot: Hello! How are you?
You: what is your name
PyBot: I'm PyBot, your first chatbot.
You: exit
PyBot: See you soon!
```

## Learning Objectives

- Practice Python functions and control flow.
- Understand rule-based conversational logic.
- Learn how to process and normalize text.
- Develop good software documentation habits.
- Track project progress with Git and GitHub.

## Roadmap

1. Basic conversational loop and rule-based responses.
2. Intent detection and improved text processing.
3. Conversation memory.
4. Machine learning for intent classification.
5. Integration with a generative AI model.

## Current Status

Phase 1 — Basic rule-based chatbot.
