#!/bin/bash
set -e

echo "========================================================================="
echo ""
echo "  ABUS Updater [Version 3.0]"
echo "  contact: abus.aikorea@gmail.com"
echo ""
echo "========================================================================="
echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check for spaces in path
if [[ "$SCRIPT_DIR" =~ [[:space:]] ]]; then
    echo "This script relies on Miniconda which can not be silently installed under a path with spaces."
    exit 1
fi

# Setup paths
INSTALL_DIR="$SCRIPT_DIR/installer_files"
CONDA_ROOT_PREFIX="$INSTALL_DIR/conda"
INSTALL_ENV_DIR="$INSTALL_DIR/env"

# Set temp directories
export TMP="$INSTALL_DIR"
export TEMP="$INSTALL_DIR"

# Check if conda exists
if [ ! -f "$CONDA_ROOT_PREFIX/bin/conda" ]; then
    echo "Conda not found. Please run start-voice.sh first to set up the environment."
    exit 1
fi

# Environment isolation
export PYTHONNOUSERSITE=1
export PYTHONPATH=
export PYTHONHOME=
export CUDA_PATH="$INSTALL_ENV_DIR"
export CUDA_HOME="$CUDA_PATH"

# Activate conda environment
CONDA_SH_PATH="$CONDA_ROOT_PREFIX/etc/profile.d/conda.sh"
if [ ! -f "$CONDA_SH_PATH" ]; then
    echo "Miniconda hook not found."
    exit 1
fi

source "$CONDA_SH_PATH"
conda activate "$INSTALL_ENV_DIR"

# Auto-detect GPU if GPU_CHOICE is not already set
if [ -z "$GPU_CHOICE" ]; then
    if command -v nvidia-smi >/dev/null 2>&1; then
        export GPU_CHOICE="G"
        echo "NVIDIA GPU detected. Setting GPU_CHOICE=G"
    else
        export GPU_CHOICE="C"
        echo "No NVIDIA GPU detected. Setting GPU_CHOICE=C (CPU mode)"
    fi
fi

cd "$SCRIPT_DIR"

export LOG_LEVEL=DEBUG
python start-abus.py voice --update

echo "Pip update process completed."
echo ""


