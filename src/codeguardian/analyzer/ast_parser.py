"""AST parser."""
import ast
from pathlib import Path
from typing import List
class ImportInfo:
    def __init__(self, module: str, line: int, is_from: bool = False):
        self.module = module
        self.line = line
        self.is_from = is_from
class ASTParser:
    def __init__(self, root_path: Path):
        self.root_path = root_path
    def parse_file(self, file_path: Path) -> List[ImportInfo]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read(), filename=str(file_path))
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(ImportInfo(alias.name, node.lineno, False))
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.append(ImportInfo(node.module, node.lineno, True))
            return imports
        except:
            return []
    def get_python_files(self, path: Path, exclude_paths: List[str]) -> List[Path]:
        if path.is_file() and path.suffix == ".py":
            return [path]
        return [f for f in path.rglob("*.py") if not any(e in str(f) for e in exclude_paths)]
    def extract_module_name(self, file_path: Path) -> str:
        try:
            relative = file_path.relative_to(self.root_path)
            parts = list(relative.parts)
            if parts[-1].endswith(".py"):
                parts[-1] = parts[-1][:-3]
            if parts and parts[-1] == "__init__":
                parts = parts[:-1]
            return ".".join(parts) if parts else ""
        except ValueError:
            return str(file_path)
