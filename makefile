help:
	type .\makefile

start-services:
	docker-compose -f docker/docker-compose.yaml up -d

rebuild-and-start-services:
	docker-compose -f docker/docker-compose.yaml up --build -d

stop-services:
	docker-compose -f docker/docker-compose.yaml down