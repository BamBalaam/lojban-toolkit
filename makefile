.PHONY: test
test:
	PYTHONPATH=. pytest -rA --tb=short --verbose
