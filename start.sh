#! /usr/bin/env sh
set -e

python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput
gunicorn solvesudoku.wsgi:application --config gunicorn_conf.py
