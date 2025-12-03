"""Configuration loader for CodeGuardian."""

from pathlib import Path
from typing import Any, Dict

import yaml

from codeguardian.models.config import Config, Module, Rule


def load_config(config_path: Path) -> Config:
    """Load and parse configuration from YAML file.

    Args:
        config_path: Path to the YAML configuration file

    Returns:
        Parsed Config object

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If config is invalid
    """
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r") as f:
        data = yaml.safe_load(f)

    if not data:
        raise ValueError("Configuration file is empty")

    return _parse_config(data)


def _parse_config(data: Dict[str, Any]) -> Config:
    """Parse configuration dictionary into Config object.

    Args:
        data: Dictionary from YAML file

    Returns:
        Config object

    Raises:
        ValueError: If required fields are missing or invalid
    """
    # Validate required fields
    required_fields = ["version", "project_name", "architecture", "modules", "rules"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    # Parse modules
    modules = []
    for mod_data in data["modules"]:
        module = Module(
            name=mod_data["name"],
            path=mod_data["path"],
            layer=mod_data.get("layer"),
            allowed_dependencies=mod_data.get("allowed_dependencies", []),
        )
        modules.append(module)

    # Parse rules
    rules = []
    for rule_data in data["rules"]:
        rule = Rule(
            type=rule_data["type"],
            from_module=rule_data.get("from"),
            to_modules=rule_data.get("to", []),
            message=rule_data.get("message"),
            severity=rule_data.get("severity", "error"),
            from_layer=rule_data.get("from_layer"),
            to_layers=rule_data.get("to_layers", []),
        )
        rules.append(rule)

    # Create config object
    config = Config(
        version=data["version"],
        project_name=data["project_name"],
        architecture=data["architecture"],
        modules=modules,
        rules=rules,
        exclude_paths=data.get("exclude_paths", ["tests", "venv", ".venv"]),
        python_version=data.get("python_version", "3.8"),
    )

    return config

