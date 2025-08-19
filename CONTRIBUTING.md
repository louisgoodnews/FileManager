# Contributing to FileManager

We're excited that you're interested in contributing to FileManager! This document outlines the process for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)
- [Testing](#testing)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment (see below)
4. Create a new branch for your changes

## Development Setup

1. Ensure you have Python 3.7+ installed
2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FileManager.git
   cd FileManager
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
5. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## How to Contribute

1. **Bug Fixes**
   - Check the issue tracker for open bugs
   - Comment on the issue that you're working on it
   - Create a pull request with your fix

2. **New Features**
   - Open an issue first to discuss the feature
   - Once approved, implement the feature with tests
   - Submit a pull request

3. **Documentation**
   - Improve documentation, fix typos, or add examples
   - Update the README when necessary

## Pull Request Process

1. Ensure your code follows the project's code style
2. Update the documentation as needed
3. Add tests for your changes
4. Run the test suite and ensure all tests pass
5. Submit your pull request with a clear description of the changes

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints for all function signatures
- Keep lines under 88 characters (Black's default line length)
- Use `isort` for import sorting
- Use `black` for code formatting

## Testing

Run the test suite with:

```bash
pytest
```

We aim for 100% test coverage. Please add tests for any new code.

## Reporting Bugs

Please report bugs by [opening a new issue](https://github.com/yourusername/FileManager/issues/new) with:

- A clear title and description
- Steps to reproduce the issue
- Expected vs. actual behavior
- Python version and OS details
- Any relevant error messages

## Feature Requests

Feature requests are welcome! Please open an issue to discuss:

- The problem you're trying to solve
- Why this feature is important
- How it should work

## License

By contributing, you agree that your contributions will be licensed under the project's [LICENSE](LICENSE) file.
