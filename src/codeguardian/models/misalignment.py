"""Data models for architecture misalignments."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Misalignment:
    """Represents an architecture misalignment."""

    rule_type: str
    severity: str  # "error", "warning"
    file_path: Path
    line_number: int
    message: str
    from_module: str
    to_module: str
    illegal_import: Optional[str] = None
    suggestion: Optional[str] = None

    def __str__(self) -> str:
        """String representation of the misalignment."""
        return (
            f"{self.severity.upper()}: {self.message}\n"
            f"  File: {self.file_path}:{self.line_number}\n"
            f"  From: {self.from_module} -> To: {self.to_module}"
        )
