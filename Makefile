.PHONY: help deps build test run

help:
\t@echo "Available targets: deps build test run"

deps:
\t@echo "Install dev deps (see README)"

build:
\t@echo "Build placeholders"

test:
\tpytest -q

run:
\t@echo "Run backend: uvicorn backend.app.main:app --reload --port 8000"
