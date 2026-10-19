
import os

from openai import (
    OpenAI,
    APIError,
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    RateLimitError,
)


MODEL = os.getenv("OPENAI_MODEL", "gpt-6-luna")
MAX_OUTPUT_TOKENS = 400


def generate_llm_response(message, history=None, memory=None):
    if not os.getenv("OPENAI_API_KEY"):
        return "OPENAI_API_KEY is not configured."

    instructions = (
        "You are PyBot, a helpful conversational assistant. "
        "Answer naturally, clearly, and completely. "
        "Reply in the same language as the user."
    )

    if memory and memory.get("name"):
        instructions += (
            f"\nThe user's name is {memory['name']}. "
            "Use their name naturally when appropriate."
        )

    conversation = []

    if history:
        for entry in history[-10:]:
            role = entry.get("role")
            content = entry.get("message", "")

            if role in ("user", "assistant") and content:
                conversation.append({
                    "role": role,
                    "content": content,
                })

    if not conversation or conversation[-1]["content"] != message:
        conversation.append({
            "role": "user",
            "content": message,
        })

    try:
        client = OpenAI(timeout=30.0, max_retries=2)

        response = client.responses.create(
            model=MODEL,
            instructions=instructions,
            input=conversation,
            max_output_tokens=MAX_OUTPUT_TOKENS,
            store=False,
        )

        answer = (response.output_text or "").strip()

        if response.status == "incomplete":
            if answer:
                return (
                    answer
                    + "\n\n[Response may be incomplete.]"
                )

            return (
                "The response was incomplete. "
                "Please try asking a shorter question."
            )

        if not answer:
            return "The AI returned an empty response. Please try again."

        return answer

    except AuthenticationError:
        return "Authentication failed. Check your API key."

    except RateLimitError:
        return "API quota or rate limit reached. Check your API usage."

    except APITimeoutError:
        return "The AI service took too long to respond. Please try again."

    except APIConnectionError:
        return "Could not connect to the AI service. Check your connection."

    except APIError as error:
        print(f"OpenAI API error: {error}")
        return "The AI service encountered an error. Please try again."
