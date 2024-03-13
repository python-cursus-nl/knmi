format:
    @echo "Running ruff, mypy"
    ruff check .
    ruff format .
    mypy .
