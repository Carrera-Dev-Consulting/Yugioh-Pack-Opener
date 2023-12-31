help:
	type makefile || cat ./makefile

format:
	black app scripts tests

lint:
	black --check app scripts tests
	mypy app

test:
	pytest tests

test-coverage:
	mkdir coverage || echo 'coverage exists'
	coverage run --data-file=coverage/.coverage -m pytest tests
	coverage lcov --data-file=coverage/.coverage -o coverage/lcov.info
	make render-coverage-html

render-coverage-html:
	coverage html --data-file=coverage/.coverage -d coverage/html
	python -m http.server --directory coverage/html -b 127.0.0.1

run-locally:
	python -m app

run-docker:
	docker build -f docker/Dockerfile -t backend
	docker run -n backend-server -p 8079:8080 -d backend

run:
	make run-locally

create-migration:
	alembic revision --autogenerate -m "$(MESSAGE)"

upgrade-db:
	alembic upgrade head


mysql-shell-local:
	docker exec -it docker_database_1 mysql -u root -p

drop-database:
	docker exec -it docker_database_1 mysql -u root -p -e "DROP DATABASE yugioh_db;"

create-database:
	docker exec -it docker_database_1 mysql -u root -p -e "CREATE DATABASE yugioh_db;"