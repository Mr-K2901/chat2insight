# Chat2Insight

Chat2Insight turns WhatsApp conversations and exported chat history into searchable summaries, topics, and action items.

## Stack

- Python 3.11+ for ingestion, processing, AI, storage, and the API
- Node.js 20+ for the WhatsApp integration
- FastAPI for the HTTP API
- Ollama, Whisper, and local vision tools as optional AI backends

## Quick start

1. Copy `.env.example` to `.env` and adjust the values.
2. Install Python dependencies:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Install the WhatsApp adapter dependencies:

   ```powershell
   npm install
   ```

4. Start the API:

   ```powershell
   uvicorn apps.api.main:app --reload
   ```

The API is available at `http://localhost:8000`; interactive docs are at `/docs`.

## Project layout

- `apps/`: application entry points and integrations
- `core/`: ingestion, media processing, AI, context, and pipeline logic
- `storage/`: database models and repositories
- `config/`: runtime configuration and prompt templates
- `scripts/`: operational and backfill commands
- `tests/`: unit and integration coverage
- `data/`: local runtime data, ignored by Git

## WhatsApp integration

The WhatsApp adapter is intentionally isolated behind `apps/whatsapp/message_listener.js`. Run it with `npm run whatsapp` after configuring authentication and the API URL. The first run may require scanning a QR code.

## Development

Run Python tests with:

```powershell
pytest
```

Run the Node syntax check with:

```powershell
npm run check
```
