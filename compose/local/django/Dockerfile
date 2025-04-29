FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && pip install --upgrade pip

COPY requirements/base.txt .
COPY requirements/local.txt .
RUN pip install -r base.txt -r local.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
