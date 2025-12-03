"""Configuration templates for different architectures."""
from typing import Dict
CLEAN_ARCHITECTURE_TEMPLATE = """version: "1.0"
project_name: "my-project"
architecture: "clean"
modules:
  - name: "domain"
    path: "src/domain"
    layer: "domain"
  - name: "application"
    path: "src/application"
    layer: "application"
  - name: "infrastructure"
    path: "src/infrastructure"
    layer: "infrastructure"
  - name: "presentation"
    path: "src/presentation"
    layer: "presentation"
rules:
  - type: "no_import"
    from: "domain"
    to: ["application", "infrastructure", "presentation"]
    message: "Domain layer must not depend on outer layers"
    severity: "error"
  - type: "no_import"
    from: "application"
    to: ["infrastructure", "presentation"]
    message: "Application layer must not depend on infrastructure or presentation"
    severity: "error"
exclude_paths:
  - "tests"
  - "venv"
  - ".venv"
"""
DDD_TEMPLATE = """version: "1.0"
project_name: "my-project"
architecture: "ddd"
modules:
  - name: "users"
    path: "src/users"
    layer: "bounded_context"
  - name: "orders"
    path: "src/orders"
    layer: "bounded_context"
  - name: "shared_kernel"
    path: "src/shared"
    layer: "shared"
rules:
  - type: "no_import"
    from: "users"
    to: ["orders"]
    message: "Bounded contexts should communicate through events"
    severity: "error"
exclude_paths:
  - "tests"
  - "venv"
"""
MVC_TEMPLATE = """version: "1.0"
project_name: "my-project"
architecture: "mvc"
modules:
  - name: "models"
    path: "src/models"
    layer: "model"
  - name: "views"
    path: "src/views"
    layer: "view"
  - name: "controllers"
    path: "src/controllers"
    layer: "controller"
rules:
  - type: "no_import"
    from: "models"
    to: ["views", "controllers"]
    message: "Models must not depend on views or controllers"
    severity: "error"
exclude_paths:
  - "tests"
  - "venv"
"""
HEXAGONAL_TEMPLATE = """version: "1.0"
project_name: "my-project"
architecture: "hexagonal"
modules:
  - name: "domain"
    path: "src/domain"
    layer: "core"
  - name: "ports"
    path: "src/ports"
    layer: "ports"
  - name: "adapters"
    path: "src/adapters"
    layer: "adapters"
rules:
  - type: "no_import"
    from: "domain"
    to: ["adapters"]
    message: "Domain core must not depend on adapters"
    severity: "error"
exclude_paths:
  - "tests"
  - "venv"
"""
LAYERED_TEMPLATE = """version: "1.0"
project_name: "my-project"
architecture: "layered"
modules:
  - name: "presentation"
    path: "src/presentation"
    layer: "presentation"
  - name: "business"
    path: "src/business"
    layer: "business"
  - name: "persistence"
    path: "src/persistence"
    layer: "persistence"
rules:
  - type: "no_import"
    from: "persistence"
    to: ["business", "presentation"]
    message: "Persistence layer cannot depend on upper layers"
    severity: "error"
exclude_paths:
  - "tests"
  - "venv"
"""
TEMPLATES: Dict[str, str] = {
    "clean": CLEAN_ARCHITECTURE_TEMPLATE,
    "ddd": DDD_TEMPLATE,
    "mvc": MVC_TEMPLATE,
    "hexagonal": HEXAGONAL_TEMPLATE,
    "layered": LAYERED_TEMPLATE,
}
def get_template(architecture: str) -> str:
    """Get configuration template for a specific architecture.
    Args:
        architecture: Name of the architecture
    Returns:
        YAML template string
    Raises:
        ValueError: If architecture is not supported
    """
    if architecture not in TEMPLATES:
        raise ValueError(
            f"Unknown architecture: {architecture}. "
            f"Supported: {', '.join(TEMPLATES.keys())}"
        )
    return TEMPLATES[architecture]
