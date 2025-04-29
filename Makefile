run:
	docker-compose up --build

shell:
	docker-compose exec django bash

migrate:
	docker-compose exec django python manage.py migrate

test:
	docker-compose exec django pytest
