#!make

MANAGE = python3 manage.py
SOURCE = src
MAIN = src

PROJECT_DIR=$(shell pwd)
WSGI_PORT=8000

# ##########################################################################
# common commands

run:
	$(MANAGE) init_project
	$(MANAGE) runserver 127.0.0.1:$(WSGI_PORT)

bot:
	$(MANAGE) bot

startapp:
	mkdir $(SOURCE)/$(NAME)
	sleep 3
	django-admin startapp $(NAME) ./$(SOURCE)/$(NAME)

# ##########################################################################
# deploy commands

black:
	black $(SOURCE) --exclude 'urls.py'

isort:
	isort $(SOURCE) --recursive

flake8:
	flake8 $(SOURCE)

# ##########################################################################
# deploy commands

gunicorn-run:
	$(MANAGE) collectstatic --no-input
	$(MANAGE) migrate --no-input
	$(MANAGE) init_project
	gunicorn config.wsgi:application -b 0.0.0.0:8000 --reload --workers=2

# ##########################################################################
# management

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

shell: # only after 'make extensions-install'
	$(MANAGE) shell_plus --print-sql

empty_migration:
	$(MANAGE) makemigrations --empty base

# ##########################################################################
# Uncommon commands

super:
	$(MANAGE) createsuperuser

install:
	pip install --no-cache-dir -r requirements/local_req.txt
