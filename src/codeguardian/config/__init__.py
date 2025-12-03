"""Configuration package for CodeGuardian."""

from codeguardian.config.loader import load_config
from codeguardian.config.templates import get_template

__all__ = ["load_config", "get_template"]

