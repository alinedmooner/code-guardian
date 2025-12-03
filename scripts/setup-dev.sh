#!/bin/bash

# Development setup script for CodeGuardian

set -e

echo "🛡️  CodeGuardian Development Setup"
echo "=================================="
echo ""

# Check Python version
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install package in development mode
echo ""
echo "Installing CodeGuardian in development mode..."
pip install -e ".[dev]"

# Run tests to verify installation
echo ""
echo "Running tests to verify installation..."
pytest -v

echo ""
echo "=================================="
echo "✓ Development setup complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "Useful commands:"
echo "  make test          - Run tests"
echo "  make coverage      - Run tests with coverage"
echo "  make format        - Format code"
echo "  make lint          - Run linters"
echo ""

