.PHONY: tests
tests:
	PYTHONPATH=. pytest --tb=short --verbose
