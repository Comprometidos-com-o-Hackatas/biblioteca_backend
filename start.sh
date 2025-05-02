#!/bin/sh

echo "📦 Rodando makemigrations..."
pdm run python manage.py makemigrations

echo "📂 Rodando migrate..."
pdm run python manage.py migrate

echo "🚀 Iniciando Gunicorn..."
pdm run gunicorn django_project.wsgi:application --bind 0.0.0.0:8000