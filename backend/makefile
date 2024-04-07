help:
	type makefile || cat ./makefile

format:
	black app scripts tests

lint:
	black --check app scripts tests
	mypy app scripts --disable-error-code=method-assign

test:
	pytest --cov=app --cov=scripts --cov-report html --cov-report term --cov-report lcov:lcov.info tests

start-cov-server:
	make test
	python -m http.server --directory htmlcov -b 127.0.0.1

run-locally:
	python -m app

run-docker:
	docker build -f docker/Dockerfile -t backend
	docker run -n backend-server -p 8079:8080 -d backend

serve-docs:
	pdoc app

run:
	make run-locally

create-migration:
	alembic revision --autogenerate -m "$(MESSAGE)"

upgrade-db:
	alembic upgrade head

seed-database:
	python -m scripts.seed_database_with_yugioh_card -d "mysql+pymysql://root:password@localhost/yugioh_db"

mysql-shell-local:
	docker exec -it docker_database_1 mysql -u root -p

drop-database:
	docker exec -it docker_database_1 mysql -u root -p -e "DROP DATABASE yugioh_db;"

create-database:
	docker exec -it docker_database_1 mysql -u root -p -e "CREATE DATABASE yugioh_db;"
database-up:
	docker-compose -f docker/docker-compose.yaml up -d database

doc:
	pdoc app