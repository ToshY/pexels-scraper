FROM python:3.10-slim-buster AS dev

LABEL maintainer="ToshY (github.com/ToshY)"

ENV PIP_ROOT_USER_ACTION ignore

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir --upgrade --force-reinstall 'setuptools>=65.5.1'

COPY . .

FROM dev AS prod

ENTRYPOINT ["python", "main.py"]
