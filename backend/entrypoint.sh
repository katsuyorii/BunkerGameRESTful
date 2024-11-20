#!/bin/bash

echo "Search for changes..."
python manage.py makemigrations
python manage.py migrate

echo "Starting Gunicorn server..."
gunicorn src.wsgi:application --bind 0.0.0.0:8000