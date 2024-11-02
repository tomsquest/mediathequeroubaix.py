SHELL:=/usr/bin/env bash

.DEFAULT_GOAL := check

.PHONY: check
check:
	uv run pre-commit run --all-files

.PHONY: format
format:
	uv run ruff format

.PHONY: clean
clean:
	find . -not -path "./.venv/*" | grep -E "\(__pycache__|\.cache|\.mypy_cache|\.pytest_cache|\.coverage|\.pyc|\.pyo$)" | xargs rm -rf
