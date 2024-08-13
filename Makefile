# Default target
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "	help		->	Display this help message"
	@echo "	info		->	Display project information"
	@echo "	current-version	->	Display current version"
	@echo "	bump-version	->	Bump version to a new version"
	@echo "	install		->	Install all dependencies for the project"
	@echo "	test		->	Run all tests for the project (Code Quality, Unit Tests, Integration Tests)"
	@echo "	black		->	Run Black code formatter"
	@echo "	black-check	->	Run Black code formatter check mode only"
	@echo "	mypy		->	Run mypy static type checker"
	@echo "	pylint		->	Run Pylint linter"
	@echo "	unittest	->	Run unit tests"
	@echo "	coverage	->	Run test coverage"
	@echo "	integrationtest	->	Run integration tests"

.PHONY: info
info:
	@echo "##### Project Information #####"
	@echo "Project Name: DockCraft"
	@echo "Version: $(shell cat VERSION)"
	@echo " "
	@echo "Description"
	@echo "A Python tool for formatting Dockerfiles with best practices, "
	@echo "ensuring clean, efficient, and maintainable container configurations. "
	@echo " "
	@echo "Author: Stefan Lacher"
	@echo "Email: contact@stefanlacher.com"

.PHONY: current-version
current-version:
	@cat VERSION

.PHONY: bump-version
bump-version:
	@read -p "Enter new version: " version; \
	if [ -z "$$version" ]; then \
		echo "Version cannot be empty. Aborting."; \
		exit 1; \
	fi; \
	echo "Bumping version to $$version"; \
	echo $$version > VERSION; \
	git add VERSION; \
	git commit -m "Bump version to $$version"; \
	git tag -a v$$version -m "Release version $$version"; \
	read -p "Do you want to push the new version and commit? (y/n) " answer; \
	if [ "$$answer" = "y" ] || [ "$$answer" = "Y" ]; then \
		git push origin HEAD; \
		git push origin --tags; \
	else \
		echo "Version bump and commit were not pushed to remote"; \
	fi



.PHONY: install
install:
	pip install -r src/requirements.txt
	pip install -r src/testing_requirements.txt

.PHONY: test
test: black-check mypy pylint coverage integrationtest rm_cache

.PHONY: black
black:
	@echo " "
	@echo " "
	@echo "##### Running Black code formatter #####"
	black --verbose src

.PHONY: black-check
black-check:
	@echo " "
	@echo " "
	@echo "##### Running Black code formatter check mode only #####"
	black --check src

.PHONY: mypy
mypy:
	@echo " "
	@echo " "
	@echo "##### Running mypy static type checker #####"
	mypy --cache-dir=/dev/null --config-file=infrastructure/testing_infrastructure/mypy.ini src
	$(MAKE) rm_cache

.PHONY: pylint
pylint:
	@echo " "
	@echo " "
	@echo "##### Running Pylint linter #####"
	pylint --rcfile=infrastructure/testing_infrastructure/.pylintrc -f colorized src

.PHONY: unittest
unittest:
	@echo " "
	@echo " "
	@echo "##### Running unit tests #####"
	pytest src/tests/unit
	$(MAKE) rm_cache

.PHONY: coverage
coverage:
	@echo " "
	@echo " "
	@echo "##### Running test coverage #####"
	coverage run --rcfile=src/.coveragerc -m pytest src/tests/unit
	$(MAKE) rm_cache
	coverage report -m
	rm -rf .coverage

.PHONY: integrationtest
integrationtest:
	@echo " "
	@echo " "
	@echo "##### Running integration tests #####"
	pytest src/tests/integration
	$(MAKE) rm_cache

.PHONY: rm_cache
rm_cache:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf src/__pycache__
	rm -rf src/DockCraft/__pycache__
	rm -rf src/tests/__pycache__
	rm -rf src/tests/unit/__pycache__
	rm -rf src/tests/integration/__pycache__
