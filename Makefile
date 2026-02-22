.DEFAULT_GOAL := help
.PHONY: help
LOCAL_DOCKER_IMAGE=houseofapis/currencyapi-python
CONTAINER_NAME=currencyapi-python
WORKING_DIR=/app
PORT=7004
# Use official image so test/run work without building
DOCKER_IMAGE ?= python:3.12-slim
DOCKER_RUN = docker run --rm -v ${PWD}:${WORKING_DIR} -w ${WORKING_DIR} --name ${CONTAINER_NAME} -p ${PORT}:${PORT}
DOCKER_RUN_IT = docker run --rm -v ${PWD}:${WORKING_DIR} -w ${WORKING_DIR} --name ${CONTAINER_NAME} -p ${PORT}:${PORT} -it

build-image: ## Build docker image
	docker build -t ${LOCAL_DOCKER_IMAGE} .

test: ## Run the tests (no build required)
	${DOCKER_RUN} ${DOCKER_IMAGE} sh -c "pip install -q -e . coverage && python -m coverage run -m unittest discover"

run: ## Run the run file (no build required)
	${DOCKER_RUN} ${DOCKER_IMAGE} sh -c "pip install -q -e . && python run.py"

test-coverage: ## Show test coverage (no build required)
	${DOCKER_RUN} ${DOCKER_IMAGE} sh -c "pip install -q -e . coverage && python -m coverage run -m unittest discover && python -m coverage report"

setup: ## Setup
	${DOCKER_RUN} ${DOCKER_IMAGE} pip install -e .

exec: ## Shell into container
	${DOCKER_RUN_IT} ${DOCKER_IMAGE} sh

build-package: ## Build pip package (sdist + wheel to dist/)
	${DOCKER_RUN} ${DOCKER_IMAGE} sh -c "pip install -q build && python -m build"

upload-package: ## Upload to PyPI (requires dist/ and ~/.pypirc credentials)
	${DOCKER_RUN} ${DOCKER_IMAGE} sh -c "pip install -q twine && twine upload dist/*" \
		-v ${HOME}/.pypirc:/root/.pypirc:ro

release: ## Build and upload to PyPI (use after version bump; requires ~/.pypirc)
	$(MAKE) build-package && $(MAKE) upload-package

help:
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
