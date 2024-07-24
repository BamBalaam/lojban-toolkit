.PHONY: tests
tests:
	PYTHONPATH=. pytest -rA --tb=short --verbose
