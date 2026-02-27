#!/bin/bash

# Azure App Service startup script for Django

echo "Starting Cloud Certified Support Inc website..."

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Start gunicorn
gunicorn --bind=0.0.0.0 --timeout 600 cloudcertifiedsupport.wsgi
