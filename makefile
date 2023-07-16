.PHONY: test
test:
	PYTHONPATH=. pytest -ra --tb=short
