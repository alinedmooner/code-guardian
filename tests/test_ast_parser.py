"""Tests for the AST parser."""

from pathlib import Path
from textwrap import dedent

import pytest

from codeguardian.analyzer.ast_parser import ASTParser


def test_parse_file_with_imports(tmp_path):
    """Test parsing a file with imports."""
    code = dedent("""
        import os
        import sys
        from pathlib import Path
        from typing import List, Dict
        
        def main():
            pass
    """)

    test_file = tmp_path / "test.py"
    test_file.write_text(code)

    parser = ASTParser(tmp_path)
    imports = parser.parse_file(test_file)

    assert len(imports) >= 2
    import_modules = [imp.module for imp in imports]
    assert "os" in import_modules
    assert "sys" in import_modules
    assert "pathlib" in import_modules


def test_get_python_files(tmp_path):
    """Test getting Python files from a directory."""
    # Create test structure
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "module1.py").write_text("# test")
    (tmp_path / "src" / "module2.py").write_text("# test")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_module.py").write_text("# test")

    parser = ASTParser(tmp_path)
    files = parser.get_python_files(tmp_path, ["tests"])

    assert len(files) == 2
    assert all(f.suffix == ".py" for f in files)
    assert not any("tests" in str(f) for f in files)


def test_extract_module_name(tmp_path):
    """Test extracting module name from file path."""
    parser = ASTParser(tmp_path)

    test_file = tmp_path / "src" / "domain" / "models.py"
    test_file.parent.mkdir(parents=True)
    test_file.write_text("# test")

    module_name = parser.extract_module_name(test_file)

    assert "domain" in module_name
    assert "models" in module_name

