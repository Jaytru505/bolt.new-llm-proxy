import logging
import json
import openai
from mitmproxy import http
from tiktoken import get_encoding

# Setup logging
logging.basicConfig(filename='llm_proxy.log', level=logging.INFO)

# OpenAI API Key (replace with your actual key)
openai.api_key = 'your-openai-api-key'

ENCODING = get_encoding("cl100k_base")
MAX_TOKENS = 8192

def process_openai_request(messages):
    """Send a request to OpenAI API."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def request(flow: http.HTTPFlow) -> None:
    """Handle HTTP requests."""
    if "chat/completions" in flow.request.url:
        messages = json.loads(flow.request.text)['messages']
        token_count = sum(len(ENCODING.encode(msg['content'])) for msg in messages)

        if token_count > MAX_TOKENS:
            response_text = process_openai_request(messages)
            flow.response = http.Response.make(
                200, json.dumps({"choices": [{"message": {"content": response_text}}]}),
                {"Content-Type": "application/json"}
            )
        else:
            flow.request.host = "127.0.0.1"
            flow.request.port = 2345