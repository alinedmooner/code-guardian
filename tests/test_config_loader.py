"""Tests for the configuration loader."""

from pathlib import Path
from textwrap import dedent

import pytest

from codeguardian.config.loader import load_config


def test_load_valid_config(tmp_path):
    """Test loading a valid configuration file."""
    config_content = dedent("""
        version: "1.0"
        project_name: "test-project"
        architecture: "clean"
        
        modules:
          - name: "domain"
            path: "src/domain"
            layer: "domain"
          
          - name: "application"
            path: "src/application"
            layer: "application"
        
        rules:
          - type: "no_import"
            from: "domain"
            to: ["application"]
            message: "Domain cannot import application"
            severity: "error"
    """)

    config_file = tmp_path / "codeguardian.yaml"
    config_file.write_text(config_content)

    config = load_config(config_file)

    assert config.version == "1.0"
    assert config.project_name == "test-project"
    assert config.architecture == "clean"
    assert len(config.modules) == 2
    assert len(config.rules) == 1
    assert config.modules[0].name == "domain"
    assert config.rules[0].type == "no_import"


def test_load_missing_file():
    """Test loading a non-existent file."""
    with pytest.raises(FileNotFoundError):
        load_config(Path("nonexistent.yaml"))


def test_load_invalid_config(tmp_path):
    """Test loading an invalid configuration file."""
    config_content = dedent("""
        version: "1.0"
        # Missing required fields
    """)

    config_file = tmp_path / "invalid.yaml"
    config_file.write_text(config_content)

    with pytest.raises(ValueError):
        load_config(config_file)

