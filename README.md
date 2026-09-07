# config

A Python project for `config` with modern tooling.

## Features

- 🐍 Python 3.12+ support
- 🧹 Code quality tools (Ruff, ty, pre-commit)
- 🧪 Testing with pytest
- 📦 Modern Python packaging with uv

## Quick Start

### 1. Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Set up environment variables

```bash
cp .env.example .env
```

### 4. Install pre-commit hooks

```bash
uv run pre-commit install
```

## Development

### Running Tests

```bash
uv run pytest
```

### Linting and Formatting

```bash
uv run ruff check src/
uv run ruff format src/
```

### Type Checking

```bash
uv run ty check
```

### Pre-commit Hooks

Pre-commit hooks will automatically run on every commit to ensure code quality. To run manually:

```bash
uv run pre-commit run --all-files
```

## Project Structure

```
config/
├── src/config/        # Main package code
├── tests/             # Test files
├── pyproject.toml     # Project configuration
├── .pre-commit-config.yaml  # Pre-commit hooks
└── README.md          # This file
```

## License

See [LICENSE](LICENSE) file for details.
