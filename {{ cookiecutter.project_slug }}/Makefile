SHELL := /bin/bash
VENV_PATH ?= .venv## path for created venv
MANIFESTS_NAME ?= ## name used for generating all required cdk8s manifests
MANIFESTS_ARGS ?= ## optional additional args to pass to main.py when generating manifests

manifests: pip-install ## Synth manifests to stdout and dist/ dir
	$(VENV_PATH)/bin/python app/main.py $(MANIFESTS_ARGS) $(MANIFESTS_NAME)

test: pip-install-dev ## Run pytest
	$(VENV_PATH)/bin/pytest --disable-warnings -v -s tests/

pip-install-dev: pip-install ## Install dev/test dependencies
	$(VENV_PATH)/bin/python -m pip install -r requirements.txt -r dev-requirements.txt

pip-install: venv ## Install all dependencies in the local venv
	$(VENV_PATH)/bin/python -m pip install -r requirements.txt

venv: ## Create a virtual env in .venv
	python -m venv $(VENV_PATH)

.PHONY: help
help: ## Print Makefile help
	@echo "Makefile usage:"
	@echo "  [INPUT_VARS] make <target>"
	@echo
	@if grep -qE '^.+ \?= .+$$' Makefile; then \
		echo "#### Input Variables ####"; \
	fi
	@awk '$$1 ~ /^[A-Z]+/ && $$2 ~ /^\?=$$/ {gsub(/\?=./, "", $$0); gsub(/##/, "", $$2); $$2="(default: "$$2")"; printf "- %s \n", $$0}' Makefile
	@echo "#### Targets ####"
	@awk -F "##" '$$1 ~ /^[a-zA-Z-_]+:.*$$/ {gsub(":.*", "", $$1); printf "- %s:%s \n", $$1, $$2}' Makefile
