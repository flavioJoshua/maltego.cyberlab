# Maltego Cyberlab

Public version of Italian Cyber Team Tools for Maltego.  
This edition is a reduced package and does not include evaluative AI features from the full Italian Cyber Team Maltego package.

## Installation (before functions)
Complete the `Installation (step-by-step)` section below before using the `Implemented Functions (Cyberlab)` section.

## Implemented Functions (Cyberlab)
The updated transforms available in this Cyberlab build are:

1. `getgooglesearchimage` (`transforms/GetGoogleSearch.py`)
2. `getgooglesearch` (`transforms/GetGoogleSearch.py`)
3. `getarticle` (`transforms/getArticle.py`)
4. `getbraveaiimagesearch` (`transforms/getBraveAIImageSearch.py`)
5. `getbraveainewssearch` (`transforms/getBraveAINewsSearch.py`)
6. `getbraveaiwebsearch` (`transforms/getBraveAIWebSearch.py`)

## Premium Version Functions (not included in Cyberlab) (not Included on Free version CyberLab)
These AI functions are not included in this Cyberlab build:

1. `getaiv3` (`transforms/getAIV3.py`)
2. `getarticleaikgentity` (`transforms/getArticleAIKGEntity.py`)
3. `getarticleaikgphrase` (`transforms/getArticleAIKGPhrase.py`)

## Quick setup
```bash
conda env create -f /home/flavio/code/Osint/maltego/environment.yml -n maltego_v2
conda env update -n maltego_v2 -f /home/flavio/code/Osint/maltego/environment.yml --prune

python -m venv .venv
source .venv/bin/activate
pip install -r /home/flavio/code/Osint/maltego/requirements.txt
```

## Installation (step-by-step)

### 1) Clone repository
```bash
git clone https://github.com/flavioJoshua/maltego.cyberlab.git
cd maltego.cyberlab
```

### 2) Install Conda
#### Debian/Ubuntu
```bash
sudo apt update
sudo apt install -y wget bzip2
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda --version
```

#### Windows (PowerShell)
1. Download Miniconda from `https://docs.conda.io/en/latest/miniconda.html`.
2. Run installer (enable "Add Miniconda to PATH" only if allowed by your IT policy).
3. Open **Anaconda Prompt** or **PowerShell**.
4. Verify:
```powershell
conda --version
```

### 3) Create Conda environment (quick setup)
Run the quick setup commands:
```bash
conda env create -f /home/flavio/code/Osint/maltego/environment.yml -n maltego_v2
conda env update -n maltego_v2 -f /home/flavio/code/Osint/maltego/environment.yml --prune
```

Locate the created environment:
```bash
conda env list
```
You should see `maltego_v2` in the list.

### 4) (Optional) Local Python venv
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r /home/flavio/code/Osint/maltego/requirements.txt
```

## Import `.mtz` package and configure Maltego

### Import package `20260202_Entity_Transformation_NO_AI_V3.mtz`
1. Open Maltego Desktop.
2. Go to `Import/Export` -> `Import Configuration`.
3. Select file `20260202_Entity_Transformation_NO_AI_V3.mtz` from repository root.
4. Confirm import and restart Maltego if requested.
5. Verify that new ICT entities/transforms are visible in palette and local transform list.

### Import new entities and transforms (step-by-step)
1. Open `Manage` -> `Import/Export` -> `Import Configuration` for `.mtz` packages.
2. If you have an updated package, import the new `.mtz` the same way.
3. Open a new graph and search ICT entities (for example `ICT.brave.request`, `ICT.brave.request.image`, `ict.ArticleDetails`).
4. Drag entity into graph and check ICT transforms in context menu.
5. Execute one transform and validate output type (`maltego.URL`, `maltego.Image`, `ICT.Brave.type.web`, etc.).

### Customize `Command line` and `Working directory`
In Maltego local transform settings, for each local Python transform:
1. Open transform configuration.
2. Set `Command line` to the environment Python.
3. Set `Working directory` to cloned repository root.

Linux example:
- `Command line`: `/path/env/bin/python /path/repo/main.py`
- `Working directory`: `/path/repo`

Windows example:
- `Command line`: `C:\path\env\python.exe C:\path\repo\main.py`
- `Working directory`: `C:\path\repo`

### Quick configuration test (`ls`)
To validate settings:
1. In `Command line`, use environment Python and call `ls`, for example:
   `/pathenv/bin/python -c "import subprocess; subprocess.run(['ls'])"`
2. On Windows use:
   `C:\path\env\python.exe -c "import subprocess; subprocess.run(['cmd','/c','dir'])"`
3. In `Working directory`, set repository root (`pwd` of project root).
4. If output lists files such as `README.MD`, `transforms.csv`, `main.py`, directory setup is correct.

## Transform list to test
1. `getgooglesearchimage` -> `ICT Search Image by Google CSE ICT Label`
2. `getgooglesearch` -> `ICT Search by Google CSE ICT Label`
3. `getarticle` -> `ICT Article Details ICT Label`
4. `getbraveaiimagesearch` -> `ICT Brave AI Image Search ICT Label`
5. `getbraveainewssearch` -> `ICT Brave AI News Search ICT Label`
6. `getbraveaiwebsearch` -> `ICT Brave AI Web Search ICT Label`

## Full test plan (step-by-step)

### A) Google CSE base test (correct starting entity: `maltego.Phrase`)
1. Create a new graph.
2. Add entity `maltego.Phrase`.
3. Recommended test value: `Italian Cyber Team`.
4. Run `ICT Search by Google CSE ICT Label`.
5. Validate output: `maltego.URL` entities with coherent title/link.

Recommended phrases (ICT CSE Search):
- `Italian Cyber Team OSINT`
- `cyber threat intelligence italy`
- `digital forensics best practices`

### B) Google CSE image test (`maltego.Phrase`)
1. Duplicate or create new `maltego.Phrase`.
2. Recommended test value: `incident response team`.
3. Run `ICT Search Image by Google CSE ICT Label`.
4. Validate output: `maltego.Image`.

Recommended phrases (ICT CSE Search Image):
- `SOC analyst dashboard`
- `cyber security operation center`
- `threat hunting workflow`

### C) Article details test (`maltego.URL`)
1. Use a valid URL from test A.
2. Run `ICT Article Details ICT Label`.
3. Validate output: `ict.ArticleDetails` with title, text and metadata.

### D) Brave AI Web test (`ICT.brave.request`)
1. Add entity `ICT.brave.request`.
2. Test value: `critical infrastructure cybersecurity`.
3. (Optional) set `count=10`, `country=IT`, `search_lang=it`.
4. Run `ICT Brave AI Web Search ICT Label`.
5. Validate output: `ICT.Brave.type.web`.

### E) Brave AI News test (`ICT.brave.request`)
1. Use entity `ICT.brave.request`.
2. Test value: `ransomware europe`.
3. (Optional) set `freshness=pw`, `count=10`.
4. Run `ICT Brave AI News Search ICT Label`.
5. Validate output: `ICT.Brave.type.web` with recent news.

### F) Brave AI Image test (`ICT.brave.request.image`)
1. Add entity `ICT.brave.request.image`.
2. Test value: `data center security`.
3. (Optional) set `count=20`, `country=IT`, `search_lang=it`.
4. Run `ICT Brave AI Image Search ICT Label`.
5. Validate output: `maltego.Image`.

### G) Test acceptance criteria
1. No transform runtime errors.
2. Correct output entity type for each transform.
3. At least 3 relevant results per test case.
4. `audit.log` available for troubleshooting.

## Operational support (IT/EN)
- Email: `support@italiancyberteam.it`
- Languages: Italian and English.
- Targets: government entities, LEA (Law Enforcement Agencies), associates.
- Channels: Meet, Chat, AnyDesk.
- Contact support for: `.mtz` import issues, entity/transform mapping issues, `command line` and `working directory` tuning, Conda environment troubleshooting.

## OpenAI models (not Included on Free version CyberLab)
- gpt-5-search-api
- gpt-4o-search-preview
- gpt-4o-mini-search-preview
- gpt-5-mini
- gpt-5.2

### OpenAI models (general API pricing list, USD per 1M tokens)
| Model Name | Input ($) | Cached Input ($) | Output ($) |
|---|---:|---:|---:|
| gpt-5.2 (and Chat/Codex) | 1.75 | 0.175 | 14.00 |
| gpt-5.1 (and Chat/Codex) | 1.25 | 0.125 | 10.00 |
| gpt-5 (and Chat/Codex) | 1.25 | 0.125 | 10.00 |
| gpt-5-mini | 0.25 | 0.025 | 2.00 |
| gpt-5-nano | 0.05 | 0.005 | 0.40 |
| gpt-4.1 | 2.00 | 0.50 | 8.00 |
| gpt-4o | 2.50 | 1.25 | 10.00 |
| gpt-4.1-mini | 0.40 | 0.10 | 1.60 |
| gpt-4o-mini | 0.15 | 0.075 | 0.60 |

### Notes for your usage (Maltego/OSINT)
- **Cache efficiency**: for recursive investigations in Maltego, GPT-5 models provide a strong advantage on cached-input cost (typically 90% lower than standard input).
- **Speed vs cost**: `gpt-5-nano` is very competitive for fast entity extraction (`$0.05` input / 1M), often cheaper than previous mini/nano tiers.
- **Direct comparison**: versus `gpt-4.1-nano`, `gpt-5-nano` is typically around half the input cost.

### OpenAI web search: Chat Completions vs Responses
- **Chat Completions (`/v1/chat/completions`)**: web search is available only with search-specialized models:
  - `gpt-5-search-api`
  - `gpt-4o-search-preview`
  - `gpt-4o-mini-search-preview`
- **Responses (`/v1/responses`)**: web search is enabled via the `web_search` tool, but it is **not guaranteed for every model/configuration**.
  - Known limitation example: `gpt-5` with reasoning `minimal` does not support web search.
  - Known limitation example: `gpt-4.1-nano` does not support web search.
- **Web search context limit**: 128k tokens for retrieved search content.
- **Practical note for getAIV3**:
  - `openAI-response=true` -> uses Responses API.
  - `openAI-response=false` -> uses Chat Completions.
  - `OPENAI_WEB_SEARCH=true` is applied only in the OpenAI Responses branch.

## HF models (not Included on Free version CyberLab)
- google/gemma-3-12b-it:featherless-ai
- deepseek-ai/DeepSeek-R1:cheapest
- deepseek-ai/DeepSeek-V3.2:cheapest
- endpoint: https://router.huggingface.co/v1

https://generativelanguage.googleapis.com/v1beta/openai/



## Gemini Studio models (not Included on Free version CyberLab)

https://ai.google.dev/gemini-api/docs/models

## text-to-text only (recommended) (not Included on Free version CyberLab)
- gemini-3-pro-preview
- gemini-3-flash-preview
- gemini-2.5-pro
- gemini-2.5-flash
- gemini-2.5-flash-lite
- gemini-2.5-flash-preview-09-2025
- gemini-2.5-flash-lite-preview-09-2025

## legacy text-to-text (deprecated) (not Included on Free version CyberLab)
- gemini-2.0-flash
- gemini-2.0-flash-lite

### Gemini pricing tiers (only models listed above)
- **Free**: good for initial testing, lower limits, content may be used to improve Google products.
- **Paid**: for production, higher limits, context caching and batch, content not used to improve products.
- **Enterprise (Vertex AI)**: large-scale/compliance deployments, dedicated support, provisioned throughput, volume discounts.

### Gemini text-to-text pricing (USD per 1M tokens, Paid tier)
| Model | Standard Input | Standard Output | Batch Input | Batch Output | Context caching (input + storage) |
|---|---:|---:|---:|---:|---|
| gemini-3-pro-preview | $2.00 (<=200k) / $4.00 (>200k) | $12.00 (<=200k) / $18.00 (>200k) | $1.00 (<=200k) / $2.00 (>200k) | $6.00 (<=200k) / $9.00 (>200k) | $0.20 (<=200k) / $0.40 (>200k) + $4.50/h storage |
| gemini-3-flash-preview | $0.50 (text/image/video), $1.00 (audio) | $3.00 | $0.25 (text/image/video), $0.50 (audio) | $1.50 | $0.05 (text/image/video), $0.10 (audio) + $1.00/h storage |
| gemini-2.5-pro | $1.25 (<=200k) / $2.50 (>200k) | $10.00 (<=200k) / $15.00 (>200k) | $0.625 (<=200k) / $1.25 (>200k) | $5.00 (<=200k) / $7.50 (>200k) | $0.125 (<=200k) / $0.25 (>200k) + $4.50/h storage |
| gemini-2.5-flash | $0.30 (text/image/video), $1.00 (audio) | $2.50 | $0.15 (text/image/video), $0.50 (audio) | $1.25 | $0.03 (text/image/video), $0.10 (audio) + $1.00/h storage |
| gemini-2.5-flash-preview-09-2025 | $0.30 (text/image/video), $1.00 (audio) | $2.50 | $0.15 (text/image/video), $0.50 (audio) | $1.25 | $0.03 (text/image/video), $0.10 (audio) + $1.00/h storage |
| gemini-2.5-flash-lite | $0.10 (text/image/video), $0.30 (audio) | $0.40 | $0.05 (text/image/video), $0.15 (audio) | $0.20 | $0.01 (text/image/video), $0.03 (audio) + $1.00/h storage |
| gemini-2.5-flash-lite-preview-09-2025 | $0.10 (text/image/video), $0.30 (audio) | $0.40 | $0.05 (text/image/video), $0.15 (audio) | $0.20 | $0.01 (text/image/video), $0.03 (audio) + $1.00/h storage |
| gemini-2.0-flash (deprecated) | $0.10 (text/image/video), $0.70 (audio) | $0.40 | $0.05 (text/image/video), $0.35 (audio) | $0.20 | $0.025 (text/image/video), $0.175 (audio) + $1.00/h storage |
| gemini-2.0-flash-lite (deprecated) | $0.075 | $0.30 | $0.0375 | $0.15 | n/a |

### Practical notes (Maltego/OSINT)
- `gemini-2.5-flash-lite` and `gemini-2.5-flash-lite-preview-09-2025` are the cheapest for high-volume entity extraction.
- `gemini-2.5-pro` and `gemini-3-pro-preview` cost more but are stronger for complex reasoning and long documents.
- Batch is typically around 50% of standard token cost on most models.
- Grounding/search/maps rates can change: verify before production rollout.




## various providers (not Included on Free version CyberLab)
openai        OK
hf            OK
lightningai
gemini        OK
vertex
ollama        OK (local)

### How to fill properties for each provider
Format: **property name: YES/NO** - what it does - what happens if missing.

#### openai
- **ICT.AI.Provider: YES** - set `openai` (default if empty).  
  If empty: OpenAI is used.
- **ICT.AI.BaseURL: NO** - not required (official endpoints are used).
- **ICT.AI.ApiKeyEnv: NO** - if empty, uses `OPENAI_API_KEY` from `.env`.
- **ICT.Model_AI: YES** - model name.  
  Examples already listed above:
  - `gpt-5-search-api`
  - `gpt-4o-search-preview`
  - `gpt-4o-mini-search-preview`
  - `gpt-5-mini`
  - `gpt-5.2`
- **openAI-response (env): YES/NO** - `true` = Responses API, `false` = Chat Completions.  
  If undefined: default `false`.
- **OPENAI_WEB_SEARCH (env): YES/NO** - enables `web_search` only with Responses API.  
  If undefined: disabled.

#### gemini (AI Studio, OpenAI-like)
- **ICT.AI.Provider: YES** - `gemini`.
- **ICT.AI.BaseURL: YES** - Gemini OpenAI-like base URL.  
  Example already listed above: `https://generativelanguage.googleapis.com/v1beta/openai/`
- **ICT.AI.ApiKeyEnv: NO** - if empty, uses `GEMINI_API_KEY` from `.env`.
- **ICT.Model_AI: YES** - Gemini model name.  
  Examples already listed above:
  - `gemini-3-pro-preview`
  - `gemini-3-flash-preview`
  - `gemini-2.5-pro`
  - `gemini-2.5-flash`
  - `gemini-2.5-flash-lite`
- **Notes**: `frequency_penalty` and `presence_penalty` are **not** supported.

#### hf (Hugging Face OpenAI-like router)
- **ICT.AI.Provider: YES** - `hf`.
- **ICT.AI.BaseURL: YES** - e.g. `https://router.huggingface.co/v1`.
- **ICT.AI.ApiKeyEnv: NO** - if empty, uses `HF_TOKEN` from `.env`.
- **ICT.Model_AI: YES** - HF model name.  
  Examples already listed above:
  - `google/gemma-3-12b-it:featherless-ai`
  - `deepseek-ai/DeepSeek-R1:cheapest`
  - `deepseek-ai/DeepSeek-V3.2:cheapest`
- **Notes**: minimal call (`model + messages`), AI.* parameters are ignored.

#### lightningai (OpenAI-like)
- **ICT.AI.Provider: YES** - `lightningai`.
- **ICT.AI.BaseURL: YES** - OpenAI-like base URL provided by the vendor.
- **ICT.AI.ApiKeyEnv: NO** - if empty, uses `LIGHTNINGAI_API_KEY` from `.env`.
- **ICT.Model_AI: YES** - LightningAI model name (provider-specific).

#### vertex (Google Vertex AI, OpenAI-like)
- **ICT.AI.Provider: YES** - `vertex`.
- **ICT.AI.BaseURL: YES** - OpenAI-like base URL for your Vertex endpoint.
- **ICT.AI.ApiKeyEnv: YES/NO** - if set, used **as OAuth token**.  
  If empty: uses `GOOGLE_APPLICATION_CREDENTIALS` to generate the token.
- **ICT.Model_AI: YES** - Vertex model/endpoint name.

#### ollama (local)
- **ICT.AI.Provider: YES** - `ollama`.
- **ICT.AI.BaseURL: NO** - optional; default `http://localhost:11434/v1`.
- **ICT.AI.ApiKeyEnv: NO** - ignored (no API key needed).
- **ICT.Model_AI: YES** - locally installed Ollama model name.

## AI providers: possible cases and requirements (not Included on Free version CyberLab)
This section summarizes **all cases** supported by the `getAIV3` transform: providers, requirements, and choices.

### OpenAI possible choices
OpenAI can run in **2 modes**:
1) **Responses API** (modern)  
   - Enabled with `.env`: `openAI-response=true`
   - Supports `tools` such as `web_search` if `OPENAI_WEB_SEARCH=true`
   - Parameters: `temperature`, `top_p`, `max_output_tokens`, `frequency_penalty`, `presence_penalty`
2) **Chat Completions** (compatibility)  
   - Used if `openAI-response=false`
   - Parameters: `temperature`, `top_p`, `max_tokens`, `frequency_penalty`, `presence_penalty`

**OpenAI flags/choices:**
- `openAI-response=true|false`: Responses vs Chat Completions.
- `OPENAI_WEB_SEARCH=true|false`: enables `web_search` **only** with Responses API.
- Model (`ICT.Model_AI`) examples:
  - `gpt-4o-mini`
  - `gpt-5-mini`

### Providers and requirements
#### openai
- **BaseURL**: not required (optional).
- **API key**: `OPENAI_API_KEY`.
- **Status**: supported.

#### gemini (AI Studio, OpenAI‑like)
- **BaseURL**: required via `ICT.AI.BaseURL`.  
  Example: `https://generativelanguage.googleapis.com/v1beta/openai/`
- **API key**: `GEMINI_API_KEY`.
- **Notes**: OpenAI‑like format. `frequency_penalty` and `presence_penalty` are not supported.
- **Status**: supported (OpenAI‑like).

#### hf (Hugging Face OpenAI‑like router)
- **BaseURL**: required via `ICT.AI.BaseURL` (e.g. `https://router.huggingface.co/v1`).
- **API key**: `HF_API_KEY` or fallback `HF_TOKEN`.
- **Notes**: **minimal** call `model + messages`.
- **Status**: supported.

#### lightningai (OpenAI‑like)
- **BaseURL**: required via `ICT.AI.BaseURL`.
- **API key**: `LIGHTNINGAI_API_KEY` (or provider equivalent).
- **Status**: basic OpenAI‑like support (depends on provider).

#### vertex (Google Vertex AI, OpenAI‑like)
- **BaseURL**: required via `ICT.AI.BaseURL`.
- **API key**: OAuth token via `ICT.AI.ApiKeyEnv` **or** Service Account JSON (`GOOGLE_APPLICATION_CREDENTIALS`).
- **Notes**: if missing, the token is generated from the JSON file.
- **Status**: basic OpenAI‑like support (depends on model/endpoint).

#### ollama (local)
- **BaseURL**: optional. Default `http://localhost:11434/v1`.
- **API key**: not required (dummy key is used internally).
- **Status**: **actively developed and tested**.

## Brave Search API
You can use **either** the standard API key **or** the AI API key: queries work with both.
.env variables:
- `BRAVE_API_KEY`: Brave Search token
Optional fallback:
- `BRAVE_SEARCH_API_KEY`: alternate name for the same token
Per-transform override:
- `ICT.Brave.ApiKeyEnv`: name of the `.env` variable to use (same logic as getAIV3)

### Rate limit (429) when selecting multiple entities
The Free plan has a very low limit (typically 1 request/second). If you run multiple entities at once, Brave may return:
`Request rate limit exceeded`.

.env parameters to mitigate this (apply to **web/news/images**):
- `BRAVE_MIN_INTERVAL_MS` (default 1100): minimum delay between requests.
- `BRAVE_MAX_RETRIES` (default 3): automatic retries on 429/5xx.
- `BRAVE_RETRY_BASE_SECONDS` (default 1.5): backoff base.
- `BRAVE_RETRY_MAX_SECONDS` (default 10): maximum retry delay.

Note: restart the transform server/Maltego after changing these values.

Result differences:
- With a **standard** key you get the base fields (title/url/description/age/page_age/meta_url/thumbnail, etc.).
- With an **AI** key you may see **additional fields** (e.g. `extra_snippets`, summary/AI fields if your plan enables them).
- Structure is compatible: the transform stores any extra fields as `ICT.Brave.*` string properties.

Result limits and offset:
- **Web**: `count` max 20 per page. `offset` is the page index (0..9) → **max ~200 results** (10 pages).
- **News**: `count` max 50 per page. `offset` is the page index (0..9) → **max ~500 results** (10 pages).
- **Images**: `count` max 200 per request (no `offset` in this transform). Values above 200 are clamped to 200.
- To get more results, paginate by increasing `offset` (e.g., Web: 5 queries with `count=20` and `offset=0..4` → ~100 results).

### Brave parameters: examples and meaning
- `count`: results **per page**.  
  Example: `count=20` (Web) → 20 results per page.  
  Default: Brave API default (the transform does **not** set a value if you don’t).
- `offset`: **page index**, not number of results.  
  Example: `count=20`, `offset=3` → results ~61–80.  
  Range 0..9 (max 10 pages).
- `freshness`: time filter.  
  Examples: `freshness=pd` (last 24h), `pw` (last week), `pm` (last month), `py` (last year), or a range `2026-01-01to2026-01-31`.
- `country`: **region/country for ranking & localization**, not “country of origin” of sites.  
  Example: `country=IT` (results more relevant to Italy).  
  If omitted, Brave uses the **default for your account/IP**.
- `search_lang`: results language (ISO 639‑1).  
  Example: `search_lang=it` filters/ranks Italian results.  
  Not UI language (we don’t use `ui_lang` here).
- `extra_snippets`: if `true`, adds extra snippets per result.  
  Example: `extra_snippets=true` → `extra_snippets` property is filled.
- `goggles`: Brave custom ranking filters.  
  Example: `goggles=https://.../goggles.json` (if you have a ruleset).  
  Leave empty if you don’t use goggles.

## LOG
This section documents **how logging works**, **where logs go**, **which parameters affect logging**, and **what is logged** for each public Maltego transform.

### How it works
- All logs go through `utility.log_message(...)`.  
  `Search/utility.py` is just a wrapper that re-exports the same function.
- Each call appends a line to `audit.log` in the project root.
- Each line contains: **timestamp with milliseconds**, **caller file+function**, **message**.
- The message is also sent to the standard `maltego.server` logger (useful in the transform server).
- Note: `utility.py` writes **one log line on import** (`"Questo e un log con millisecondi."`).

### Where logs go
- Main file: `audit.log` (project root).  
  The path is computed in `utility.py` and always resolves to the project root, even if the log_file is relative.

### Parameters/controls for logging
There are **no global flags** to enable/disable logging.  
The only variables that affect logging content are Brave retry/limit settings (because they add log lines):
- `BRAVE_MIN_INTERVAL_MS`: throttling; does not log by itself, but affects timing and retries.
- `BRAVE_MAX_RETRIES`: number of retries (more retries => more logs).
- `BRAVE_RETRY_BASE_SECONDS` / `BRAVE_RETRY_MAX_SECONDS`: backoff; logged during retries.
AI-specific parameter:
- `logtokenMax` (env): `true|false`. If `true`, logs `usage` (tokens) and `finish_reason` when available.

### What gets logged per public transform (Maltego)
List of transforms registered with `@registry.register_transform` and **all logs they produce**.

#### ICT Query AI (V3) — `transforms/getAIV3.py`
Main logs:
- Type of `request.Properties` and full dump of `Properties` + `TransformSettings`.
- Selected provider, base URL, API key source, and flags `openAI-response` + `OPENAI_WEB_SEARCH`.
- Base URL normalization messages (e.g., Gemini fixups).
- Call parameters (model, temperature, top_p, max_tokens).
- For each attempt: **parameter keys**, success/failure, and error.
- Warning if output is empty.
- **Full response text** (`AI response text: ...`).
Notes:
- If `logtokenMax=true` (env), logs **usage/tokens** and **finish_reason** when present.
- For optimization, uses a max-token fallback cache at `transforms/fallback_tokenmax.txt`.

#### ICT Brave AI Web Search — `transforms/getBraveAIWebSearch.py`
Main logs:
- `Value` + `Properties`.
- Parsing errors for numeric parameters (`count`, `offset`, etc.).
- Clamping of out-of-range parameters.
- Pagination: `Paged results offset=... count=...`.
- Final results count.
- For each added entity: URL.

#### ICT Brave AI News Search — `transforms/getBraveAINewsSearch.py`
Main logs:
- `Value` + `Properties`.
- Parsing errors for numeric parameters.
- Clamping of out-of-range parameters.
- Pagination: `Paged results offset=... count=...`.
- Final results count.
- For each added entity: URL.

#### ICT Brave AI Image Search — `transforms/getBraveAIImageSearch.py`
Main logs:
- `Value` + `Properties`.
- Parsing/clamp errors for `count`.
- Icon download errors or image too large for base64.

#### ICT Article Details — `transforms/getArticle.py`
Main logs:
- `Value` + `Properties` + `TransformSettings`.
- Article title, full text, authors, publish date.
- Warning if article is empty.
- In `GetHTML_LXML`: title, summary, images, cleaned HTML, links.
Note: this transform can generate very large logs.

#### ICT Search by Google CSE — `transforms/GetGoogleSearch.py`
Main logs:
- `Value` + `Properties` + `TransformSettings`.
- CSE request URLs.
- **Full Google CSE JSON responses**.
- "Results for query ..." lines and any HTTP errors.
Note: very verbose logs (full JSON).

#### ICT Search Image by Google CSE — `transforms/GetGoogleSearch.py`
Main logs:
- Same as "ICT Search by Google CSE".

#### ICT DNS to IP — `transforms/DNSToIP.py`
Main logs:
- `Value` + `Properties` + `TransformSettings`.

#### ICT DNS to IP2 — `transforms/DNSToIP2.py`
Main logs:
- `Value` + `Properties` + `TransformSettings`.

#### ICT Greet Person — `transforms/GreetPerson.py`
Main logs:
- `Value` + `Properties` + `TransformSettings`.
- Exceptions (if any).

#### ICT Greet Person (localized) — `transforms/GreetPersonLocalized.py`
Main logs:
- **No logs** (does not call `log_message`).

#### ICT Overlay Example — `transforms/OverlayExample.py`
Main logs:
- Type of `request.Properties`.
- `Value` + `Properties` + `TransformSettings`.

#### ICT test phrase — `transforms/persontest2.py`
Main logs:
- `Value` + `Properties` + `TransformSettings`.

### Brave helper (used by Brave transforms)
`Search/brave_ai.py` adds logs for:
- Endpoint and parameters for each Brave request.
- Retries on 429/5xx with delay and attempt number.

### Privacy/volume
- Some transforms log **full text** (AI or articles) and/or **full JSON** (Google CSE).  
  To reduce logging you must change code (there are no global flags).
  
### Max-token fallback cache
The file `transforms/fallback_tokenmax.txt` stores provider/model pairs that failed with `max_tokens`/`max_output_tokens`.  
When present, the transform **skips** attempts that include those parameters.

### finish_reason: how to read it
- `stop`: response completed normally (not truncated).
- `length`: response truncated by token/max-token limit.

## getAIV3: providers, parameters and fallback (full explanation) (not Included on Free version CyberLab)
This section documents the behavior of the transform `transforms/getAIV3.py`.

### Entity properties (what to set in Maltego)
These properties are read by the transform:
- `ICT.Model_AI`: **model name** (examples):
  - `gpt-4o-mini`
  - `gemini-2.5-pro`
  - `llama3`
- `ICT.AI.Provider`: **provider** (`openai`, `hf`, `gemini`, `lightningai`, `vertex`, `ollama`).  
  Default: `openai` if missing.
- `ICT.AI.BaseURL`: **OpenAI‑like base URL** (required for non‑OpenAI providers).  
  Must be the **API root** (e.g. `https://router.huggingface.co/v1`, `http://localhost:11434/v1`).  
  Do not include `/chat/completions` or `/responses`.
- `ICT.AI.ApiKeyEnv`: **direct API key/token**.  
  Note: it is not an `.env` variable name. If set, it is used **as the token**.
- `ICT.1.ask`: **user prompt**.  
  If empty, the transform uses `request.Value` (or `text`).
- `text`: **system prompt / context**.
- `ICT.AI.Temperature`: creativity (0.0..1.0).
- `ICT.AI.Top`: top_p (0.0..1.0).
- `ICT.AI.MaxToken`: max generated tokens (1..100000).
- `ICT.AI.Frequency`: frequency_penalty (0.0..2.0).
- `ICT.AI.Presence_Penalty`: presence_penalty (0.0..2.0).
- `ICT.sentiment`: `Y/N` for sentiment analysis.
- `ICT.NLI`: `Y/N` for NLI.

### .env variables per provider
- **openai**: `OPENAI_API_KEY`, `openAI-response=true|false`, `OPENAI_WEB_SEARCH=true|false`
- **gemini**: `GEMINI_API_KEY`
- **hf**: `HF_TOKEN`
- **lightningai**: `LIGHTNINGAI_API_KEY`
- **vertex**: `GOOGLE_APPLICATION_CREDENTIALS` (Service Account JSON path)  
  Alternative: OAuth token via `ICT.AI.ApiKeyEnv`
- **ollama**: none (API key ignored; base URL optional)

### AI.* parameters supported (by provider)
Legend: **OK** = used; **NO** = ignored; **AUTO** = attempted but may fallback.
- **openai**: Temperature **OK**, Top **OK**, MaxToken **OK**, Frequency **OK**, Presence **OK**  
  (Responses API may reject some keys → automatic fallback)
- **gemini**: Temperature **OK**, Top **OK**, MaxToken **OK**, Frequency **NO**, Presence **NO**
- **hf**: **only** `model + messages` → all AI.* parameters **NO**
- **lightningai**: Temperature **AUTO**, Top **AUTO**, MaxToken **AUTO**, Frequency **AUTO**, Presence **AUTO**
- **vertex**: Temperature **AUTO**, Top **AUTO**, MaxToken **AUTO**, Frequency **AUTO**, Presence **AUTO**
- **ollama**: Temperature **AUTO**, Top **AUTO**, MaxToken **AUTO**, Frequency **NO**, Presence **NO**

### Supported providers and base URL
- **openai**: uses the official OpenAI endpoints. `ICT.AI.BaseURL` is optional.
- **hf** (Hugging Face OpenAI-like router): `ICT.AI.BaseURL` required (e.g. `https://router.huggingface.co/v1`).
- **lightningai**: `ICT.AI.BaseURL` required.
- **gemini** (AI Studio OpenAI-like): `ICT.AI.BaseURL` required.  
  If you accidentally set a documentation URL (`ai.google.dev`), the code normalizes it to `https://generativelanguage.googleapis.com/v1beta/openai/`.
- **vertex**: `ICT.AI.BaseURL` required. OAuth auth via Service Account.
- **ollama** (local): `ICT.AI.BaseURL` optional. If missing it uses `http://localhost:11434/v1`.

**Important (BaseURL):** provide **only the API root** (e.g. `http://localhost:11434/v1`), **not** the full endpoint.
The client automatically appends `/chat/completions` or `/responses` depending on the call.
Example:
- BaseURL to set: `http://localhost:11434/v1`
- Final endpoint used: `http://localhost:11434/v1/chat/completions`

### Which parameters are read by providers
Parameters come from Maltego properties:
`ICT.AI.Temperature`, `ICT.AI.Top`, `ICT.AI.MaxToken`, `ICT.AI.Frequency`, `ICT.AI.Presence_Penalty`.

The transform **always tries** to use the full set when possible, but it **falls back** automatically if the provider does not support them. In practice:
- **openai**: reads all parameters (temperature/top_p/max_tokens/frequency/presence).  
  In Responses mode it uses `max_output_tokens`.
- **lightningai**: treated as OpenAI-like -> tries all parameters, with fallback.
- **vertex**: treated as OpenAI-like -> tries all parameters, with fallback.
- **gemini**: **does not use** `frequency_penalty` and `presence_penalty` (removed).  
  Temperature/top_p/max_tokens OK (if supported by the model).
- **ollama**: **does not use** `frequency_penalty` and `presence_penalty` (removed).  
  Temperature/top_p/max_tokens are attempted, then fallback if the server rejects them.
- **hf**: **only** `model + messages`. No temperature/top_p/max_tokens/penalties.

> Note: if a parameter is not supported by the provider or model, the transform retries with a more minimal set (see fallback below).

### getAIV3 parameter ranges, meaning, and error handling
In the code (`transforms/getAIV3.py`), values are **cast** and **validated** before any API call.
If a value is out of range or not numeric, the transform **fails** with `ValueError` and **does not** call the API.

**Accepted ranges (hard checks):**
- `ICT.AI.Temperature`: **0.0 .. 1.0**  
  `0.0` = more deterministic output; `1.0` = more variability/creativity.
- `ICT.AI.Top` (top_p): **0.0 .. 1.0**  
  Lower = tighter sampling; higher = more variety.
- `ICT.AI.MaxToken`: **1 .. 100000**  
  Max tokens to generate (or `max_output_tokens` in Responses API).
- `ICT.AI.Frequency`: **0.0 .. 2.0**  
  Penalizes **frequent** repetitions (reduces loops).
- `ICT.AI.Presence_Penalty`: **0.0 .. 2.0**  
  Penalizes **repeating** existing concepts (encourages new topics).

**What happens with invalid values:**
- If the value is **not numeric** (e.g., a non‑convertible string), the `float()`/`int()` cast fails and the transform exits with error.
- If the value is **out of range**, a `ValueError` is raised with an explicit message (e.g., “Temperature should be between 0.0 and 1.0.”).
- There is **no automatic clamping**: fix the value in Maltego.

**Provider notes:**
- Even with valid values, some providers/models **don’t support** all parameters, so the transform retries with a minimal set (see fallback).
- For `hf`, even with valid parameters, it sends **only** `model + messages`.

### Dual OpenAI query mechanism
The transform can use **two different APIs** when `provider=openai`:

1) **Responses API** (modern)  
Enabled only if `.env` has `openAI-response=true`.
Uses:
```
model, input, instructions, temperature, top_p, max_output_tokens,
frequency_penalty, presence_penalty
```
If `OPENAI_WEB_SEARCH=true`, it adds `tools=[{"type":"web_search"}]` and `tool_choice="auto"`.

**Responses fallback (attempt order):**
1. `full` (all parameters)
2. `no_penalties` (removes frequency/presence)
3. `no_sampling` (removes temperature/top_p)
4. `defaults_only_max_output_tokens` (only model/input/instructions + max_output_tokens)
5. `defaults_only` (only model/input/instructions)
> If `web_search` is enabled, tools remain in all attempts.

2) **Chat Completions** (OpenAI-like compatible)  
Used when:
- `provider != openai`, **or**
- `openAI-response=false`.

**Chat Completions fallback (attempt order):**
For **hf**:
1. `defaults_only` -> only `model + messages`

For **other providers**:
1. `full` (model, messages, temperature, top_p, max_tokens, penalties)
2. `full_max_completion_tokens` (replaces `max_tokens` with `max_completion_tokens`)
3. `no_penalties` (removes frequency/presence)
4. `no_penalties_max_completion_tokens` (same + max_completion_tokens)
5. `defaults_only`
6. `defaults_only_max_tokens`
7. `defaults_only_max_completion_tokens`

### Parameter reuse (2nd query / sentiment / NLI)
When a parameter combination works, it is saved and reused:
- for `ICT.2.ask`
- for Sentiment (`ICT.sentiment=Y`)
- for NLI (`ICT.NLI=Y`)

This avoids new retries and keeps results consistent.

### .env variables used by getAIV3
Only these variables are read by the transform:
- `OPENAI_API_KEY`: OpenAI API key (provider=openai)
- `HF_TOKEN`: Hugging Face API key (provider=hf)
- `LIGHTNINGAI_API_KEY`: LightningAI API key
- `GEMINI_API_KEY`: Gemini AI Studio API key
- `GOOGLE_APPLICATION_CREDENTIALS`: path to the Service Account JSON (provider=vertex)
- `openAI-response`: `true|false` -> enable Responses API when provider=openai
- `OPENAI_WEB_SEARCH`: `true|false` -> enable web_search **only** with Responses API

Important notes:
- **Ollama does not require an API key**: the client uses an internal dummy key (`OLLAMA_DUMMY_API_KEY`), so no `.env` variable is needed.
- `ICT.AI.ApiKeyEnv` is **not** a `.env` variable name: it is the actual token passed by the Entity (has priority).


## how to use an image model (not Included on Free version CyberLab)

in user question:  Describe this image in one sentence:
in text (system)   "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"



## Debug
python project.py local greetperson "phrase=valore da scrivere"

python project.py local dnstoip "DNS=italiancyberteam.it"
local dnstoip "italiancyberteam.it"

put this in command parameters before the command:
-m debugpy --listen 5678 --wait-for-client

Full example:
python -m debugpy --listen 5678 --wait-for-client project.py runserver

then attach with the launch.json config

/home/flavio/.conda/envs/maltego/bin/python
/home/flavio/.conda/envs/maltego_v2/bin/python3

{
      "name": "Python: Attach  5678 ",
      "type": "python",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
}

## Future features
- Grounding with web search also for `gemini` provider (with safe fallback if the tool is not supported by endpoint/model).
