# Voice Wish

A text-to-speech backend prototype that generates speech from text and a local reference audio file using XTTS v2.

Backend implementation by **Yaesung Seo**.

## Current scope

Implemented:

- A FastAPI server with `POST /tts/generate`.
- Request fields for text, a reference-audio filename, and language (default: `ko`).
- Coqui TTS / XTTS v2 inference configured to run on CPU.
- Local WAV output and basic missing-file/error responses.

Not implemented yet: the web frontend, browser playback, background jobs, per-request output files, authentication, and a reproducibly validated deployment environment. The `frontend/` directory is a placeholder.

## Request flow

1. FastAPI validates the request shape.
2. The service resolves the reference audio beneath `backend/app/voices/`.
3. XTTS v2 generates speech on CPU.
4. The service writes `backend/app/outputs/cloned.wav`.
5. The API returns a message and the local output path.

The model is initialized when the service module is imported. The response is a local filesystem path, not a downloadable audio response. Every generation currently targets the same output file, so requests can overwrite previous results.

## Repository layout

```text
backend/app/
  main.py                 FastAPI application
  routes/tts.py           Request schema and API endpoint
  services/tts_service.py Model initialization and inference
  voices/                 Local reference audio (not committed)
  outputs/                Generated audio (not committed)
frontend/                 Placeholder
requirements.txt          Pinned dependency list
```

## Local setup

The following reflects the source layout; dependency compatibility and model initialization have not been revalidated in this documentation pass. First use may need to download model assets and follow the model's setup requirements.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd backend
uvicorn app.main:app --reload
```

Place a reference recording you are permitted to use at `backend/app/voices/reference.wav`, then call:

```sh
curl -X POST http://127.0.0.1:8000/tts/generate \
  -H 'Content-Type: application/json' \
  -d '{"text":"Hello, this is Voice Wish.","speaker_filename":"reference.wav","language":"en"}'
```

The expected response shape contains `message` and `output_path`. Audio is currently read from the generated local file.

## Known limitations

- Caller-supplied audio paths are not constrained to the intended directory.
- Output filenames are shared across requests.
- Inference is synchronous; there is no explicit queue or concurrency policy.
- Input length and supported-language restrictions are not explicitly enforced.
- Generic exceptions are returned as error text.
- There is no automated test suite or measured latency baseline in this repository.

See [ROADMAP.md](ROADMAP.md) for the next development milestones.
