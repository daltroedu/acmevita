#!/bin/bash

exec gunicorn --workers=4 --bind 0.0.0.0:5000 app.wsgi:application --reload --access-logfile - --error-logfile - --timeout 30 --keep-alive 5