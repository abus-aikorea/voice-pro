#!/bin/bash
set -e

echo "========================================================================="
echo ""
echo "  ABUS Launcher [Version 4.0 - uv]"
echo "  contact: abus.aikorea@gmail.com"
echo ""
echo "========================================================================="
echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check for special characters
if [[ "$SCRIPT_DIR" =~ [!@#\$%^\&*\(\)+,\;:=\<\>\?@\[\]\^\`\{\|\}~] ]]; then
    echo ""
    echo "*******************************************************************"
    echo "* WARNING: Special characters were detected in the installation path!"
    echo "*          This can cause the installation to fail!"
    echo "*******************************************************************"
    echo ""
fi

# Setup paths
INSTALL_DIR="$SCRIPT_DIR/installer_files"
INSTALL_ENV_DIR="$INSTALL_DIR/env"
UV_VERSION="0.11.28"
UV_DIR="$INSTALL_DIR/uv"
UV_EXE="$UV_DIR/uv"

if ! mkdir -p "$INSTALL_DIR"; then
    echo ""
    echo "Cannot create $INSTALL_DIR"
    echo "Check the parent folder permissions and try again."
    exit 1
fi

for CHECK_DIR in "$INSTALL_DIR" "$INSTALL_ENV_DIR"; do
    if [ -e "$CHECK_DIR" ] && [ ! -w "$CHECK_DIR" ]; then
        echo ""
        echo "$CHECK_DIR is not writable by the current user."
        echo "If a previous install was run with sudo, restore ownership with:"
        echo "  sudo chown -R \"$(id -un)\" \"$INSTALL_DIR\""
        exit 1
    fi
done

# Set temp directories
export TMP="$INSTALL_DIR"
export TEMP="$INSTALL_DIR"

# keep everything project-local (no global uv/python/cache pollution)
export UV_PYTHON_INSTALL_DIR="$INSTALL_DIR/python"
export UV_CACHE_DIR="$INSTALL_DIR/uv-cache"
export UV_PROJECT_ENVIRONMENT="$INSTALL_ENV_DIR"

# environment isolation
export PYTHONNOUSERSITE=1
unset PYTHONPATH
unset PYTHONHOME

# Determine the uv release artifact for this platform
ARCH="$(uname -m)"
if [[ "$OSTYPE" == "darwin"* ]]; then
    if [[ "$ARCH" == "arm64" ]]; then
        UV_TARGET="aarch64-apple-darwin"
    else
        UV_TARGET="x86_64-apple-darwin"
        echo "WARNING: PyTorch no longer ships wheels for Intel macOS; installation will likely fail."
    fi
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [[ "$ARCH" == "aarch64" ]]; then
        UV_TARGET="aarch64-unknown-linux-gnu"
    else
        UV_TARGET="x86_64-unknown-linux-gnu"
    fi
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

# (if necessary) download uv into a contained folder
if [ ! -f "$UV_EXE" ]; then
    echo "Downloading uv $UV_VERSION to $UV_DIR"
    mkdir -p "$UV_DIR"
    curl -Lk "https://github.com/astral-sh/uv/releases/download/$UV_VERSION/uv-$UV_TARGET.tar.gz" -o "$INSTALL_DIR/uv.tar.gz"
    tar -xzf "$INSTALL_DIR/uv.tar.gz" -C "$UV_DIR" --strip-components=1
    rm "$INSTALL_DIR/uv.tar.gz"
fi

# test the uv binary
echo "uv version:"
"$UV_EXE" --version

# figure out the GPU choice: GPU_CHOICE env var > saved choice > autodetect
SAVED_CHOICE_FILE="$INSTALL_DIR/gpu_choice.txt"
if [ -z "$GPU_CHOICE" ] && [ -f "$SAVED_CHOICE_FILE" ]; then
    GPU_CHOICE="$(cat "$SAVED_CHOICE_FILE")"
fi
if [ -z "$GPU_CHOICE" ]; then
    if [[ "$OSTYPE" != "darwin"* ]] && command -v nvidia-smi >/dev/null 2>&1; then
        GPU_CHOICE="G"
    else
        GPU_CHOICE="C"
    fi
fi
GPU_CHOICE="$(echo "$GPU_CHOICE" | tr '[:lower:]' '[:upper:]')"
echo "$GPU_CHOICE" > "$SAVED_CHOICE_FILE"

if [ "$GPU_CHOICE" == "G" ]; then
    SYNC_EXTRA="gpu"
    echo "GPU mode: NVIDIA (CUDA 12.8)"
else
    SYNC_EXTRA="cpu"
    echo "GPU mode: CPU"
fi
echo "To change this, delete \"$SAVED_CHOICE_FILE\" or set the GPU_CHOICE environment variable (G=NVIDIA, C=CPU)."

# install/update the environment from the committed lockfile (installs Python automatically)
"$UV_EXE" sync --frozen --extra "$SYNC_EXTRA"

# check if the environment was actually created
if [ ! -f "$INSTALL_ENV_DIR/bin/python" ]; then
    echo ""
    echo "Python environment is empty."
    exit 1
fi

export LOG_LEVEL=DEBUG
"$INSTALL_ENV_DIR/bin/python" start-abus.py voice
