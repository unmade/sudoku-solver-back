FROM python:3.8-alpine

ENV HOME_DIR /usr/src/app

ENV PYTHONPATH="${HOME_DIR}/solvesudoku"

COPY requirements/requirements.txt ${HOME}/requirements/
COPY requirements/prod-requirements.txt ${HOME}/requirements/
RUN pip install -r requirements/requirements.txt -r requirements/prod-requirements.txt

ARG django_allowed_hosts
ENV DJANGO_ALLOWED_HOSTS $django_allowed_hosts

ARG django_cors_origin_whitelist
ENV DJANGO_CORS_ORIGIN_WHITELIST $django_cors_origin_whitelist

ARG django_secret_key
ENV DJANGO_SECRET_KEY $django_secret_key

ENV DJANGO_SETTINGS_MODULE=solvesudoku.settings

WORKDIR ${HOME_DIR}

COPY . ${HOME_DIR}

EXPOSE 8000

CMD ["gunicorn", "--access-logfile=-", "--error-logfile=-", "--workers=2", "--bind=0.0.0.0:8000", "solvesudoku.wsgi:application"]
