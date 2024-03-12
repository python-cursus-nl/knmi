format:
    @echo "Running ruff, mypy"
    ruff .
    ruff format .
    mypy .
