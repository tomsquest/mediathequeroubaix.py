SHELL:=/usr/bin/env bash

.DEFAULT_GOAL := check

.PHONY: check
check:
	poetry run pre-commit run --all-files

.PHONY: format
format:
	poetry run black src

.PHONY: clean
clean:
	find . -not -path "./.venv/*" | grep -E "\(__pycache__|\.cache|\.mypy_cache|\.pytest_cache|\.coverage|\.pyc|\.pyo$)" | xargs rm -rf
