#!/bin/bash
set -e

echo "========================================================================="
echo ""
echo "  ABUS Configure [Version 3.0]"
echo "  contact: abus.aikorea@gmail.com"
echo ""
echo "========================================================================="
echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if running as root (for package installation)
if [ "$EUID" -ne 0 ]; then
    echo "This script may need administrator privileges for some operations."
    echo "You may be prompted for your password."
    echo ""
fi

# Determine OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "macOS detected"
    
    # Check for Homebrew
    if ! command -v brew &> /dev/null; then
        echo "Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    # Install ffmpeg
    if ! command -v ffmpeg &> /dev/null; then
        echo "Installing ffmpeg..."
        brew install ffmpeg
    fi
    
    # Install git if needed
    if ! command -v git &> /dev/null; then
        echo "Installing git..."
        brew install git
    fi
    
    echo "macOS configuration complete."
    
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Linux detected"
    
    # Detect package manager
    if command -v apt-get &> /dev/null; then
        # Debian/Ubuntu
        echo "Detected apt package manager"
        sudo apt-get update
        sudo apt-get install -y git ffmpeg build-essential cmake
    elif command -v yum &> /dev/null; then
        # RHEL/CentOS
        echo "Detected yum package manager"
        sudo yum install -y git ffmpeg gcc gcc-c++ make
    elif command -v dnf &> /dev/null; then
        # Fedora
        echo "Detected dnf package manager"
        sudo dnf install -y git ffmpeg gcc gcc-c++ make
    elif command -v pacman &> /dev/null; then
        # Arch Linux
        echo "Detected pacman package manager"
        sudo pacman -S --noconfirm git ffmpeg base-devel
    else
        echo "Unsupported Linux distribution. Please install git and ffmpeg manually."
        exit 1
    fi
    
    # Check for NVIDIA GPU (Linux)
    if command -v nvidia-smi &> /dev/null; then
        echo "NVIDIA GPU detected. Please ensure CUDA toolkit is installed if needed."
        nvidia-smi
    fi
    
    echo "Linux configuration complete."
else
    echo "Unsupported operating system: $OSTYPE"
    exit 1
fi

echo ""
echo "ABUS configure.sh finished."
echo ""

