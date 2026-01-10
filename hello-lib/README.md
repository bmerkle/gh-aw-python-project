# Hello Lib

A simple Python library example demonstrating best practices for Python project structure, testing, linting, and CI/CD.

## Features

- Simple `Greeter` class for generating greeting messages
- Convenience `greet()` function
- Full type hints with `py.typed` marker
- Comprehensive test suite with pytest
- Code quality with Ruff (linting + formatting)
- Type checking with mypy
- GitHub Actions CI/CD pipeline

## Installation

```bash
# Install with pip
pip install hello-lib

# Or install from source with uv
uv sync
```

## Usage

```python
from hello_lib import Greeter, greet

# Using the convenience function
message = greet("World")
print(message)  # Output: Hello, World!

# Using the Greeter class
greeter = Greeter("Alice")
print(greeter.greet())        # Output: Hello, Alice!
print(greeter.greet_formal()) # Output: Good day, Alice. It is a pleasure to meet you.
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/hello-lib.git
cd hello-lib

# Install dependencies (using uv)
uv sync --dev
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=hello_lib --cov-report=html
```

### Linting and Formatting

```bash
# Check for linting issues
uv run ruff check src tests

# Auto-fix linting issues
uv run ruff check --fix src tests

# Check formatting
uv run ruff format --check src tests

# Apply formatting
uv run ruff format src tests
```

### Type Checking

```bash
uv run mypy src
```

### Building

```bash
uv build
```

## Project Structure

```
hello-lib/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI pipeline
├── src/
│   └── hello_lib/
│       ├── __init__.py     # Package exports
│       ├── greeter.py      # Main module
│       └── py.typed        # PEP 561 marker
├── tests/
│   ├── __init__.py
│   └── test_greeter.py     # Test suite
├── pyproject.toml          # Project configuration
└── README.md
```

## License

MIT License
