# AGENTS.md - Guidelines for Coding Agents

## Build/Lint/Test Commands
- **Ultra Kernel Build**: `cd Ultra && python build.py --toolchain gcc --arch x86_64`
- **Ultra Tests**: `cd Ultra && python build.py --unit-tests`
- **Ultra Single Test**: Run test binary directly: `Ultra/tests/bin/run_tests --filter <test_name>`
- **Sinai Server**: `python3 -m uvicorn sinai_server.app:app --reload --host 0.0.0.0 --port 8000`
- **Sinai CLI**: `./sinai_cli.py` (or `python3 sinai_cli.py`)
- **UI Build**: `cd ui/web && npm install && npm run build` (if scripts added)
- **Lint Python**: `ruff check .` (install ruff)
- **Lint JS**: `cd ui/web && npx eslint src/` (if configured)
- **Type Check**: `mypy sinai_server/ sinai_core/` (install mypy)

## Code Style Guidelines
- **Imports**: Absolute imports, group stdlib, third-party, local. Use `from sinai_server.core import ...`
- **Formatting**: Use Black for Python (line length 88). Consistent indentation.
- **Types**: Use type hints everywhere. Return types, parameter types.
- **Naming**: snake_case for functions/variables, CamelCase for classes, UPPER_CASE for constants.
- **Error Handling**: Use try-except, raise custom exceptions, log errors with logging module.
- **Async**: Use async/await for I/O operations in FastAPI.
- **Docstrings**: Use Google-style docstrings for functions/classes.
- **Security**: No secrets in code, validate inputs, use HTTPS.
- **Testing**: Write unit tests with pytest, mock external deps.
- **Commits**: Use imperative mood, e.g., "Add feature X".

No Cursor or Copilot rules found.</content>
<parameter name="filePath">AGENTS.md