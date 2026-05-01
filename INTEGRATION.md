# Integrating `huble-sdk-python` into your app

Field guide for plugging the SDK into common Python app shells. For the
API surface itself (`agent.chat`, `chat.completions`, errors, env vars),
see [README.md](README.md).

## 1. The shape of the integration

- The SDK is **sync**, urllib3-based.
- `LLMHub(...)` is cheap to construct but holds a `urllib3.PoolManager`
  internally — **reuse one instance per process** for connection pooling.
- Configuration precedence: explicit kwargs > `LLMHUB_*` env vars > defaults.
- Errors are typed: `AuthenticationError`, `RateLimitError(retry_after)`,
  `ValidationError`, `NotFoundError`, `ServerError`, `LLMHubError`.

## 2. Plain Python script / cron

Smallest case. Read config from env, build the client once, call.

```python
import os, time, logging
from llmhub import LLMHub, RateLimitError

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Reads LLMHUB_API_KEY / LLMHUB_BASE_URL from env when omitted.
client = LLMHub()

def chat(prompt: str) -> str:
    for attempt in (1, 2):
        try:
            r = client.chat.completions.create(
                model="deepseek-v3.2",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=512,
                timeout=30,
            )
            return r.choices[0].message.content or ""
        except RateLimitError as e:
            wait = e.retry_after or 30
            log.warning("rate-limited; sleeping %ss (attempt %d)", wait, attempt)
            time.sleep(wait)
    raise RuntimeError("rate-limit exceeded after retry")

if __name__ == "__main__":
    print(chat("Reply with: hello"))
```

## 3. FastAPI service

One client per process, attached to the app via the lifespan context, then
dependency-injected into routes.

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Request
from llmhub import LLMHub

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.huble = LLMHub()  # picks up LLMHUB_* env vars
    yield
    # No explicit close needed; PoolManager cleans up on GC.

app = FastAPI(lifespan=lifespan)

def get_huble(request: Request) -> LLMHub:
    return request.app.state.huble

@app.post("/chat")
def chat(prompt: str, client: LLMHub = Depends(get_huble)):
    r = client.chat.completions.create(
        model="deepseek-v3.2",
        messages=[{"role": "user", "content": prompt}],
    )
    return {"content": r.choices[0].message.content,
            "cost_usd": r.cost_usd, "model": r.model}
```

The SDK is sync. Under high concurrency, offload to a worker thread so
the event loop stays free:

```python
import asyncio
content = await asyncio.to_thread(
    client.chat.completions.create,
    model="deepseek-v3.2",
    messages=[{"role": "user", "content": prompt}],
)
```

## 4. Django service

Add config to `settings.py` (use `os.environ` or `django-environ` —
the SDK has no preference) and wrap the client behind a lazy accessor
so it isn't constructed at import time.

```python
# settings.py
import os
LLMHUB_API_KEY  = os.environ["LLMHUB_API_KEY"]
LLMHUB_BASE_URL = os.environ.get("LLMHUB_BASE_URL", "https://api.huble.app")
```

```python
# apps/llm/services.py
from django.conf import settings
from llmhub import LLMHub

_client: LLMHub | None = None

def get_huble() -> LLMHub:
    """Lazy singleton — settings must be loaded before first call."""
    global _client
    if _client is None:
        _client = LLMHub(
            api_key=settings.LLMHUB_API_KEY,
            base_url=settings.LLMHUB_BASE_URL,
        )
    return _client

def chat(prompt: str) -> str:
    r = get_huble().chat.completions.create(
        model="deepseek-v3.2",
        messages=[{"role": "user", "content": prompt}],
    )
    return r.choices[0].message.content or ""
```

Use it from a view or a management command:

```python
# apps/llm/views.py
from django.http import JsonResponse
from .services import chat

def chat_view(request):
    return JsonResponse({"reply": chat(request.GET["q"])})
```

```python
# apps/llm/management/commands/llm_smoke.py
from django.core.management.base import BaseCommand
from apps.llm.services import chat

class Command(BaseCommand):
    help = "Smoke-test the LLM provider"
    def handle(self, *args, **opts):
        self.stdout.write(chat("Reply with: ok"))
```

## 5. Odoo addon

Build the SDK client from your provider model's existing config fields,
cache it on the recordset (not at module level — Odoo registries reload
on module upgrade), and convert SDK exceptions to `UserError` at the
boundary so admins see actionable messages in the UI.

```python
from odoo import models, _
from odoo.exceptions import UserError
from llmhub import (
    LLMHub, AuthenticationError, RateLimitError,
    ValidationError, ServerError, LLMHubError,
)

class LLMProviderHuble(models.AbstractModel):
    _name = "llm.huble"
    _inherit = "llm.base"

    def _get_huble_client(self, llm_provider):
        """Cached per-recordset SDK client."""
        cache = getattr(self, "_huble_clients", None)
        if cache is None:
            cache = self._huble_clients = {}
        key = (llm_provider.id, llm_provider.x_endpoint, llm_provider.x_api_key)
        if key not in cache:
            api_key = (llm_provider.x_api_key or "").strip()
            if not api_key:
                raise UserError(_("API key is not configured on '%s'.") % llm_provider.display_name)
            cache[key] = LLMHub(
                api_key=api_key,
                base_url=llm_provider.x_endpoint or "https://api.huble.app",
            )
        return cache[key]

    def get_llm_response(self, llm_info=None, custom_llm_prompt=None,
                        file_content=False, llm_provider=None):
        client = self._get_huble_client(llm_provider)
        try:
            r = client.chat.completions.create(
                model=(llm_info or {}).get("model") or "deepseek-v3.2",
                messages=[{"role": "user", "content": custom_llm_prompt or ""}],
                max_tokens=int((llm_info or {}).get("max_tokens", 4096)),
                temperature=float((llm_info or {}).get("temperature", 0.7)),
            )
            return r.choices[0].message.content or ""
        except AuthenticationError:
            raise UserError(_("Huble rejected the API key."))
        except RateLimitError as e:
            raise UserError(_("Huble rate-limited; retry in %ss.") % (e.retry_after or 30))
        except (ValidationError, ServerError, LLMHubError) as e:
            raise UserError(_("Huble request failed: %s") % e)
```

See [`examples/odoo_addon_migration.py`](examples/odoo_addon_migration.py)
for a side-by-side before/after diff using raw `requests` vs the SDK.

## 6. Cross-cutting concerns

### Timeouts

Both `agent.chat(...)` and `chat.completions.create(...)` accept a
`timeout=` kwarg in seconds. Reasonable defaults:

- **30 s** for short single-turn chat.
- **120 s** for tool-use loops where the model may iterate.

### Retries

The SDK does **not** auto-retry. The minimum policy: on `RateLimitError`,
sleep `retry_after` and retry once. For 5xx, exponential backoff is the
caller's choice — for non-trivial cases, [`tenacity`](https://tenacity.readthedocs.io/)
handles this without adding a hard SDK dependency.

```python
from tenacity import retry, retry_if_exception_type, wait_exponential, stop_after_attempt
from llmhub import ServerError

@retry(retry=retry_if_exception_type(ServerError),
       wait=wait_exponential(multiplier=1, max=30),
       stop=stop_after_attempt(4))
def call(client, **kw):
    return client.chat.completions.create(**kw)
```

### Logging

The SDK logs nothing of its own. Wrap calls with your app's logger at
the points you care about:

```python
import logging
log = logging.getLogger(__name__)

r = client.chat.completions.create(model="...", messages=[...])
log.info("huble call: model=%s tokens=%s cost=%.6f",
         r.model, r.usage.total_tokens, r.cost_usd or 0.0)
```

### Testing / mocking

Patch the SDK method (or the underlying HTTP) to keep unit tests fast
and offline.

```python
from unittest.mock import patch, MagicMock
from llmhub.chat import ChatCompletion

def test_chat_handler():
    fake = ChatCompletion({
        "content": "ok", "stop_reason": "stop",
        "input_tokens": 1, "output_tokens": 1, "tokens_used": 2,
    })
    with patch("llmhub.chat._Completions.create", return_value=fake):
        result = my_handler(prompt="hi")
        assert result == "ok"
```

For lower-level control (asserting wire payloads), patch
`ChatOperations._http.request` and return a fake `urllib3` response —
see `tests/unit/test_chat.py` in this repo for the full pattern.
