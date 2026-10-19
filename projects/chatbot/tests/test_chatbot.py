
import json
from urllib import response
import llm_client
import httpx

from openai import (
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
)

from main import (
    contains_phrase,
    detect_intent,
    extract_name,
    generate_response,
    handle_command,
)


def test_contains_phrase():
    assert contains_phrase("hello there", "hello")
    assert not contains_phrase("shelloworld", "hello")


def test_detect_greeting():
    assert detect_intent("hello") == "greeting"


def test_extract_name():
    assert extract_name("my name is Jose") == "Jose"


def test_save_user_name(tmp_path, monkeypatch):     # Use tmp_path and monkeypatch to avoid writing to the actual file system
    monkeypatch.chdir(tmp_path)
    memory = {}

    response = generate_response("my name is Ana", memory)

    assert response == "Nice to meet you, Ana!"
    assert memory["name"] == "Ana"

    with open("memory.json", encoding="utf-8") as file:
        saved_memory = json.load(file)

    assert saved_memory["name"] == "Ana"


def test_recall_user_name():
    memory = {"name": "Jose"}

    response = generate_response("what is my name", memory)

    assert response == "Your name is Jose."


def test_exit_command(capsys):  # capsys is a pytest fixture that captures stdout and stderr
    history = []

    handled, updated_history = handle_command("exit", history)

    assert handled is True
    assert updated_history == history
    assert "See you soon!" in capsys.readouterr().out


def test_missing_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    response = llm_client.generate_llm_response("Hello")

    assert response == "OPENAI_API_KEY is not configured."


def test_successful_llm_response(monkeypatch):
    class FakeResponse:
        status = "completed"
        output_text = "Hello! How can I help?"

    class FakeResponses:
        def create(self, **kwargs):
            return FakeResponse()

    class FakeClient:
        def __init__(self, **kwargs):
            self.responses = FakeResponses()

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(llm_client, "OpenAI", FakeClient)

    response = llm_client.generate_llm_response("Hello")

    assert response == "Hello! How can I help?"


def test_empty_llm_response(monkeypatch):
    class FakeResponse:
        status = "completed"
        output_text = ""

    class FakeResponses:
        def create(self, **kwargs):
            return FakeResponse()

    class FakeClient:
        def __init__(self, **kwargs):
            self.responses = FakeResponses()

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(llm_client, "OpenAI", FakeClient)

    response = llm_client.generate_llm_response("Hello")

    assert response == (
        "The AI returned an empty response. Please try again."
    )


def test_incomplete_llm_response(monkeypatch):
    class FakeResponse:
        status = "incomplete"
        output_text = "Python is a programming language"

    class FakeResponses:
        def create(self, **kwargs):
            return FakeResponse()

    class FakeClient:
        def __init__(self, **kwargs):
            self.responses = FakeResponses()

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(llm_client, "OpenAI", FakeClient)

    response = llm_client.generate_llm_response("Explain Python")

    assert response.startswith("Python is a programming language")
    assert "[Response may be incomplete.]" in response



def test_authentication_error(monkeypatch):
    class FakeResponses:
        def create(self, **kwargs):
            response = httpx.Response(
                401,
                request=httpx.Request(
                    "POST", "https://api.openai.com/v1/responses"
                ),
            )
            raise AuthenticationError(
                "Invalid API key",  
                response=response,
                body=None,
            )

    class FakeClient:
        def __init__(self, **kwargs):
            self.responses = FakeResponses()

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(llm_client, "OpenAI", FakeClient)

    result = llm_client.generate_llm_response("Hello")

    assert result == "Authentication failed. Check your API key."


def test_rate_limit_error(monkeypatch):
    class FakeResponses:
        def create(self, **kwargs):
            response = httpx.Response(
                429,
                request=httpx.Request(
                    "POST", "https://api.openai.com/v1/responses"
                ),
            )
            raise RateLimitError(
                "Rate limit exceeded", 
                response=response,
                body=None,
            )

    class FakeClient:
        def __init__(self, **kwargs):
            self.responses = FakeResponses()

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(llm_client, "OpenAI", FakeClient)

    result = llm_client.generate_llm_response("Hello")

    assert result == (
        "API quota or rate limit reached. Check your API usage."
    )


def test_api_connection_error(monkeypatch):
    class FakeResponses:
        def create(self, **kwargs):
            request = httpx.Request(
                "POST", "https://api.openai.com/v1/responses"
            )
            raise APIConnectionError(
                message="Connection failed",
                request=request,
            )

    class FakeClient:
        def __init__(self, **kwargs):
            self.responses = FakeResponses()

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(llm_client, "OpenAI", FakeClient)

    result = llm_client.generate_llm_response("Hello")

    assert result == (
        "Could not connect to the AI service. Check your connection."
    )
