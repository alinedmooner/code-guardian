# CodeGuardian 🛡️
Made with ❤️ for clean architecture advocates

---

- 🐛 [Issues](https://github.com/code-guardian/code-guardian/issues)
- 💬 [Discussions](https://github.com/code-guardian/code-guardian/discussions)
- 📖 [Documentation](https://docs.codeguardian.dev) (coming soon)

## Support

- [ ] VS Code extension
- [ ] Architecture visualization
- [ ] Custom rule DSL
- [ ] Support for TypeScript/JavaScript
- [ ] Web configuration generator
- [x] GitHub Action integration
- [x] YAML configuration system
- [x] Core AST analyzer

## Roadmap

MIT License - see [LICENSE](LICENSE) file for details

## License

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## Development

- GitHub Actions (for PR integration)
- Python 3.8+

## Requirements

5. **Continuous Auditing** - Maintain architectural integrity over time
4. **Documentation** - YAML configuration serves as living architecture documentation
3. **Technical Debt Prevention** - Catch architectural violations before they're merged
2. **Onboarding** - Help new developers understand the project's architecture
1. **PR Validation** - Automatic architecture checks on every Pull Request

## Use Cases

- **Layered Architecture** - Traditional n-tier architecture validation
- **Hexagonal Architecture** - Enforce ports and adapters pattern
- **Model-View-Controller (MVC)** - Ensure proper separation of concerns
- **Domain-Driven Design (DDD)** - Separate bounded contexts and prevent cross-context contamination
- **Clean Architecture** - Enforce dependency rule: outer layers depend on inner layers

## Supported Architectures

```
codeguardian analyze --config codeguardian.yaml --path ./src
```bash

Run analysis locally:

```
pip install codeguardian
```bash

Install CodeGuardian:

## Local Usage

CodeGuardian will automatically analyze your code and post comments on violations!

### 3. Open a Pull Request

```
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        env:
          fail-on-violation: true
          config-path: codeguardian.yaml
        with:
        uses: code-guardian/action@v1
      - name: Run CodeGuardian
      
      - uses: actions/checkout@v3
    steps:
    runs-on: ubuntu-latest
  architecture-check:
jobs:

    branches: [main, develop]
  pull_request:
on:

name: CodeGuardian Architecture Check
```yaml

Create `.github/workflows/codeguardian.yml`:

### 2. Add GitHub Action Workflow

```
    message: "Domain layer must not depend on outer layers"
    to: ["application", "infrastructure"]
    from: "domain"
  - type: "no_import"
rules:

    layer: "infrastructure"
    path: "src/infrastructure"
  - name: "infrastructure"
    layer: "application"
    path: "src/application"
  - name: "application"
    layer: "domain"
    path: "src/domain"
  - name: "domain"
modules:

architecture: "clean"
project_name: "my-project"
version: "1.0"
```yaml

Or create manually:

Visit [codeguardian.dev](https://codeguardian.dev) (coming soon) to generate your `codeguardian.yaml` file by selecting your architecture pattern.

### 1. Generate Configuration

## Quick Start

🚀 **Zero Infrastructure** - No servers needed, runs entirely within GitHub Actions  
⚙️ **Simple Configuration** - YAML-based configuration generated from a web interface  
📝 **Clear Reporting** - Detailed violation reports with actionable feedback  
🔍 **AST-Based Analysis** - Deep code analysis using Python's Abstract Syntax Tree  
🏗️ **Architecture Patterns** - Built-in support for Clean Architecture, DDD, MVC, Hexagonal, and Layered architectures  
✨ **Automated PR Analysis** - Runs automatically on every Pull Request via GitHub Actions  

## Features

CodeGuardian is an automated architecture validation tool that runs on every Pull Request to detect architectural violations in Python projects. It helps teams maintain clean architecture, prevent forbidden dependencies, and enforce architectural patterns like Clean Architecture, DDD, MVC, and more.

> Automated architecture analyzer for Python projects - Keep your codebase clean and enforce architectural boundaries


