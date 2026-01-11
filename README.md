# Langchain models — Demo Workspace

This repository contains small demos and examples for using LangChain-style wrappers with streaming/service LLMs (Gemini/OpenAI) and Streamlit UI demos.

Folders
- `ChatBot/` — Streamlit chat UI (`chatBot.py`) and small CLI demos (`chatbot2.py`, examples). Interactive chat application with session-state history, Enter-to-send support, and a temperature slider.
- `Prompt/` — Streamlit prompt UI demos (e.g. `prompt_ui.py`) including a research-paper summarizer example.
- `Chat_Models/` — small model invocation examples (e.g. `chat_models_gemini.py`, `chatmodel_openai.py`).
- `Embedded_Models/` — embedding examples and document-similarity utilities.
- `LLMs/` — small LLM example scripts.
- `Structured_output/` — examples showing TypedDict / structured outputs and prompt templates.

## Quick Start

1. Create & activate a virtual environment (Windows PowerShell example):

```powershell
python -m venv venv
& .\venv\Scripts\Activate.ps1
```

2. Install required packages (basic set):

```powershell
pip install -U pip
pip install streamlit python-dotenv langchain-google-genai langchain-core
```

If you want to pin versions, generate a `requirements.txt` from your env.

3. Add your API key to a `.env` file at the repo root:

```
GOOGLE_API_KEY=your_api_key_here
```

Both Streamlit and CLI demos read `GOOGLE_API_KEY` using `python-dotenv`.

## Run the Streamlit Chat UI

From the repository root run:

```powershell
streamlit run .\ChatBot\chatBot.py
```

- Open `http://localhost:8501` in your browser.
- Use the sidebar to change temperature or clear chat history.
- Type a message and press Enter or click `Send`.

## Run CLI Chat Demo

```powershell
python .\ChatBot\chatbot2.py
```

- Type messages in the terminal; `exit` or `quit` to stop.

## Prompt UI (paper summarizer)

```powershell
streamlit run .\Prompt\prompt_ui.py
```

Pick paper/style/length and click `Summarize`.

## Common Errors & Troubleshooting

- `GOOGLE_API_KEY not found` — Ensure `.env` exists with `GOOGLE_API_KEY` and you restarted your shell/IDE after creating it.

- `pydantic` ValidationError on `ChatGoogleGenerativeAI`:
  - You must pass the `model` parameter and API key when constructing the client, e.g.:

    ```py
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
    ```

- `None of PyTorch, TensorFlow >= 2.0, or Flax have been found.` — informational: means local model execution is unavailable. Using cloud APIs is fine.

- Streamlit avatar or image errors: don't pass empty string to `avatar=`; use an emoji or omit the parameter.

- Long API response times:
  - Mostly due to cloud model inference and network latency. Typical response time is several seconds.
  - Use `timeout` parameter on model client to avoid indefinite blocking.
  - For very low-latency needs, consider a local model (requires GPU and additional setup).

## Git / Collaboration notes

- If `git push` is rejected because the remote has commits you don't have locally, fetch and rebase/merge (see below).

Safe sync steps:

```powershell
git fetch origin
git pull --rebase origin main   # rebase your changes onto remote
# resolve conflicts if any, then
git push origin main
```

If you need to overwrite remote (dangerous on shared branches):

```powershell
# Force-push (only if you know what you're doing)
git push --force-with-lease origin main
```

`--force-with-lease` is safer than `--force` because it prevents overwriting unexpected remote changes.

## File Map (high level)

- `ChatBot/chatBot.py` — main Streamlit chat UI
- `ChatBot/chatbot2.py` — CLI REPL demo
- `Prompt/prompt_ui.py` — Streamlit prompt-based UI (paper summarizer)
- `Chat_Models/*` — small quick scripts demonstrating model usage
- `Embedded_Models/*` — embedding + similarity scripts
- `Structured_output/*` — TypedDict / structured output examples

## Next steps & Suggestions

- Add a `requirements.txt` (I can generate one from your venv if you want).
- Add a `.gitignore` (exclude `venv/`, `.env`, and IDE files).
- Add a short `CONTRIBUTING.md` if you plan to collaborate.

---

If you want, I can: 
- create `requirements.txt` from your environment,
- add a `.gitignore`,
- or create a minimal `Dockerfile` for reproducible runs.

Tell me which of those you'd like next.
