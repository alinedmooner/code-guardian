# Contributing to CodeGuardian

Thank you for your interest in contributing to CodeGuardian! This document provides guidelines and instructions for contributing.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/code-guardian/code-guardian.git
   cd code-guardian
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e ".[dev]"
   # Or
   pip install -r requirements-dev.txt
   ```

4. **Run tests**
   ```bash
   pytest
   ```

## Project Structure

```
code-guardian/
├── src/codeguardian/      # Main package
│   ├── analyzer/          # AST parsing and analysis
│   ├── config/            # Configuration loading and templates
│   ├── models/            # Data models
│   └── reporters/         # Output formatters
├── tests/                 # Test suite
├── examples/              # Example configurations
├── action.yml             # GitHub Action definition
└── docs/                  # Documentation (coming soon)
```

## Coding Standards

- Follow PEP 8 style guide
- Use type hints for function signatures
- Write docstrings for all public functions and classes
- Keep functions focused and single-purpose
- Maximum line length: 100 characters

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=codeguardian --cov-report=term-missing

# Run specific test file
pytest tests/test_analyzer.py
```

## Code Formatting

We use `black` for code formatting and `isort` for import sorting:

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Check with flake8
flake8 src/ tests/
```

## Adding New Features

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write tests first** (TDD approach)
   - Add tests in the `tests/` directory
   - Run tests to ensure they fail initially

3. **Implement the feature**
   - Write clean, documented code
   - Follow existing patterns in the codebase

4. **Ensure tests pass**
   ```bash
   pytest
   ```

5. **Update documentation**
   - Update README.md if needed
   - Add examples if applicable

6. **Submit a pull request**
   - Provide a clear description of changes
   - Reference any related issues

## Adding New Architecture Templates

To add a new architecture template:

1. Add the template in `src/codeguardian/config/templates.py`
2. Update the `TEMPLATES` dictionary
3. Add an example in `examples/`
4. Update the CLI to include the new option
5. Add tests

## Reporting Bugs

Please use the GitHub issue tracker to report bugs. Include:

- Python version
- CodeGuardian version
- Steps to reproduce
- Expected vs actual behavior
- Sample configuration (if applicable)

## Feature Requests

We welcome feature requests! Please:

- Check if a similar request already exists
- Provide a clear use case
- Describe the expected behavior

## Questions?

Open a discussion on GitHub or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

