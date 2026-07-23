# Docker

Voice-Pro can run in a CPU-only Docker container. GPU containers need extra CUDA
runtime work and are not covered by this first image.

## Build

```bash
docker build -t voice-pro:cpu .
```

## Run

```bash
mkdir -p workspace model

docker run --rm -it \
  -p 7870:7870 \
  -v "$PWD/workspace:/app/workspace" \
  -v "$PWD/model:/app/model" \
  voice-pro:cpu
```

Open `http://127.0.0.1:7870` after Gradio starts.

For Azure Translator or Azure TTS, add `--env-file .env` to the `docker run`
command after creating `.env` from `.env.example`.

## Notes

- The image uses the `cpu` optional dependency set from `uv.lock`.
- Mounting `model/` keeps downloaded models between container runs.
- Mounting `workspace/` keeps generated files on the host.
- Azure credentials are optional. Pass them with `--env-file .env` when needed.
