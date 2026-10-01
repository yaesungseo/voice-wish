# Voice Wish development plan

These items are planned work, not shipped capabilities.

## 1. Make individual requests reliable

- [ ] Replace arbitrary filenames with a validated reference-voice registry, or constrain resolved paths to the reference directory.
- [ ] Validate text length, empty input, and supported languages.
- [ ] Generate unique output IDs and filenames.
- [ ] Return stable error responses without internal exception details.
- [ ] Add API tests using a fake inference service, including invalid paths and failed generation.

Acceptance: invalid inputs are rejected before inference, and two requests cannot overwrite each other's output.

## 2. Define the inference lifecycle

- [ ] Separate model loading and inference from HTTP request handling.
- [ ] Choose an explicit concurrency limit based on measured CPU and memory behavior.
- [ ] Add queued jobs with status endpoints if request duration warrants them.
- [ ] Add an audio download endpoint and a bounded retention/cleanup policy.
- [ ] Separate liveness from model readiness.

Acceptance: failures are observable, output files remain associated with the correct request, and storage growth is bounded.

## 3. Complete the user workflow

- [ ] Build a minimal interface for reference selection, text entry, generation status, and playback.
- [ ] Add one end-to-end test for text submission through audio retrieval.
- [ ] Validate installation on a clean environment and record the exact Python/runtime versions.
- [ ] Document model provisioning and provide a demo with permitted reference audio.

Acceptance: another developer can reproduce generation and playback from the README.

## Evidence to collect

Measure model initialization time, generation latency by text length, and peak memory on a named machine. Keep cold-start and warm-run measurements separate. Publish results only after running a reproducible benchmark; no performance claims are established yet.
