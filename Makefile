init: 
	django-admin startproject main

create-app:
	django-admin startapp "$(name)"

dev:
	docker-compose up -d

check-migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver