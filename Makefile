# Makefile for FinMLOps project

PYTHON=python
MAIN=main.py

.PHONY: run clean lint test

run:
	$(PYTHON) $(MAIN)

lint:
	flake8 src --max-line-length=100

test:
	pytest -v

clean:
	rm -rf __pycache__ .pytest_cache
	find . -type f -name "*.pyc" -delete
