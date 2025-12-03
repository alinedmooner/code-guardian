.PHONY: help install install-dev test coverage lint format clean build publish
	codeguardian init mvc
init-mvc:  ## Initialize an MVC config in current directory

	codeguardian init ddd
init-ddd:  ## Initialize a DDD config in current directory

	codeguardian init clean
init-clean:  ## Initialize a clean architecture config in current directory

	cd examples/clean-architecture && codeguardian analyze
example-clean:  ## Run example on clean architecture

	python -m twine upload dist/*
publish:  ## Publish to PyPI

	python -m twine upload --repository testpypi dist/*
publish-test:  ## Publish to TestPyPI

	python -m build
build:  ## Build package

	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf *.egg-info
	rm -rf dist/
	rm -rf build/
clean:  ## Clean build artifacts

	isort --check-only src/ tests/
	black --check src/ tests/
format-check:  ## Check if code is formatted correctly

	isort src/ tests/
	black src/ tests/
format:  ## Format code with black and isort

	mypy src/
	flake8 src/ tests/
lint:  ## Run linters

	pytest --cov=codeguardian --cov-report=term-missing --cov-report=html
coverage:  ## Run tests with coverage report

	pytest -v
test:  ## Run tests

	pip install -e ".[dev]"
install-dev:  ## Install package with development dependencies

	pip install -e .
install:  ## Install package

	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "CodeGuardian - Development Commands"
help:  ## Show this help message


