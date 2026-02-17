# Maltego  Cyberlab

è la versione  pubblica di Italian Cyber Team  Tools for Maltego.
questa  versione è la versione diminuita e senza AI valutativa del package  Italian Cyber Team  Maltego

## Funzioni Implementate (Cyberlab)
Le transform aggiornate e disponibili in questa versione sono:

1. `getgooglesearchimage` (`transforms/GetGoogleSearch.py`)
2. `getgooglesearch` (`transforms/GetGoogleSearch.py`)
3. `getarticle` (`transforms/getArticle.py`)
4. `getbraveaiimagesearch` (`transforms/getBraveAIImageSearch.py`)
5. `getbraveainewssearch` (`transforms/getBraveAINewsSearch.py`)
6. `getbraveaiwebsearch` (`transforms/getBraveAIWebSearch.py`)

## Funzioni Versione Premium (non incluse in Cyberlab)
Queste funzioni AI non sono incluse in questa build Cyberlab:

1. `getaiv3` (`transforms/getAIV3.py`)
2. `getarticleaikgentity` (`transforms/getArticleAIKGEntity.py`)
3. `getarticleaikgphrase` (`transforms/getArticleAIKGPhrase.py`)

## Setup rapido
```bash
conda env create -f /home/flavio/code/Osint/maltego/environment.yml -n maltego_v2
conda env update -n maltego_v2 -f /home/flavio/code/Osint/maltego/environment.yml --prune

python -m venv .venv
source .venv/bin/activate
pip install -r /home/flavio/code/Osint/maltego/requirements.txt
```

## model OpenAI
- gpt-5-search-api
- gpt-4o-search-preview
- gpt-4o-mini-search-preview
- gpt-5-mini
- gpt-5.2

### Modelli OpenAI (lista generale prezzi API, USD per 1M token)
| Nome Modello | Input ($) | Cached Input ($) | Output ($) |
|---|---:|---:|---:|
| gpt-5.2 (e Chat/Codex) | 1.75 | 0.175 | 14.00 |
| gpt-5.1 (e Chat/Codex) | 1.25 | 0.125 | 10.00 |
| gpt-5 (e Chat/Codex) | 1.25 | 0.125 | 10.00 |
| gpt-5-mini | 0.25 | 0.025 | 2.00 |
| gpt-5-nano | 0.05 | 0.005 | 0.40 |
| gpt-4.1 | 2.00 | 0.50 | 8.00 |
| gpt-4o | 2.50 | 1.25 | 10.00 |
| gpt-4.1-mini | 0.40 | 0.10 | 1.60 |
| gpt-4o-mini | 0.15 | 0.075 | 0.60 |

### Osservazioni per il tuo utilizzo (Maltego/OSINT)
- **Efficienza cache**: se fai indagini ricorsive su Maltego, la serie GPT-5 offre un vantaggio forte sul costo input in cache (sconto tipico 90% rispetto all'input standard).
- **Velocita vs costo**: `gpt-5-nano` e molto competitivo per estrazione rapida di entita (`$0.05` input / 1M), con costo inferiore a molti modelli mini/nano precedenti.
- **Confronto diretto**: rispetto a `gpt-4.1-nano`, `gpt-5-nano` risulta tipicamente circa alla meta del costo input.

### OpenAI web search: Chat Completions vs Responses
- **Chat Completions (`/v1/chat/completions`)**: web search disponibile solo con modelli search-specialized:
  - `gpt-5-search-api`
  - `gpt-4o-search-preview`
  - `gpt-4o-mini-search-preview`
- **Responses (`/v1/responses`)**: web search tramite tool `web_search`, ma **non e garantita su tutti i modelli/configurazioni**.
  - Esempio di limite noto: `gpt-5` con reasoning `minimal` non supporta web search.
  - Esempio di limite noto: `gpt-4.1-nano` non supporta web search.
- **Limite contesto web search**: 128k token di contesto per i contenuti di ricerca.
- **Nota pratica per getAIV3**:
  - `openAI-response=true` -> usa Responses API.
  - `openAI-response=false` -> usa Chat Completions.
  - `OPENAI_WEB_SEARCH=true` viene usato solo nel ramo Responses di OpenAI.

## model HF 
- google/gemma-3-12b-it:featherless-ai
- deepseek-ai/DeepSeek-R1:cheapest
- deepseek-ai/DeepSeek-V3.2:cheapest
- endpoint: https://router.huggingface.co/v1

https://generativelanguage.googleapis.com/v1beta/openai/



## model   Gemini Studio 

https://ai.google.dev/gemini-api/docs/models

## solo modelli text-to-text (consigliati)
- gemini-3-pro-preview
- gemini-3-flash-preview
- gemini-2.5-pro
- gemini-2.5-flash
- gemini-2.5-flash-lite
- gemini-2.5-flash-preview-09-2025
- gemini-2.5-flash-lite-preview-09-2025

## modelli text-to-text precedenti (deprecati)
- gemini-2.0-flash
- gemini-2.0-flash-lite

### Gemini pricing tiers (solo modelli in lista)
- **Free**: utile per test iniziali, limiti piu bassi, contenuti usati per migliorare i prodotti Google.
- **Paid**: per produzione, limiti maggiori, context caching e batch, contenuti non usati per migliorare i prodotti.
- **Enterprise (Vertex AI)**: per grandi volumi/compliance, supporto dedicato, throughput provisioned, sconti volume.

### Gemini text-to-text pricing (USD per 1M token, Paid tier)
| Modello | Standard Input | Standard Output | Batch Input | Batch Output | Context caching (input + storage) |
|---|---:|---:|---:|---:|---|
| gemini-3-pro-preview | $2.00 (<=200k) / $4.00 (>200k) | $12.00 (<=200k) / $18.00 (>200k) | $1.00 (<=200k) / $2.00 (>200k) | $6.00 (<=200k) / $9.00 (>200k) | $0.20 (<=200k) / $0.40 (>200k) + $4.50/h storage |
| gemini-3-flash-preview | $0.50 (text/image/video), $1.00 (audio) | $3.00 | $0.25 (text/image/video), $0.50 (audio) | $1.50 | $0.05 (text/image/video), $0.10 (audio) + $1.00/h storage |
| gemini-2.5-pro | $1.25 (<=200k) / $2.50 (>200k) | $10.00 (<=200k) / $15.00 (>200k) | $0.625 (<=200k) / $1.25 (>200k) | $5.00 (<=200k) / $7.50 (>200k) | $0.125 (<=200k) / $0.25 (>200k) + $4.50/h storage |
| gemini-2.5-flash | $0.30 (text/image/video), $1.00 (audio) | $2.50 | $0.15 (text/image/video), $0.50 (audio) | $1.25 | $0.03 (text/image/video), $0.10 (audio) + $1.00/h storage |
| gemini-2.5-flash-preview-09-2025 | $0.30 (text/image/video), $1.00 (audio) | $2.50 | $0.15 (text/image/video), $0.50 (audio) | $1.25 | $0.03 (text/image/video), $0.10 (audio) + $1.00/h storage |
| gemini-2.5-flash-lite | $0.10 (text/image/video), $0.30 (audio) | $0.40 | $0.05 (text/image/video), $0.15 (audio) | $0.20 | $0.01 (text/image/video), $0.03 (audio) + $1.00/h storage |
| gemini-2.5-flash-lite-preview-09-2025 | $0.10 (text/image/video), $0.30 (audio) | $0.40 | $0.05 (text/image/video), $0.15 (audio) | $0.20 | $0.01 (text/image/video), $0.03 (audio) + $1.00/h storage |
| gemini-2.0-flash (deprecato) | $0.10 (text/image/video), $0.70 (audio) | $0.40 | $0.05 (text/image/video), $0.35 (audio) | $0.20 | $0.025 (text/image/video), $0.175 (audio) + $1.00/h storage |
| gemini-2.0-flash-lite (deprecato) | $0.075 | $0.30 | $0.0375 | $0.15 | n/d |

### Note pratiche (Maltego/OSINT)
- `gemini-2.5-flash-lite` e `gemini-2.5-flash-lite-preview-09-2025` sono i piu economici per estrazione massiva entita.
- `gemini-2.5-pro` e `gemini-3-pro-preview` hanno costo alto ma rendono meglio su ragionamento complesso/documenti lunghi.
- Se usi batch, il costo token e circa il 50% dello standard nella maggior parte dei modelli.
- Le tariffe di grounding/search/maps possono cambiare: verifica sempre prima del deploy.




## vari provider
openai        OK 
hf            OK
lightningai
gemini        OK
vertex
ollama        OK (locale)

### Come compilare le proprieta per ogni provider
Formato: **nome prop: SI/NO** – cosa fa – cosa succede se manca.

#### openai
- **ICT.AI.Provider: SI** – imposta `openai` (default se vuoto).  
  Se vuoto: usa OpenAI.
- **ICT.AI.BaseURL: NO** – non serve (usa endpoint ufficiali).
- **ICT.AI.ApiKeyEnv: NO** – se vuoto usa `OPENAI_API_KEY` da `.env`.
- **ICT.Model_AI: SI** – nome modello.  
  Esempi gia presenti sopra:
  - `gpt-5-search-api`
  - `gpt-4o-search-preview`
  - `gpt-4o-mini-search-preview`
  - `gpt-5-mini`
  - `gpt-5.2`
- **openAI-response (env): SI/NO** – `true` = Responses API, `false` = Chat Completions.  
  Se non definito: default `false`.
- **OPENAI_WEB_SEARCH (env): SI/NO** – abilita `web_search` solo con Responses API.  
  Se non definito: disabilitato.

#### gemini (AI Studio, OpenAI‑like)
- **ICT.AI.Provider: SI** – `gemini`.
- **ICT.AI.BaseURL: SI** – base URL OpenAI‑like di Gemini.  
  Esempio gia presente sopra: `https://generativelanguage.googleapis.com/v1beta/openai/`
- **ICT.AI.ApiKeyEnv: NO** – se vuoto usa `GEMINI_API_KEY` da `.env`.
- **ICT.Model_AI: SI** – nome modello Gemini.  
  Esempi gia presenti sopra:
  - `gemini-3-pro-preview`
  - `gemini-3-flash-preview`
  - `gemini-2.5-pro`
  - `gemini-2.5-flash`
  - `gemini-2.5-flash-lite`
- **Note**: `frequency_penalty` e `presence_penalty` **non** supportate.

#### hf (Hugging Face router OpenAI‑like)
- **ICT.AI.Provider: SI** – `hf`.
- **ICT.AI.BaseURL: SI** – es. `https://router.huggingface.co/v1`.
- **ICT.AI.ApiKeyEnv: NO** – se vuoto usa `HF_TOKEN` da `.env`.
- **ICT.Model_AI: SI** – nome modello HF.  
  Esempi gia presenti sopra:
  - `google/gemma-3-12b-it:featherless-ai`
  - `deepseek-ai/DeepSeek-R1:cheapest`
  - `deepseek-ai/DeepSeek-V3.2:cheapest`
- **Note**: chiamata minimal (`model + messages`), parametri AI.* ignorati.

#### lightningai (OpenAI‑like)
- **ICT.AI.Provider: SI** – `lightningai`.
- **ICT.AI.BaseURL: SI** – base URL OpenAI‑like fornito dal provider.
- **ICT.AI.ApiKeyEnv: NO** – se vuoto usa `LIGHTNINGAI_API_KEY` da `.env`.
- **ICT.Model_AI: SI** – nome modello LightningAI (dipende dal provider).

#### vertex (Google Vertex AI, OpenAI‑like)
- **ICT.AI.Provider: SI** – `vertex`.
- **ICT.AI.BaseURL: SI** – base URL OpenAI‑like del tuo endpoint Vertex.
- **ICT.AI.ApiKeyEnv: SI/NO** – se valorizzato, usato **come token OAuth**.  
  Se vuoto: usa `GOOGLE_APPLICATION_CREDENTIALS` per generare il token.
- **ICT.Model_AI: SI** – nome modello/endpoint Vertex.

#### ollama (locale)
- **ICT.AI.Provider: SI** – `ollama`.
- **ICT.AI.BaseURL: NO** – opzionale; default `http://localhost:11434/v1`.
- **ICT.AI.ApiKeyEnv: NO** – ignorato (non serve API key).
- **ICT.Model_AI: SI** – nome modello locale installato in Ollama.

## Provider AI: casi possibili e requisiti
Questa sezione riassume **tutti i casi** supportati dal transform `getAIV3`: provider, requisiti e scelte.

### Scelte possibili per OpenAI
OpenAI può lavorare in **2 modalità**:
1) **Responses API** (moderna)  
   - Attiva con `.env`: `openAI-response=true`
   - Supporta `tools` come `web_search` se `OPENAI_WEB_SEARCH=true`
   - Parametri: `temperature`, `top_p`, `max_output_tokens`, `frequency_penalty`, `presence_penalty`
2) **Chat Completions** (compatibilità)  
   - Usata se `openAI-response=false`
   - Parametri: `temperature`, `top_p`, `max_tokens`, `frequency_penalty`, `presence_penalty`

**Scelte/flag OpenAI:**
- `openAI-response=true|false`: Responses vs Chat Completions.
- `OPENAI_WEB_SEARCH=true|false`: abilita `web_search` **solo** con Responses API.
- Modello (`ICT.Model_AI`) esempio:
  - `gpt-4o-mini`
  - `gpt-5-mini`

### Provider e requisiti
#### openai
- **BaseURL**: non serve (opzionale).
- **API key**: `OPENAI_API_KEY`.
- **Stato**: supportato.

#### gemini (AI Studio, OpenAI‑like)
- **BaseURL**: obbligatorio via `ICT.AI.BaseURL`.  
  Esempio: `https://generativelanguage.googleapis.com/v1beta/openai/`
- **API key**: `GEMINI_API_KEY`.
- **Note**: formato OpenAI‑like. `frequency_penalty` e `presence_penalty` non sono supportate.
- **Stato**: supportato (OpenAI‑like).

#### hf (Hugging Face router OpenAI‑like)
- **BaseURL**: obbligatorio via `ICT.AI.BaseURL` (es. `https://router.huggingface.co/v1`).
- **API key**: `HF_API_KEY` o fallback `HF_TOKEN`.
- **Note**: chiamata **minimal** `model + messages`.
- **Stato**: supportato.

#### lightningai (OpenAI‑like)
- **BaseURL**: obbligatorio via `ICT.AI.BaseURL`.
- **API key**: `LIGHTNINGAI_API_KEY` (o variabile equivalente del provider).
- **Stato**: supporto base OpenAI‑like (dipende dal provider).

#### vertex (Google Vertex AI, OpenAI‑like)
- **BaseURL**: obbligatorio via `ICT.AI.BaseURL`.
- **API key**: token OAuth via `ICT.AI.ApiKeyEnv` **oppure** Service Account JSON (`GOOGLE_APPLICATION_CREDENTIALS`).
- **Note**: se manca il token, prova a generarlo dal JSON.
- **Stato**: supporto base OpenAI‑like (dipende dal modello/endpoint).

#### ollama (locale)
- **BaseURL**: opzionale. Default `http://localhost:11434/v1`.
- **API key**: non richiesta (usa dummy interno).
- **Stato**: **sviluppato e testato attivamente**.

## Brave Search API
Puoi usare **sia** la API key standard **sia** la API key AI: le query funzionano con entrambe.
Variabili `.env`:
- `BRAVE_API_KEY`: token Brave Search
Fallback opzionale:
- `BRAVE_SEARCH_API_KEY`: secondo nome per lo stesso token
Override per trasformata:
- `ICT.Brave.ApiKeyEnv`: nome della variabile `.env` da usare (stessa logica di getAIV3)

### Rate limit (errore 429) quando lanci piu entita insieme
Il piano Free ha un limite molto basso (tipicamente 1 richiesta/secondo). Se selezioni piu entita in contemporanea, Brave puo rispondere con:
`Request rate limit exceeded`.

Parametri `.env` per ridurre il problema (valgono per **web/news/images**):
- `BRAVE_MIN_INTERVAL_MS` (default 1100): delay minimo tra le richieste.
- `BRAVE_MAX_RETRIES` (default 3): numero di retry automatici su 429/5xx.
- `BRAVE_RETRY_BASE_SECONDS` (default 1.5): base del backoff.
- `BRAVE_RETRY_MAX_SECONDS` (default 10): massimo delay tra retry.

Nota: dopo aver cambiato questi valori, riavvia il server dei transform/Maltego.

Differenze nei risultati:
- Con key **standard** ottieni i campi base (title/url/description/age/page_age/meta_url/thumbnail, ecc.).
- Con key **AI** possono comparire **campi aggiuntivi** (es. `extra_snippets`, summary/AI fields se abilitati dal piano).
- La struttura è compatibile: il transform aggiunge tutte le proprietà presenti in risposta come `ICT.Brave.*` (string).

Limiti risultati e offset:
- **Web**: `count` massimo 20 per pagina. `offset` è il numero di pagina (0..9) → **max ~200 risultati** (10 pagine).
- **News**: `count` massimo 50 per pagina. `offset` è il numero di pagina (0..9) → **max ~500 risultati** (10 pagine).
- **Images**: `count` massimo 200 per richiesta (niente `offset` nel transform). Se imposti un valore maggiore, viene clampato a 200.
- Per ottenere più risultati si paginano le richieste aumentando `offset` (es. Web: 5 query con `count=20` e `offset=0..4` → ~100 risultati).

### Parametri Brave: esempi e significato
- `count`: quanti risultati **per pagina**.  
  Esempio: `count=20` (Web) → 20 risultati per pagina.  
  Default: usa il default dell’API Brave (il transform **non** imposta un valore se non lo specifichi).
- `offset`: **indice pagina**, non numero risultati.  
  Esempio: `count=20`, `offset=3` → risultati ~61–80.  
  Range 0..9 (max 10 pagine).
- `freshness`: filtro tempo.  
  Esempi: `freshness=pd` (last 24h), `pw` (last week), `pm` (last month), `py` (last year), oppure range `2026-01-01to2026-01-31`.
- `country`: **regione/paese per ranking e localizzazione**, non “paese di origine” dei siti.  
  Esempio: `country=IT` (risultati più rilevanti per Italia).  
  Se non lo specifichi, Brave usa il **default del tuo account/IP**.
- `search_lang`: lingua dei risultati (ISO 639‑1).  
  Esempio: `search_lang=it` filtra/rank risultati in italiano.  
  Non è la lingua della UI (per quella servirebbe `ui_lang`, che qui non usiamo).
- `extra_snippets`: se `true`, aggiunge snippet aggiuntivi per ogni risultato.  
  Esempio: `extra_snippets=true` → proprietà `extra_snippets` piena.
- `goggles`: filtri di ranking personalizzati di Brave.  
  Esempio: `goggles=https://.../goggles.json` (se hai un set di regole).  
  Se non usi goggles, lascia vuoto.

## LOG
Questa sezione documenta **come funzionano i log**, **dove finiscono**, **quali parametri li influenzano** e **cosa viene loggato** per ogni transform pubblico di Maltego.

### Come funzionano
- Tutti i log passano da `utility.log_message(...)`.  
  In `Search/utility.py` c'e solo un wrapper che re‑esporta la stessa funzione.
- Ogni chiamata scrive una riga in `audit.log` nella root del progetto.
- Ogni riga contiene: **timestamp con millisecondi**, **file+funzione chiamante**, **messaggio**.
- Il messaggio viene anche inviato al logger standard `maltego.server` (utile nel server dei transform).
- Nota: `utility.py` scrive **una riga di log all'import** (`"Questo e un log con millisecondi."`).

### Dove finiscono
- File principale: `audit.log` (root progetto).  
  Percorso effettivo: viene calcolato da `utility.py` e risulta sempre nella root del progetto, anche se il log_file e relativo.

### Parametri/controlli per il log
**Non esistono flag globali** per abilitare/disabilitare i log.  
Le uniche variabili che influenzano il contenuto dei log sono quelle legate ai retry/limiti Brave (perche generano log aggiuntivi):
- `BRAVE_MIN_INTERVAL_MS`: applica throttling; non scrive di per se, ma influisce su tempi e retry.
- `BRAVE_MAX_RETRIES`: numero di retry (piu retry => piu log).
- `BRAVE_RETRY_BASE_SECONDS` / `BRAVE_RETRY_MAX_SECONDS`: backoff; loggati durante i retry.
Parametri specifici per AI:
- `logtokenMax` (env): `true|false`. Se `true`, logga `usage` (token) e `finish_reason` quando disponibili.

### Cosa viene loggato per ogni transform pubblico (Maltego)
Elenco dei transform con `@registry.register_transform` e **tutti i log prodotti**.

#### ICT Query AI (V3) — `transforms/getAIV3.py`
Log principali:
- Tipo di `request.Properties` e dump completo di `Properties` + `TransformSettings`.
- Provider selezionato, base URL, API key da proprieta/env, stato dei flag `openAI-response` e `OPENAI_WEB_SEARCH`.
- Messaggi di normalizzazione base URL (es. correzione Gemini).
- Parametri di chiamata (model, temperature, top_p, max_tokens).
- Per ogni tentativo: **chiavi dei parametri**, esito success/fail e errore.
- Warning se output vuoto.
- **Testo completo della risposta** (`AI response text: ...`).
Note:
- Se `logtokenMax=true` (env), logga **usage/token** e **finish_reason** quando presenti.
- Per ottimizzare, usa una cache di fallback su max token in `transforms/fallback_tokenmax.txt`.

#### ICT Brave AI Web Search — `transforms/getBraveAIWebSearch.py`
Log principali:
- `Value` + `Properties`.
- Errori di parsing per parametri numerici (`count`, `offset`, ecc.).
- Clamp dei parametri fuori range.
- Paginazione: `Paged results offset=... count=...`.
- Conteggio risultati finali.
- Per ogni entita aggiunta: URL.

#### ICT Brave AI News Search — `transforms/getBraveAINewsSearch.py`
Log principali:
- `Value` + `Properties`.
- Errori di parsing per parametri numerici.
- Clamp dei parametri fuori range.
- Paginazione: `Paged results offset=... count=...`.
- Conteggio risultati finali.
- Per ogni entita aggiunta: URL.

#### ICT Brave AI Image Search — `transforms/getBraveAIImageSearch.py`
Log principali:
- `Value` + `Properties`.
- Errori di parsing/clamp del parametro `count`.
- Errori nel download dell'icona o immagine troppo grande per base64.

#### ICT Article Details — `transforms/getArticle.py`
Log principali:
- `Value` + `Properties` + `TransformSettings`.
- Titolo articolo, testo completo, autori, data pubblicazione.
- Warning se articolo vuoto.
- In `GetHTML_LXML`: titolo, testo (summary), immagini, HTML pulito, link.
Attenzione: questo transform puo produrre log molto grandi.

#### ICT Search by Google CSE — `transforms/GetGoogleSearch.py`
Log principali:
- `Value` + `Properties` + `TransformSettings`.
- URL delle richieste CSE.
- **Intera risposta JSON** di Google CSE.
- Riga "Results for query ..." e gli eventuali errori HTTP.
Attenzione: log voluminosi (JSON completo).

#### ICT Search Image by Google CSE — `transforms/GetGoogleSearch.py`
Log principali:
- Identici a "ICT Search by Google CSE".

#### ICT DNS to IP — `transforms/DNSToIP.py`
Log principali:
- `Value` + `Properties` + `TransformSettings`.

#### ICT DNS to IP2 — `transforms/DNSToIP2.py`
Log principali:
- `Value` + `Properties` + `TransformSettings`.

#### ICT Greet Person — `transforms/GreetPerson.py`
Log principali:
- `Value` + `Properties` + `TransformSettings`.
- Eccezioni (se presenti).

#### ICT Greet Person (localized) — `transforms/GreetPersonLocalized.py`
Log principali:
- **Nessun log** (non chiama `log_message`).

#### ICT Overlay Example — `transforms/OverlayExample.py`
Log principali:
- Tipo di `request.Properties`.
- `Value` + `Properties` + `TransformSettings`.

#### ICT test phrase — `transforms/persontest2.py`
Log principali:
- `Value` + `Properties` + `TransformSettings`.

### Brave helper (usato dai transform Brave)
`Search/brave_ai.py` aggiunge log aggiuntivi per:
- Endpoint e parametri di ogni richiesta Brave.
- Retry su 429/5xx con delay e numero tentativo.

### Privacy/volume
- Alcuni transform loggano **testo completo** (AI o articoli) e/o **JSON completi** (Google CSE).  
  Se vuoi ridurre i log, bisogna modificare il codice (non ci sono flag globali).
  
### Cache fallback max token
Il file `transforms/fallback_tokenmax.txt` memorizza i provider/modelli che hanno fallito con `max_tokens`/`max_output_tokens`.  
Quando presente, il transform **salta direttamente** i tentativi che includono quei parametri.

### finish_reason: come interpretarlo
- `stop`: risposta completata normalmente (non troncata).
- `length`: risposta troncata per limite token/max token.

## getAIV3: provider, parametri e fallback (spiegazione completa)
Questa sezione documenta il comportamento del transform `transforms/getAIV3.py`.

### Proprietà dell'entità (cosa mettere in Maltego)
Queste proprietà vengono lette dal transform:
- `ICT.Model_AI`: **nome modello** (esempi):
  - `gpt-4o-mini`
  - `gemini-2.5-pro`
  - `llama3`
- `ICT.AI.Provider`: **provider** (`openai`, `hf`, `gemini`, `lightningai`, `vertex`, `ollama`).  
  Default: `openai` se mancante.
- `ICT.AI.BaseURL`: **base URL OpenAI‑like** (solo per provider non‑OpenAI).  
  Deve essere la **root** API (es. `https://router.huggingface.co/v1`, `http://localhost:11434/v1`).  
  Non inserire `/chat/completions` o `/responses`.
- `ICT.AI.ApiKeyEnv`: **API key/token diretto**.  
  Nota: non è un nome di variabile `.env`. Se valorizzato, viene usato **come token**.
- `ICT.1.ask`: **testo utente** (prompt).  
  Se vuoto, il transform usa `request.Value` (o `text`).
- `text`: **system prompt / contesto**.
- `ICT.AI.Temperature`: creatività (0.0..1.0).
- `ICT.AI.Top`: top_p (0.0..1.0).
- `ICT.AI.MaxToken`: max token generati (1..100000).
- `ICT.AI.Frequency`: frequency_penalty (0.0..2.0).
- `ICT.AI.Presence_Penalty`: presence_penalty (0.0..2.0).
- `ICT.sentiment`: `Y/N` per analisi sentiment.
- `ICT.NLI`: `Y/N` per NLI.

### .env: variabili per provider
- **openai**: `OPENAI_API_KEY`, `openAI-response=true|false`, `OPENAI_WEB_SEARCH=true|false`
- **gemini**: `GEMINI_API_KEY`
- **hf**: `HF_TOKEN`
- **lightningai**: `LIGHTNINGAI_API_KEY`
- **vertex**: `GOOGLE_APPLICATION_CREDENTIALS` (path JSON Service Account)  
  Alternativa: token OAuth via `ICT.AI.ApiKeyEnv`
- **ollama**: nessuna (API key ignorata; base URL opzionale)

### Parametri AI.* supportati (per provider)
Legenda: **OK** = usato; **NO** = ignorato; **AUTO** = provato ma può fare fallback.
- **openai**: Temperature **OK**, Top **OK**, MaxToken **OK**, Frequency **OK**, Presence **OK**  
  (Responses API può rifiutare alcune chiavi → fallback automatico)
- **gemini**: Temperature **OK**, Top **OK**, MaxToken **OK**, Frequency **NO**, Presence **NO**
- **hf**: **solo** `model + messages` → tutti i parametri AI.* **NO**
- **lightningai**: Temperature **AUTO**, Top **AUTO**, MaxToken **AUTO**, Frequency **AUTO**, Presence **AUTO**
- **vertex**: Temperature **AUTO**, Top **AUTO**, MaxToken **AUTO**, Frequency **AUTO**, Presence **AUTO**
- **ollama**: Temperature **AUTO**, Top **AUTO**, MaxToken **AUTO**, Frequency **NO**, Presence **NO**

### Provider supportati e URL base
- **openai**: usa gli endpoint OpenAI ufficiali. `ICT.AI.BaseURL` è opzionale.
- **hf** (Hugging Face router OpenAI‑like): `ICT.AI.BaseURL` obbligatorio (es. `https://router.huggingface.co/v1`).
- **lightningai**: `ICT.AI.BaseURL` obbligatorio.
- **gemini** (AI Studio OpenAI‑like): `ICT.AI.BaseURL` obbligatorio.  
  Se per errore metti un URL della documentazione (`ai.google.dev`), il codice lo normalizza automaticamente in `https://generativelanguage.googleapis.com/v1beta/openai/`.
- **vertex**: `ICT.AI.BaseURL` obbligatorio. Autenticazione OAuth via Service Account.
- **ollama** (locale): `ICT.AI.BaseURL` opzionale. Se mancante usa `http://localhost:11434/v1`.

**Importante (BaseURL):** inserisci **solo la root** dell'API (es. `http://localhost:11434/v1`), **non** l'endpoint completo.
Il client aggiunge automaticamente `/chat/completions` o `/responses` in base alla chiamata.
Esempio:
- BaseURL da inserire: `http://localhost:11434/v1`
- Endpoint finale usato: `http://localhost:11434/v1/chat/completions`

### Quali parametri vengono letti dai provider
I parametri arrivano da proprietà Maltego:
`ICT.AI.Temperature`, `ICT.AI.Top`, `ICT.AI.MaxToken`, `ICT.AI.Frequency`, `ICT.AI.Presence_Penalty`.

Il transform **tenta** sempre di usare i parametri completi quando possibile, ma **fa fallback** automatici se il provider non li supporta. In pratica:
- **openai**: legge tutti i parametri (temperature/top_p/max_tokens/frequency/presence).  
  In modalità Responses usa `max_output_tokens`.
- **lightningai**: trattato come OpenAI‑like → tenta tutti i parametri, con fallback.
- **vertex**: trattato come OpenAI‑like → tenta tutti i parametri, con fallback.
- **gemini**: **non usa** `frequency_penalty` e `presence_penalty` (rimossi).  
  Temperature/top_p/max_tokens OK (se supportati dal modello).
- **ollama**: **non usa** `frequency_penalty` e `presence_penalty` (rimossi).  
  Temperature/top_p/max_tokens: provati, poi fallback se il server non li accetta.
- **hf**: **solo** `model + messages`. Niente temperature/top_p/max_tokens/penalties.

> Nota: se un parametro non è supportato dal provider o dal modello, il transform riprova con un set più minimale (vedi fallback sotto).

### Range, significato e gestione errori dei parametri getAIV3
Nel codice (`transforms/getAIV3.py`) i valori vengono **convertiti** e **validati** prima di chiamare l'API.
Se un valore è fuori range o non è numerico, il transform **va in errore** con `ValueError` e **non** fa la chiamata.

**Range accettati (hard check):**
- `ICT.AI.Temperature`: **0.0 .. 1.0**  
  `0.0` = output più deterministico; `1.0` = più variabilità/creatività.
- `ICT.AI.Top` (top_p): **0.0 .. 1.0**  
  Più basso = sampling più restrittivo; più alto = più varietà.
- `ICT.AI.MaxToken`: **1 .. 100000**  
  Limite massimo di token generati (o `max_output_tokens` in Responses API).
- `ICT.AI.Frequency`: **0.0 .. 2.0**  
  Penalizza ripetizioni **frequenti** (riduce loop).
- `ICT.AI.Presence_Penalty`: **0.0 .. 2.0**  
  Penalizza la **riapparizione** di concetti già usati (spinge nuovi temi).

**Cosa succede con valori errati:**
- Se il valore **non è numerico** (es. stringa non convertibile), la conversione `float()`/`int()` fallisce e il transform termina con errore.
- Se il valore è **fuori range**, viene generato `ValueError` con messaggio esplicito (es. “Temperature should be between 0.0 and 1.0.”).
- Non c’è clamp automatico: correggi il valore a monte in Maltego.

**Note provider:**
- Anche se i parametri sono validi, alcuni provider/modelli **non li supportano**: il transform fa retry con un set più minimale (vedi sezione fallback).
- Per `hf`, anche con parametri validi, viene inviato **solo** `model + messages`.

### Doppio meccanismo di query OpenAI
Il transform può usare **due API diverse** quando `provider=openai`:

1) **Responses API** (moderna)  
Attiva solo se in `.env` hai `openAI-response=true`.
Usa:
```
model, input, instructions, temperature, top_p, max_output_tokens,
frequency_penalty, presence_penalty
```
Se `OPENAI_WEB_SEARCH=true`, aggiunge `tools=[{"type":"web_search"}]` e `tool_choice="auto"`.

**Fallback Responses (ordine tentativi):**
1. `full` (tutti i parametri)
2. `no_penalties` (rimuove frequency/presence)
3. `no_sampling` (rimuove temperature/top_p)
4. `defaults_only_max_output_tokens` (solo model/input/instructions + max_output_tokens)
5. `defaults_only` (solo model/input/instructions)
> Se `web_search` è attivo, i tools restano in tutti i tentativi.

2) **Chat Completions** (compatibile OpenAI‑like)  
Usata quando:
- `provider != openai`, **oppure**
- `openAI-response=false`.

**Fallback Chat Completions (ordine tentativi):**
Per **hf**:
1. `defaults_only` → solo `model + messages`

Per **altri provider**:
1. `full` (model, messages, temperature, top_p, max_tokens, penalties)
2. `full_max_completion_tokens` (sostituisce `max_tokens` con `max_completion_tokens`)
3. `no_penalties` (rimuove frequency/presence)
4. `no_penalties_max_completion_tokens` (come sopra + max_completion_tokens)
5. `defaults_only`
6. `defaults_only_max_tokens`
7. `defaults_only_max_completion_tokens`

### Riutilizzo parametri (2ª query / sentiment / NLI)
Quando una combinazione di parametri funziona, viene salvata e riutilizzata:
- per `ICT.2.ask`
- per Sentiment (`ICT.sentiment=Y`)
- per NLI (`ICT.NLI=Y`)

Questo evita nuovi retry e rende i risultati coerenti.

### Variabili `.env` usate da getAIV3
Solo queste variabili vengono lette dal transform:
- `OPENAI_API_KEY`: API key OpenAI (provider=openai)
- `HF_TOKEN`: API key Hugging Face (provider=hf)
- `LIGHTNINGAI_API_KEY`: API key LightningAI
- `GEMINI_API_KEY`: API key Gemini AI Studio
- `GOOGLE_APPLICATION_CREDENTIALS`: path al JSON Service Account (provider=vertex)
- `openAI-response`: `true|false` → abilita Responses API quando provider=openai
- `OPENAI_WEB_SEARCH`: `true|false` → abilita web_search **solo** con Responses API

Note importanti:
- **Ollama non richiede API key**: il client usa una chiave fittizia interna (`OLLAMA_DUMMY_API_KEY`), quindi nessuna variabile `.env` è necessaria.
- `ICT.AI.ApiKeyEnv` **non è** un nome di variabile `.env`: è il token vero e proprio passato dalla Entity (ha priorità).


## come usare un  model imaging 

su domanda(user)  Describe this image in one sentence: 
su text (system)   "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"

## configurazione  trasformate  ICT 
command line  :   /home/flavio/.conda/envs/maltego/bin/python
Command  Parameters :  project.py local getgooglesearch
Working Directoy :  /home/flavio/code/Osint/maltego

## Debug
python project.py local greetperson "phrase=valore da scrivere"

python project.py local dnstoip "DNS=italiancyberteam.it"
local dnstoip "italiancyberteam.it"

da mettere sul command parameters prima del comando:
-m debugpy --listen 5678 --wait-for-client

Esempio completo:
python -m debugpy --listen 5678 --wait-for-client project.py runserver

poi ti agganci con la  la versione launch.json 

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

python -c "import lxml.html.clean; from newspaper import Article; from maltego_trx.handler import handle_run; print('OK')"


## Future features
- Grounding con web search anche per provider `gemini` (con fallback sicuro se il tool non e supportato dall'endpoint/model).
