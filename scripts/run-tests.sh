#!/bin/bash

# Quick test script for CodeGuardian

set -e

echo "🛡️  Running CodeGuardian Tests"
echo "=============================="
echo ""

# Run unit tests
echo "Running unit tests..."
pytest -v

echo ""

# Run with coverage
echo "Running coverage analysis..."
pytest --cov=codeguardian --cov-report=term-missing

echo ""

# Run linters
echo "Running linters..."
flake8 src/ tests/ || true

echo ""
echo "=============================="
echo "✓ Test suite complete!"

