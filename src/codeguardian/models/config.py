"""Data models for CodeGuardian configuration."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Module:
    """Represents a module in the codebase."""

    name: str
    path: str
    layer: Optional[str] = None
    allowed_dependencies: List[str] = field(default_factory=list)


@dataclass
class Rule:
    """Represents an architecture rule."""

    type: str  # "no_import", "layer_dependency", "module_dependency", etc.
    from_module: Optional[str] = None
    to_modules: List[str] = field(default_factory=list)
    message: Optional[str] = None
    severity: str = "error"  # "error", "warning"

    # For layer-based rules
    from_layer: Optional[str] = None
    to_layers: List[str] = field(default_factory=list)


@dataclass
class Config:
    """Main configuration for CodeGuardian."""

    version: str
    project_name: str
    architecture: str  # "clean", "ddd", "mvc", "hexagonal", "layered"
    modules: List[Module]
    rules: List[Rule]
    exclude_paths: List[str] = field(default_factory=lambda: ["tests", "venv", ".venv"])
    python_version: str = "3.8"

