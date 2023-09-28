.DEFAULT_GOAL := help
.PHONY: help
LOCAL_DOCKER_IMAGE=houseofapis/currencyapi-python
CONTAINER_NAME=currencyapi-python
WORKING_DIR=/app
PORT=7004
DOCKER_COMMAND=docker run --rm -v ${PWD}:${WORKING_DIR} -w ${WORKING_DIR} --name ${CONTAINER_NAME} -p ${PORT}:${PORT} -it ${LOCAL_DOCKER_IMAGE}

build-image: ## Build docker image
	docker build -t ${LOCAL_DOCKER_IMAGE} .

test: ## Run the tests
	${DOCKER_COMMAND} python -m coverage run -m unittest discover

run: ## Run the sample testing file
	${DOCKER_COMMAND} python run.py

test-coverage: ## Show test coverage
	${DOCKER_COMMAND} python -m coverage report

setup: ## Setup
	${DOCKER_COMMAND} python setup.py install

exec: ## Run test file
	${DOCKER_COMMAND} sh

build-package: ## Build pip package
	${DOCKER_COMMAND} python setup.py sdist bdist_wheel

upload-package: ## Upload pip package
	${DOCKER_COMMAND} python -m twine upload dist/*

help:
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
