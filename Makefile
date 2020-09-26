.PHONY: help build

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help


build:
	docker-compose build

run:
	docker-compose up -d

run-stdout:
	docker-compose up

stop:
	docker-compose stop

down:
	docker-compose down

logs-web:
	docker-compose logs -f acmevita-web

logs-db:
	docker-compose logs -f acmevita-db

db-init:
	docker-compose exec acmevita-web flask db init

db-migrate:
	docker-compose exec acmevita-web flask db migrate

db-upgrade:
	docker-compose exec acmevita-web flask db upgrade

run-tests:
	docker-compose exec acmevita-web coverage run -m unittest discover app/tests

coverage-tests:
	docker-compose exec acmevita-web coverage report -m

coverage-html-tests:
	docker-compose exec acmevita-web coverage html