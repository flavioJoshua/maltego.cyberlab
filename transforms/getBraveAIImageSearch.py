import base64

import requests

from extensions import registry
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform

from Search.brave_ai import brave_request
from utility import log_message


def _get_prop(request: MaltegoMsg, *names: str) -> str | None:
    for name in names:
        value = request.TransformSettings.get(name) if request.TransformSettings else None
        if value is not None and (not isinstance(value, str) or value.strip() != ""):
            return value
        value = request.Properties.get(name)
        if value is None:
            continue
        if isinstance(value, str) and value.strip() == "":
            continue
        return value
    return None


def _clamp_int_param(params: dict[str, str], name: str, min_val: int, max_val: int) -> None:
    if name not in params:
        return
    try:
        value = int(params[name])
    except (TypeError, ValueError):
        log_message(f"Invalid {name} (not int): {params[name]}")
        params.pop(name, None)
        return
    if value < min_val:
        log_message(f"{name} too small ({value}), clamp to {min_val}")
        value = min_val
    if value > max_val:
        log_message(f"{name} too large ({value}), clamp to {max_val}")
        value = max_val
    params[name] = str(value)


@registry.register_transform(
    display_name="ICT Brave AI Image Search",
    input_entity="ICT.brave.request.image",
    description="Brave AI Image Search (REST) con output strutturato.",
    output_entities=["maltego.Image"],
)
class getBraveAIImageSearch(DiscoverableTransform):
    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
        log_message(f"Value: {request.Value} | Properties: {request.Properties}")

        query = _get_prop(request, "ICT.Brave.q", "ICT.Brave.query", "q", "query")
        query = query or request.Value
        api_key_env = _get_prop(request, "ICT.Brave.ApiKeyEnv")

        params: dict[str, str] = {}
        for key in ["count", "country", "search_lang"]:
            prop = _get_prop(request, f"ICT.Brave.{key}", key)
            if prop is not None:
                params[key] = str(prop)
        params["q"] = str(query)
        _clamp_int_param(params, "count", 1, 200)

        data = brave_request("/images/search", params, api_key_env=api_key_env)

        results = []
        if isinstance(data.get("images"), dict):
            results = data.get("images", {}).get("results", [])
        elif isinstance(data.get("results"), list):
            results = data.get("results", [])

        for result in results:
            if not isinstance(result, dict):
                continue
            url_value = result.get("url") or query
            entity = response.addEntity("maltego.Image", str(url_value))
            if result.get("url") is not None:
                entity.addProperty("url", value=str(result.get("url")))
            if result.get("title") is not None:
                entity.addProperty("title", value=str(result.get("title")))
            if result.get("description") is not None:
                entity.addProperty("description", value=str(result.get("description")))
            entity.addProperty("ICT.Brave.type.images", value="images")

            favicon = None
            meta_url = result.get("meta_url")
            if isinstance(meta_url, dict):
                favicon = meta_url.get("favicon")
            if favicon is not None:
                entity.addProperty("ICT.Brave.meta_url.favicon", value=str(favicon))

            thumbnail_url = None
            thumbnail = result.get("thumbnail")
            if isinstance(thumbnail, dict):
                thumbnail_url = thumbnail.get("src")
            if not thumbnail_url:
                thumbnail_url = result.get("thumbnail_url")
            _set_entity_icon(entity, thumbnail_url or result.get("url"))


def _set_entity_icon(entity, image_url: str | None) -> None:
    if not image_url:
        return
    try:
        encoded = _download_as_base64(image_url)
        if encoded:
            entity.addProperty("base64", value=encoded)
            entity.setIconURL(f"data:image/jpeg;base64,{encoded}")
    except Exception as exc:
        log_message(f"Icon error for {image_url}: {exc}")


def _download_as_base64(image_url: str, max_bytes: int = 100_000) -> str | None:
    response = requests.get(image_url, timeout=10, stream=True)
    if response.status_code != 200:
        return None

    data = bytearray()
    for chunk in response.iter_content(chunk_size=8192):
        if not chunk:
            continue
        data.extend(chunk)
        if len(data) > max_bytes:
            log_message(f"Image too large for base64 ({len(data)} bytes) {image_url}")
            return None

    encoded = base64.b64encode(bytes(data)).decode("ascii")
    return encoded
