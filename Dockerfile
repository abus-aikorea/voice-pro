FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONNOUSERSITE=1 \
    GPU_CHOICE=C \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_SERVER_PORT=7870 \
    UV_PROJECT_ENVIRONMENT=/app/installer_files/env \
    UV_CACHE_DIR=/app/installer_files/uv-cache \
    UV_PYTHON_INSTALL_DIR=/app/installer_files/python

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        curl \
        ffmpeg \
        git \
        pkg-config \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --extra cpu

COPY . .

EXPOSE 7870

CMD ["installer_files/env/bin/python", "start-voice.py"]
