#!/bin/bash
python manage.py migrate
python manage.py loaddata apps/user/fixtures/user_fixture.json
python manage.py runserver
