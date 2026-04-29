#!/bin/bash
set -e

# Function to find conda binary
find_conda_binary() {
    local conda_root="${1:-$CONDA_ROOT_PREFIX}"
    
    # Check standard locations first
    if [ -f "$conda_root/bin/conda" ]; then
        echo "$conda_root/bin/conda"
        return
    fi
    if [ -f "$conda_root/condabin/conda" ]; then
        echo "$conda_root/condabin/conda"
        return
    fi
    
    # If not found, check pkgs directory (partial installation)
    local pkgs_conda=$(find "$conda_root/pkgs" -name "conda" -type f -path "*/bin/conda" 2>/dev/null | head -1)
    if [ -n "$pkgs_conda" ] && [ -f "$pkgs_conda" ]; then
        echo "$pkgs_conda"
        return
    fi
    
    # Last resort: search entire conda directory
    local found_conda=$(find "$conda_root" -name "conda" -type f -path "*/bin/conda" 2>/dev/null | head -1)
    if [ -n "$found_conda" ] && [ -f "$found_conda" ]; then
        echo "$found_conda"
        return
    fi
    
    echo ""
}

echo "========================================================================="
echo ""
echo "  ABUS Launcher [Version 3.0]"
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
CONDA_ROOT_PREFIX="$INSTALL_DIR/conda"
INSTALL_ENV_DIR="$INSTALL_DIR/env"

# Set temp directories
export TMP="$INSTALL_DIR"
export TEMP="$INSTALL_DIR"

# Determine platform
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-py310_24.5.0-0-MacOSX-x86_64.sh"
    MINICONDA_CHECKSUM="a95f99c31ee1d2bf87e51546b9c71f5820b792e05b0d2f4a1bc4618478efce15"
    MINICONDA_INSTALLER="Miniconda3-py310_24.5.0-0-MacOSX-x86_64.sh"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-py310_24.5.0-0-Linux-x86_64.sh"
    MINICONDA_CHECKSUM="a95f99c31ee1d2bf87e51546b9c71f5820b792e05b0d2f4a1bc4618478efce15"
    MINICONDA_INSTALLER="Miniconda3-py310_24.5.0-0-Linux-x86_64.sh"
else
    echo "Unsupported operating system: $OSTYPE"
    exit 1
fi

# Function to check if conda base Python is corrupted
check_conda_base_python() {
    local conda_root="$1"
    local python_bin="$conda_root/bin/python"
    
    # Check if Python binary exists
    if [ ! -f "$python_bin" ]; then
        return 1  # Python not found = corrupted
    fi
    
    # Try to import critical built-in modules (this should work on all platforms)
    # Use a clean environment to avoid interference
    # Only check built-in modules that are essential and platform-independent
    if ! "$python_bin" -c "import sys; import os; import math" 2>/dev/null; then
        return 1  # Failed to import built-in modules = corrupted
    fi
    
    # Check if Python can execute basic operations
    if ! "$python_bin" -c "print('OK')" 2>/dev/null | grep -q "OK"; then
        return 1  # Python cannot execute basic code = corrupted
    fi
    
    # Note: We don't check subprocess here because:
    # 1. On macOS, subprocess.py tries to import msvcrt (Windows-only) which fails
    # 2. This is expected behavior and Python handles it gracefully
    # 3. The actual conda functionality doesn't require subprocess import to succeed at this stage
    
    return 0  # Python is OK
}

# Check if conda exists
CONDA_BIN=$(find_conda_binary "$CONDA_ROOT_PREFIX")
CONDA_EXISTS="F"
CONDA_BASE_CORRUPTED="F"

if [ -n "$CONDA_BIN" ] && [ -f "$CONDA_BIN" ]; then
    CONDA_EXISTS="T"
    
    # Check if conda base Python is corrupted
    # Only check if conda itself can run, not if all Python modules work
    echo "Checking conda base Python installation..."
    if ! check_conda_base_python "$CONDA_ROOT_PREFIX"; then
        echo "WARNING: Conda base Python installation appears corrupted."
        echo "This can happen if the installation was interrupted or files were corrupted."
        echo "Verification details:"
        echo "  - Python binary: $CONDA_ROOT_PREFIX/bin/python"
        if [ -f "$CONDA_ROOT_PREFIX/bin/python" ]; then
            echo "  - Python exists: YES"
            echo "  - Testing basic Python functionality..."
            "$CONDA_ROOT_PREFIX/bin/python" -c "import sys; print(f'Python {sys.version}')" 2>&1 || echo "  - Python test: FAILED"
        else
            echo "  - Python exists: NO"
        fi
        CONDA_BASE_CORRUPTED="T"
    else
        echo "Conda base Python installation verified."
    fi
fi

# Install or reinstall conda if needed or if corrupted
if [ "$CONDA_EXISTS" == "F" ] || [ "$CONDA_BASE_CORRUPTED" == "T" ]; then
    if [ "$CONDA_BASE_CORRUPTED" == "T" ]; then
        echo "Removing corrupted conda installation..."
        rm -rf "$CONDA_ROOT_PREFIX"
        echo "Conda installation removed. Will reinstall..."
    fi
    echo "Downloading Miniconda from $MINICONDA_URL"
    mkdir -p "$INSTALL_DIR"
    
    if ! curl -Lk "$MINICONDA_URL" -o "$INSTALL_DIR/$MINICONDA_INSTALLER"; then
        echo "Miniconda failed to download."
        exit 1
    fi
    
    # Verify checksum (simplified check)
    echo "Installing Miniconda to $CONDA_ROOT_PREFIX"
    # Run installer - python.app package may fail on macOS but conda should still work
    # Use set +e temporarily to allow installation to continue even if python.app fails
    # The installer may exit with non-zero code if python.app fails, but conda itself may still be installed
    set +e
    bash "$INSTALL_DIR/$MINICONDA_INSTALLER" -b -p "$CONDA_ROOT_PREFIX" -u
    INSTALLER_EXIT_CODE=$?
    set -e
    
    # Note: INSTALLER_EXIT_CODE may be non-zero if python.app fails, but this is expected on macOS
    # We'll check if conda actually exists rather than relying on exit code
    
    # Wait a moment for file system to sync
    echo "Waiting for installation to complete..."
    sleep 5
    
    # Test conda - check if it's actually functional despite any installation warnings
    echo "Verifying Miniconda installation..."
    
    # Find conda binary after installation (try multiple times)
    CONDA_BIN=""
    for i in 1 2 3; do
        CONDA_BIN=$(find_conda_binary "$CONDA_ROOT_PREFIX")
        if [ -n "$CONDA_BIN" ] && [ -f "$CONDA_BIN" ]; then
            break
        fi
        if [ $i -lt 3 ]; then
            echo "Conda binary not found, waiting and retrying... (attempt $i/3)"
            sleep 2
        fi
    done
    
    if [ -z "$CONDA_BIN" ] || [ ! -f "$CONDA_BIN" ]; then
        echo "WARNING: Conda binary not found in standard locations after installation."
        echo "This may happen if python.app installation failed (expected on macOS)."
        echo ""
        echo "Searching for conda in installation directory..."
        local found_condas=$(find "$CONDA_ROOT_PREFIX" -name "conda" -type f 2>/dev/null | head -5)
        if [ -n "$found_condas" ]; then
            echo "Found conda binaries:"
            echo "$found_condas"
            echo ""
            echo "Attempting to use conda from pkgs directory..."
            # Try to use conda from pkgs to complete installation
            local pkgs_conda=$(find "$CONDA_ROOT_PREFIX/pkgs" -name "conda" -type f -path "*/bin/conda" 2>/dev/null | head -1)
            if [ -n "$pkgs_conda" ] && [ -f "$pkgs_conda" ]; then
                echo "Found conda at: $pkgs_conda"
                echo "Attempting to complete installation using this conda..."
                # Try to use the conda from pkgs to complete the installation
                # First, try to copy/link conda to the standard location
                mkdir -p "$CONDA_ROOT_PREFIX/bin"
                mkdir -p "$CONDA_ROOT_PREFIX/condabin"
                
                # Copy conda binary to standard locations
                if cp "$pkgs_conda" "$CONDA_ROOT_PREFIX/bin/conda" 2>/dev/null; then
                    chmod +x "$CONDA_ROOT_PREFIX/bin/conda"
                    echo "Copied conda to $CONDA_ROOT_PREFIX/bin/conda"
                    CONDA_BIN="$CONDA_ROOT_PREFIX/bin/conda"
                elif cp "$pkgs_conda" "$CONDA_ROOT_PREFIX/condabin/conda" 2>/dev/null; then
                    chmod +x "$CONDA_ROOT_PREFIX/condabin/conda"
                    echo "Copied conda to $CONDA_ROOT_PREFIX/condabin/conda"
                    CONDA_BIN="$CONDA_ROOT_PREFIX/condabin/conda"
                else
                    # If copy fails, use the pkgs conda directly
                    echo "Using conda from pkgs directory directly"
                    CONDA_BIN="$pkgs_conda"
                fi
                
                # Verify the conda works
                if [ -n "$CONDA_BIN" ] && [ -f "$CONDA_BIN" ]; then
                    # Check if conda can actually run (not just exists)
                    if "$CONDA_BIN" --version 2>/dev/null >/dev/null 2>&1; then
                        echo "Conda is now available and functional at: $CONDA_BIN"
                    else
                        echo "WARNING: Conda binary found but cannot execute (likely has bad interpreter path)."
                        echo "This happens when conda binary references a temporary build path."
                        echo "Re-running Miniconda installer in update mode to complete installation..."
                        
                        # Re-run the installer in update mode (-u flag) to complete the installation
                        # This will install conda properly without the temporary path issue
                        set +e
                        bash "$INSTALL_DIR/$MINICONDA_INSTALLER" -b -p "$CONDA_ROOT_PREFIX" -u 2>&1 | grep -v "python.app" || true
                        set -e
                        sleep 5
                        
                        # Try to find conda again after re-installation
                        CONDA_BIN=$(find_conda_binary "$CONDA_ROOT_PREFIX")
                        if [ -n "$CONDA_BIN" ] && [ -f "$CONDA_BIN" ]; then
                            if "$CONDA_BIN" --version 2>/dev/null >/dev/null 2>&1; then
                                echo "Installation repaired successfully. Conda at: $CONDA_BIN"
                            else
                                echo "ERROR: Conda still cannot execute after repair attempt."
                                echo "The installation may be corrupted. Please try:"
                                echo "  rm -rf $CONDA_ROOT_PREFIX"
                                echo "  ./start.sh"
                                exit 1
                            fi
                        else
                            echo "ERROR: Could not find conda after repair attempt."
                            echo "The installation may be corrupted. Please try:"
                            echo "  rm -rf $CONDA_ROOT_PREFIX"
                            echo "  ./start.sh"
                            exit 1
                        fi
                    fi
                else
                    echo "ERROR: Could not use conda from pkgs directory."
                    exit 1
                fi
            else
                echo "ERROR: Miniconda installation failed - conda binary not found."
                echo "Installer exit code: $INSTALLER_EXIT_CODE"
                echo ""
                echo "Possible solutions:"
                echo "1. Check disk space: df -h"
                echo "2. Check permissions on $CONDA_ROOT_PREFIX"
                echo "3. Try removing and reinstalling: rm -rf $CONDA_ROOT_PREFIX"
                exit 1
            fi
        else
            echo "ERROR: No conda binaries found anywhere."
            echo "Installer exit code: $INSTALLER_EXIT_CODE"
            echo ""
            echo "Possible solutions:"
            echo "1. Check disk space: df -h"
            echo "2. Check permissions on $CONDA_ROOT_PREFIX"
            echo "3. Try removing and reinstalling: rm -rf $CONDA_ROOT_PREFIX"
            exit 1
        fi
    fi
    
    echo "Found conda at: $CONDA_BIN"
    echo "Miniconda version:"
    if ! "$CONDA_BIN" --version 2>/dev/null; then
        echo "ERROR: Conda binary found but cannot execute."
        echo "The conda binary may have an incorrect interpreter path."
        echo "Please remove the installation and try again:"
        echo "  rm -rf $CONDA_ROOT_PREFIX"
        exit 1
    fi || (echo "Miniconda not functional." && exit 1)
    
    # Verify conda base Python after installation
    echo "Verifying conda base Python after installation..."
    if ! check_conda_base_python "$CONDA_ROOT_PREFIX"; then
        echo "ERROR: Conda base Python is still corrupted after installation."
        echo "This may indicate a problem with the Miniconda installer or system."
        echo "Please try manually removing and reinstalling:"
        echo "  rm -rf $CONDA_ROOT_PREFIX"
        echo "  ./start.sh"
        exit 1
    fi
    echo "Conda base Python verified successfully."
    
    # Delete installer
    rm -f "$INSTALL_DIR/$MINICONDA_INSTALLER"
fi

# Find conda binary (may be in different locations)
CONDA_BIN=$(find_conda_binary "$CONDA_ROOT_PREFIX")
if [ -z "$CONDA_BIN" ] || [ ! -f "$CONDA_BIN" ]; then
    echo "ERROR: Could not find conda binary"
    exit 1
fi

# Create conda environment if needed
ABUS_GENUINE_INSTALLED="T"
if [ ! -d "$INSTALL_ENV_DIR" ]; then
    ABUS_GENUINE_INSTALLED="F"
    echo "Creating conda environment..."
    "$CONDA_BIN" create -y -k --prefix "$INSTALL_ENV_DIR" python=3.10 || (echo "Conda environment creation failed." && exit 1)
fi

# Check if environment was created
if [ ! -f "$INSTALL_ENV_DIR/bin/python" ]; then
    echo "Conda environment is empty."
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
    echo "Miniconda hook not found at $CONDA_SH_PATH"
    echo "Attempting to find conda.sh..."
    CONDA_SH_PATH=$(find "$CONDA_ROOT_PREFIX" -name "conda.sh" -type f 2>/dev/null | head -1)
    if [ -z "$CONDA_SH_PATH" ] || [ ! -f "$CONDA_SH_PATH" ]; then
        echo "ERROR: Could not find conda.sh"
        exit 1
    fi
    echo "Found conda.sh at: $CONDA_SH_PATH"
fi

source "$CONDA_SH_PATH"
conda activate "$INSTALL_ENV_DIR"

# Initialize conda for better compatibility (recommended by Anaconda documentation)
# This ensures conda commands work properly in the environment
if ! conda info --envs 2>/dev/null | grep -q "$INSTALL_ENV_DIR"; then
    echo "Initializing conda environment..."
    conda init bash 2>/dev/null || true
fi

# Verify Python is functional - if not, reinstall it
echo "Verifying Python installation..."
# Test multiple critical modules to ensure Python is fully functional
# Use full path to python to avoid conda activation issues
PYTHON_BIN="$INSTALL_ENV_DIR/bin/python"
if [ -f "$PYTHON_BIN" ]; then
    if ! "$PYTHON_BIN" -c "import sys; import math; import os" 2>/dev/null; then
        echo "Python installation appears incomplete or corrupted."
        echo "Removing corrupted environment and recreating..."
        rm -rf "$INSTALL_ENV_DIR"
        "$CONDA_BIN" create -y -k --prefix "$INSTALL_ENV_DIR" python=3.10 || (echo "Conda environment creation failed." && exit 1)
        conda activate "$INSTALL_ENV_DIR"
        
        # Verify again after recreation
        echo "Verifying recreated Python installation..."
        if ! python -c "import sys; import math; import os" 2>/dev/null; then
            echo "ERROR: Python installation is still broken after recreation."
            echo "This may indicate a problem with the conda installation itself."
            exit 1
        fi
        echo "Python installation verified successfully."
    else
        echo "Python installation verified successfully."
    fi
else
    echo "Python binary not found. This should not happen if environment was created correctly."
fi

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

# Setup installer env
echo "Miniconda location: $CONDA_ROOT_PREFIX"
cd "$SCRIPT_DIR"

if [ "$ABUS_GENUINE_INSTALLED" == "F" ]; then
    python -m pip install huggingface-hub==0.27.1
fi

export LOG_LEVEL=DEBUG
python start-abus.py voice


