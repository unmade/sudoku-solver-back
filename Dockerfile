FROM python:3.8-alpine

ENV HOME_DIR /usr/src/app
ENV PYTHONPATH="${HOME_DIR}/solvesudoku"

COPY ./requirements/requirements.txt ${HOME}/requirements/
COPY ./requirements/prod-requirements.txt ${HOME}/requirements/

RUN pip install -r requirements/requirements.txt

RUN apk add --no-cache --virtual .build-deps gcc libc-dev postgresql-dev \
    && apk add --no-cache postgresql-client \
    && pip install -r requirements/prod-requirements.txt \
    && apk del .build-deps gcc libc-dev postgresql-dev

WORKDIR ${HOME_DIR}

COPY . ${HOME_DIR}

RUN chmod +x ${HOME_DIR}/start.sh

EXPOSE 8000

CMD ["./start.sh"]
