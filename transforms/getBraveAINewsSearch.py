import json
from typing import Any

from extensions import registry
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform

from Search.brave_ai import brave_request
from utility import log_message


def _to_str(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=True)
    return str(value)


def _flatten(prefix: str, obj: Any, out: dict) -> None:
    if obj is None:
        return
    if isinstance(obj, dict):
        for key, value in obj.items():
            next_prefix = f"{prefix}.{key}" if prefix else str(key)
            _flatten(next_prefix, value, out)
        return
    if isinstance(obj, list):
        out[prefix] = obj
        return
    out[prefix] = obj


def _add_properties(entity, data: dict, prefix: str) -> None:
    flat: dict[str, Any] = {}
    _flatten(prefix, data, flat)
    for key, value in flat.items():
        val = _to_str(value)
        if val is None or key == "":
            continue
        entity.addProperty(key, value=val)


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


def _build_params(request: MaltegoMsg, allowed: list[str]) -> dict:
    params: dict[str, str] = {}
    for key in allowed:
        prop = _get_prop(request, f"ICT.Brave.{key}", key)
        if prop is not None:
            params[key] = str(prop)
    return params


def _get_int_prop(request: MaltegoMsg, *names: str) -> int | None:
    value = _get_prop(request, *names)
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        log_message(f"Invalid int for {names}: {value}")
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


def _paginate_results(
    endpoint: str,
    base_params: dict[str, str],
    api_key_env: str | None,
    max_results: int,
    per_page: int,
    start_offset: int,
    top_key: str,
) -> list[dict]:
    results: list[dict] = []
    seen: set[str] = set()
    offset = start_offset
    while offset <= 9 and len(results) < max_results:
        params = dict(base_params)
        params["offset"] = str(offset)
        remaining = max_results - len(results)
        page_count = per_page if remaining > per_page else remaining
        params["count"] = str(page_count)
        data = brave_request(endpoint, params, api_key_env=api_key_env)
        page_results = _extract_results(data, top_key)
        log_message(f"Paged results offset={offset} count={len(page_results)}")
        if not page_results:
            break
        for result in page_results:
            if not isinstance(result, dict):
                continue
            url = result.get("url")
            if url:
                if url in seen:
                    continue
                seen.add(url)
            results.append(result)
        offset += 1
    return results


def _extract_results(data: dict, top_key: str | None) -> list[dict]:
    if top_key and isinstance(data.get(top_key), dict):
        results = data.get(top_key, {}).get("results")
        if isinstance(results, list):
            return results
    results = data.get("results")
    if isinstance(results, list):
        return results
    return []


def _add_result_entity(
    response: MaltegoTransform,
    result: dict,
    value_fallback: str,
    type_tag: str,
    entity_type: str,
) -> None:
    url_value = result.get("url") or value_fallback
    entity = response.addEntity(entity_type, str(url_value))
    log_message(f"Add result entity ({type_tag}): {url_value}")
    if result.get("url") is not None:
        entity.addProperty("url", value=str(result.get("url")))
    if result.get("title") is not None:
        entity.addProperty("title", value=str(result.get("title")))
    if result.get("description") is not None:
        entity.addProperty("description", value=str(result.get("description")))
    entity.addProperty(f"ICT.Brave.type.{type_tag}", value=str(type_tag))
    _add_properties(entity, result, "ICT.Brave")


@registry.register_transform(
    display_name="ICT Brave AI News Search",
    input_entity="ICT.brave.request",
    description="Brave AI News Search (REST) con output strutturato.",
    output_entities=["ICT.Brave.type.web"],
)
class getBraveAINewsSearch(DiscoverableTransform):
    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
        log_message(f"Value: {request.Value} | Properties: {request.Properties}")

        query = _get_prop(request, "ICT.Brave.q", "ICT.Brave.query", "q", "query")
        query = query or request.Value
        api_key_env = _get_prop(request, "ICT.Brave.ApiKeyEnv")

        params = _build_params(
            request,
            [
                "count",
                "offset",
                "freshness",
                "country",
                "search_lang",
                "extra_snippets",
                "goggles",
            ],
        )
        params["q"] = str(query)
        _clamp_int_param(params, "count", 1, 50)
        _clamp_int_param(params, "offset", 0, 9)

        max_results = _get_int_prop(request, "ICT.Brave.max_results", "max_results")
        if max_results and max_results > 0:
            per_page = _get_int_prop(request, "ICT.Brave.count", "count") or 50
            if per_page < 1:
                per_page = 1
            if per_page > 50:
                per_page = 50
            start_offset = _get_int_prop(request, "ICT.Brave.offset", "offset") or 0
            if start_offset < 0:
                start_offset = 0
            if start_offset > 9:
                start_offset = 9
            params.pop("offset", None)
            params.pop("count", None)
            results = _paginate_results(
                "/news/search",
                params,
                api_key_env,
                max_results,
                per_page,
                start_offset,
                "news",
            )
        else:
            data = brave_request("/news/search", params, api_key_env=api_key_env)
            results = _extract_results(data, "news")
        log_message(f"News results count: {len(results)}")
        for result in results:
            if isinstance(result, dict):
                _add_result_entity(response, result, str(query), "news", "ICT.Brave.type.web")
