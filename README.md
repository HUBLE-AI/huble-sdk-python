# HUBLE Python SDK (`llmhub`)

Official Python SDK for **HUBLE** (LLMHub) — a unified gateway to 18+ AI
providers including **Melious** (EU open-weight), **Claude**, **OpenAI**,
**Groq**, **Mistral**, **Google Gemini**, **Cohere**, **Ollama**, and more.

Single API surface for text, embeddings, documents, audio (TTS/STT),
video, images, moderation, enrichment, prompts, and data operations —
plus a **dual-shape agent endpoint** with tool-use and an **OpenAI SDK
drop-in** so existing OpenAI clients can swap `base_url` to HUBLE
without touching their code.

## Status

**Alpha (`0.2.0`)** — adoption-ready for Python integrators including the
internal NOCA Odoo addon collection. PyPI publication pending review.

## Installation

```bash
# From source (development)
git clone https://github.com/HUBLE-AI/huble-sdk-python.git
cd huble-sdk-python
pip install -e .
```

PyPI: _coming soon_ (`pip install llmhub`).

## Quick Start

```python
from llmhub import LLMHub

# Reads LLMHUB_API_KEY / LLMHUB_BASE_URL from env when omitted
client = LLMHub(api_key="mgw_...", base_url="https://api.huble.app")

response = client.text.generate(prompt="Write a haiku about coding")
print(response.content, response.cost_usd, response.provider_used)
```

## Agent endpoint with tool-use — `client.agent.chat()`

Multi-turn chat with **dual-shape input** — the SDK accepts either the
OpenAI message shape or the Anthropic content-blocks shape, and mirrors
the request shape on the response (or you can override via
`response_shape`). Tools are first-class and routed through HUBLE's
provider-agnostic tool layer.

```python
resp = client.agent.chat(
    messages=[{"role": "user", "content": "What's the weather in Hamburg?"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
            },
        },
    }],
    tool_choice="auto",
    provider="melious",          # default — EU-hosted, open weights, low cost
    model="deepseek-v3.2",       # default for Melious
)
print(resp.content)              # str (may be empty when tool-call goes first)
print(resp.tool_calls)           # [{"id":"call_x", "type":"function", ...}]
print(resp.stop_reason)          # "stop" | "tool_calls" | "length"
print(resp.cost_usd, resp.provider_metadata)
```

### Anthropic shape (auto-detected)

```python
resp = client.agent.chat(
    system="Be concise.",
    messages=[
        {"role": "user", "content": [{"type": "text", "text": "weather?"}]},
    ],
    tools=[{
        "name": "get_weather",
        "description": "Look up current weather",
        "input_schema": {"type": "object", "properties": {"city": {"type": "string"}}},
    }],
    tool_choice={"type": "auto"},
)
# resp.content is a list of content blocks, resp.stop_reason is "tool_use"
```

## OpenAI SDK drop-in — `client.chat.completions.create()`

Hits `/api/v2/chat/completions` and returns an OpenAI-shape
`ChatCompletion`. Code written for `openai.OpenAI()` can swap `base_url`
to your HUBLE host without changing response handling.

```python
resp = client.chat.completions.create(
    model="deepseek-v3.2",
    messages=[{"role": "user", "content": "hi"}],
    tools=[...],
    tool_choice="auto",
    temperature=0.7,
)
print(resp.choices[0].message.content)
print(resp.choices[0].message.tool_calls)        # nested attribute access
print(resp.choices[0].finish_reason)             # "stop" | "tool_calls" | "length"
print(resp.usage.prompt_tokens, resp.usage.total_tokens)
print(resp.cost_usd, resp.provider_used)         # HUBLE bookkeeping extras
```

The shape unwrapper is also exported as a pure helper for callers that
hit the API by hand:

```python
from llmhub import huble_to_openai_chat_completion
openai_shape = huble_to_openai_chat_completion(raw_dict_from_huble)
```

## Other operations

```python
client.text.generate(prompt="...")
client.text.translate(text="...", target_language="es")
client.text.summarize(text="...")
client.embeddings.generate(texts=["...", "..."])
client.document.parse(document="...")
client.document.extract(document="...", extract_fields=["invoice_number"])
client.audio.transcribe(audio="...")
client.image.generate(prompt="...")
client.moderation.analyze(content="...")
client.prompts.create(name="...", template="...")
client.discovery.get_models(provider="melious")
```

## Provider override

Every operation accepts `provider` and `model` overrides:

```python
client.text.generate(prompt="hi", provider="claude", model="claude-haiku-4-5")
client.agent.chat(messages=[...], provider="openai", model="gpt-4o-mini")
```

## Configuration

### Environment variables

```bash
export LLMHUB_API_KEY="mgw_..."
export LLMHUB_BASE_URL="https://api.huble.app"   # default: http://localhost:4000
```

### In code

```python
client = LLMHub(api_key="...", base_url="...")
```

Precedence: explicit args > `LLMHUB_*` env vars > defaults.

## Error handling

```python
from llmhub import (
    LLMHub, AuthenticationError, RateLimitError,
    NotFoundError, ValidationError, ServerError, LLMHubError,
)

try:
    client.agent.chat(messages=[{"role": "user", "content": "hi"}])
except RateLimitError as e:
    sleep(e.retry_after or 30)
except AuthenticationError:
    ...
except LLMHubError:
    ...
```

| Status   | Exception              |
|----------|------------------------|
| 401, 403 | `AuthenticationError`  |
| 404      | `NotFoundError`        |
| 422, 4xx | `ValidationError`      |
| 429      | `RateLimitError(retry_after=…)` |
| 5xx      | `ServerError`          |
| network  | `LLMHubError`          |

## Migration: replacing raw `requests` with the SDK

See [`examples/odoo_addon_migration.py`](examples/odoo_addon_migration.py)
for a side-by-side BEFORE / AFTER showing how to replace ~80 lines of raw
`requests.post(...)` + manual response unwrapping with three SDK calls.

## Requirements

- Python 3.9+
- HUBLE API key (V2 — `X-API-Key`)

## Development

See [DEVELOPMENT.md](DEVELOPMENT.md). Run tests with `pytest tests/`.

## License

MIT — see [LICENSE](LICENSE).

## Links

- **HUBLE backend**: <https://github.com/HUBLE-AI/llmhub>
- **This SDK**: <https://github.com/HUBLE-AI/huble-sdk-python>
