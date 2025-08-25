.PHONY: help install install-dev test lint format build publish clean

help: ## Afficher cette aide
	@grep -E '^[a-zA-Z_-]+:.*?## .*$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $1, $2}'

install: ## Installer le package
	pip install -e .

install-dev: ## Installer en mode développement
	pip install -e ".[dev]"
	pip install -r requirements-dev.txt

test: ## Lancer les tests
	pytest tests/ -v --cov=create_fastapi --cov-report=term-missing

lint: ## Vérifier le code avec flake8
	flake8 create_fastapi tests
	mypy create_fastapi

format: ## Formater le code
	black create_fastapi tests
	isort create_fastapi tests

build: clean ## Construire le package
	python -m build

publish: build ## Publier sur PyPI
	twine upload dist/*

clean: ## Nettoyer les fichiers générés
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
