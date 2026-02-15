import json
import os
import threading
import time

import requests
from dotenv import load_dotenv

from utility import log_message


BRAVE_API_BASE = "https://api.search.brave.com/res/v1"
_THROTTLE_LOCK = threading.Lock()
_LAST_REQUEST_TS = 0.0


def _throttle_if_needed() -> None:
    min_interval_ms = int(os.getenv("BRAVE_MIN_INTERVAL_MS", "1100"))
    if min_interval_ms <= 0:
        return
    min_interval_s = min_interval_ms / 1000.0
    global _LAST_REQUEST_TS
    with _THROTTLE_LOCK:
        now = time.monotonic()
        wait_for = min_interval_s - (now - _LAST_REQUEST_TS)
        if wait_for > 0:
            time.sleep(wait_for)
        _LAST_REQUEST_TS = time.monotonic()


def _retry_delay(attempt: int, response: requests.Response | None) -> float:
    retry_after = None
    if response is not None:
        retry_after = response.headers.get("Retry-After")
    if retry_after:
        try:
            return float(retry_after)
        except ValueError:
            pass
    base_delay = float(os.getenv("BRAVE_RETRY_BASE_SECONDS", "1.5"))
    max_delay = float(os.getenv("BRAVE_RETRY_MAX_SECONDS", "10"))
    return min(max_delay, base_delay * (2 ** attempt))


def _build_headers(api_key: str) -> dict:
    return {
        "Accept": "application/json",
        "X-Subscription-Token": api_key,
    }


def _get_api_key(api_key_env: str | None = None) -> str:
    load_dotenv()
    if api_key_env:
        api_key = os.getenv(api_key_env)
        if not api_key:
            raise ValueError(f"Missing {api_key_env} in .env")
        return api_key
    api_key = os.getenv("BRAVE_API_KEY") or os.getenv("BRAVE_SEARCH_API_KEY")
    if not api_key:
        raise ValueError("Missing BRAVE_API_KEY (or BRAVE_SEARCH_API_KEY) in .env")
    return api_key


def brave_request(endpoint: str, params: dict, api_key_env: str | None = None) -> dict:
    api_key = _get_api_key(api_key_env=api_key_env)
    url = f"{BRAVE_API_BASE}{endpoint}"
    log_message(f"Brave request: {url} | params: {params}")
    max_retries = int(os.getenv("BRAVE_MAX_RETRIES", "3"))
    for attempt in range(max_retries + 1):
        _throttle_if_needed()
        response = requests.get(url, headers=_build_headers(api_key), params=params, timeout=30)
        if response.status_code == 200:
            break
        if response.status_code in {429, 502, 503, 504} and attempt < max_retries:
            delay = _retry_delay(attempt, response)
            log_message(
                "Brave request rate-limited or unavailable; "
                f"retrying in {delay:.2f}s (attempt {attempt + 1}/{max_retries})"
            )
            time.sleep(delay)
            continue
        raise ValueError(f"Brave API error {response.status_code}: {response.text}")
    try:
        return response.json()
    except json.JSONDecodeError as exc:
        raise ValueError("Brave API response is not valid JSON") from exc
