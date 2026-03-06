#!/bin/bash

REPO_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
PYTHON_REQS="$REPO_DIR/requirements.txt"
VENV_DIR="$REPO_DIR/.venv"

sudo apt update

# Check if git-lfs is installed
if ! command -v git-lfs &> /dev/null; then
    echo "git-lfs is not installed. Installing..."
    sudo apt install -y git-lfs
    git lfs install
    echo "git-lfs installation complete."
else
    echo "git-lfs is already installed."
    git lfs version
fi

# Check if azure-cli is installed
if ! command -v az &> /dev/null; then
    echo "azure-cli is not installed. Installing the latest version..."
    
    # Install azure-cli
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    
    echo "azure-cli installation complete."
else
    echo "azure-cli is already installed."
    az --version
fi

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv is not installed. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    echo "uv installation complete."
else
    echo "uv is already installed."
    uv --version
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment at $VENV_DIR..."
    uv venv "$VENV_DIR"
    echo "Virtual environment created."
else
    echo "Virtual environment already exists at $VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Install Python dependencies
if [ -f "$PYTHON_REQS" ]; then
    echo "Installing Python dependencies from requirements.txt..."
    uv pip install --prerelease=allow -r "$PYTHON_REQS"
    echo "Python dependencies installation complete."
else
    echo "requirements.txt not found. Skipping Python dependencies installation."
fi