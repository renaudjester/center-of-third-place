start-python-api:
	poetry run python src/app.py

start-mongodb:
	docker-compose up -d

stop-mongodb:
	docker-compose down

stop-mongodb-and-remove-data:
	docker-compose down -v && rm -rf data