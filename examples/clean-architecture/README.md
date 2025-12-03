# Example: Clean Architecture Project
The `violations/` directory contains examples of code that would violate the architecture rules.

## Expected Violations

```
./run_check.sh
# Or use the provided script

codeguardian analyze --config codeguardian.yaml
# Run analysis

pip install codeguardian
# Install CodeGuardian
```bash

## Running the Check

3. **Dependency Flow**: Dependencies flow inward (presentation → infrastructure → application → domain)
2. **Application Isolation**: Application layer can only import from domain
1. **Domain Independence**: Domain layer cannot import from any other layer

## Key Rules

See `codeguardian.yaml` in this directory for the complete configuration.

## Configuration

```
└── codeguardian.yaml
├── tests/
│   └── presentation/    # Presentation layer (API, UI)
│   ├── infrastructure/  # Infrastructure layer (repositories, external services)
│   ├── application/     # Application layer (use cases)
│   ├── domain/          # Domain layer (entities, value objects)
├── src/
my-project/
```

## Project Structure

This example demonstrates how to configure CodeGuardian for a Clean Architecture project.


