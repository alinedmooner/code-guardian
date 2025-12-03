# CodeGuardian Documentation

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Configuration](#configuration)
4. [Architecture Patterns](#architecture-patterns)
5. [CLI Reference](#cli-reference)
6. [GitHub Action](#github-action)
7. [Rule Types](#rule-types)
8. [Advanced Usage](#advanced-usage)

## Installation

### From PyPI (when published)

```bash
pip install codeguardian
```

### From Source

```bash
git clone https://github.com/code-guardian/code-guardian.git
cd code-guardian
pip install -e .
```

## Quick Start

### 1. Initialize Configuration

Choose your architecture pattern:

```bash
codeguardian init clean    # Clean Architecture
codeguardian init ddd      # Domain-Driven Design
codeguardian init mvc      # Model-View-Controller
codeguardian init hexagonal # Hexagonal Architecture
codeguardian init layered   # Layered Architecture
```

This creates a `codeguardian.yaml` file in your current directory.

### 2. Customize Configuration

Edit `codeguardian.yaml` to match your project structure:

```yaml
version: "1.0"
project_name: "my-project"
architecture: "clean"

modules:
  - name: "domain"
    path: "src/domain"
    layer: "domain"

rules:
  - type: "no_import"
    from: "domain"
    to: ["application"]
    message: "Domain cannot import application"
```

### 3. Run Analysis

```bash
codeguardian analyze
```

## Configuration

### Configuration File Structure

```yaml
version: string            # Configuration version (currently "1.0")
project_name: string       # Your project name
architecture: string       # Architecture type (clean, ddd, mvc, hexagonal, layered)

modules:                   # List of modules in your project
  - name: string          # Module name
    path: string          # Path to module
    layer: string         # Optional layer name
    allowed_dependencies: # Optional list of allowed dependencies
      - string

rules:                     # Architecture rules
  - type: string          # Rule type (no_import, layer_dependency, etc.)
    from: string          # Source module
    to: [string]          # Target modules
    message: string       # Error message
    severity: string      # error or warning

exclude_paths:            # Paths to exclude from analysis
  - string

python_version: string    # Python version (default: "3.8")
```

## Architecture Patterns

### Clean Architecture

Enforces the Dependency Rule: dependencies point inward.

**Layers:**
- Domain (innermost)
- Application
- Infrastructure
- Presentation (outermost)

**Key Rules:**
- Domain cannot import from any other layer
- Application can only import from Domain
- Infrastructure can import from Application and Domain
- Presentation can import from all layers

### Domain-Driven Design (DDD)

Separates bounded contexts and enforces context independence.

**Structure:**
- Multiple bounded contexts (users, orders, payments, etc.)
- Shared kernel for common code

**Key Rules:**
- Bounded contexts should not directly depend on each other
- Communication through events or shared kernel

### Model-View-Controller (MVC)

Classic MVC pattern separation.

**Layers:**
- Models
- Views
- Controllers

**Key Rules:**
- Models cannot import from Views or Controllers
- Views should not import from Controllers

### Hexagonal Architecture

Ports and adapters pattern.

**Layers:**
- Domain (core)
- Ports (interfaces)
- Adapters (implementations)

**Key Rules:**
- Domain cannot depend on Adapters
- Ports should not depend on specific Adapters

### Layered Architecture

Traditional n-tier architecture.

**Layers:**
- Presentation
- Business
- Persistence
- Database

**Key Rules:**
- Each layer can only depend on layers below it

## CLI Reference

### `codeguardian analyze`

Analyze code for architecture violations.

```bash
codeguardian analyze [OPTIONS]
```

**Options:**
- `--config, -c PATH`: Path to configuration file (default: codeguardian.yaml)
- `--path, -p PATH`: Path to analyze (default: current directory)
- `--format, -f FORMAT`: Output format (console or json)
- `--output, -o PATH`: Output file for JSON format
- `--fail-on-violation/--no-fail`: Exit with error if violations found

**Examples:**

```bash
# Basic analysis
codeguardian analyze

# Analyze specific path
codeguardian analyze --path ./src

# JSON output
codeguardian analyze --format json --output report.json

# Don't fail on violations (useful for CI)
codeguardian analyze --no-fail
```

### `codeguardian init`

Initialize a new configuration file.

```bash
codeguardian init ARCHITECTURE [OPTIONS]
```

**Arguments:**
- `ARCHITECTURE`: clean, ddd, mvc, hexagonal, or layered

**Options:**
- `--output, -o PATH`: Output file path (default: codeguardian.yaml)

**Examples:**

```bash
# Initialize Clean Architecture
codeguardian init clean

# Custom output path
codeguardian init ddd --output config/architecture.yaml
```

### `codeguardian validate-config`

Validate configuration file.

```bash
codeguardian validate-config
```

## GitHub Action

### Setup

Create `.github/workflows/codeguardian.yml`:

```yaml
name: CodeGuardian Architecture Check

on:
  pull_request:
    branches: [main, develop]

jobs:
  architecture-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run CodeGuardian
        uses: code-guardian/action@v1
        with:
          config-path: codeguardian.yaml
          fail-on-violation: true
          comment-on-pr: true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Action Inputs

- `config-path`: Path to configuration file (default: codeguardian.yaml)
- `fail-on-violation`: Fail if violations found (default: true)
- `comment-on-pr`: Post comment on PR (default: true)
- `python-version`: Python version to use (default: 3.11)

### Action Outputs

- `violations-count`: Number of violations found
- `passed`: Whether the check passed (true/false)

## Rule Types

### `no_import`

Prevents imports from one module/layer to another.

```yaml
- type: "no_import"
  from: "domain"
  to: ["application", "infrastructure"]
  message: "Domain cannot import from outer layers"
  severity: "error"
```

### Layer-based Rules

Use `from_layer` and `to_layers` for layer-based restrictions:

```yaml
- type: "no_import"
  from_layer: "domain"
  to_layers: ["application", "infrastructure"]
  message: "Domain layer violation"
```

## Advanced Usage

### Custom Module Matching

For complex project structures, you can specify exact paths:

```yaml
modules:
  - name: "user_domain"
    path: "src/modules/users/domain"
    layer: "domain"
```

### Combining Warnings and Errors

Use different severities for different rules:

```yaml
rules:
  - type: "no_import"
    from: "domain"
    to: ["infrastructure"]
    severity: "error"  # Hard block
  
  - type: "no_import"
    from: "application"
    to: ["presentation"]
    severity: "warning"  # Just warn
```

### Multiple Configuration Files

Use different configs for different parts of your project:

```bash
codeguardian analyze --config backend/codeguardian.yaml --path backend/
codeguardian analyze --config frontend/codeguardian.yaml --path frontend/
```

## Best Practices

1. **Start Simple**: Begin with basic rules and add more as needed
2. **Document Your Architecture**: Use the YAML config as living documentation
3. **CI/CD Integration**: Run CodeGuardian on every PR
4. **Gradual Adoption**: Use warnings initially, then upgrade to errors
5. **Team Alignment**: Ensure the team understands and agrees on the architecture

## Troubleshooting

### "Configuration file not found"

Ensure `codeguardian.yaml` exists in your project root or specify the path:

```bash
codeguardian analyze --config path/to/config.yaml
```

### "Module not found"

Check that module paths in the configuration match your actual directory structure.

### "No violations detected but architecture seems wrong"

Review your rule configuration. The rules might not be specific enough or the module matching might need adjustment.

## Support

- GitHub Issues: [Report bugs](https://github.com/code-guardian/code-guardian/issues)
- Discussions: [Ask questions](https://github.com/code-guardian/code-guardian/discussions)
- Documentation: [Read more](https://docs.codeguardian.dev)

