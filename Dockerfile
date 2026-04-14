FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /auvk6-parlament

COPY . /auvk6-parlament/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD gunicorn core.wsgi:application --bind 0.0.0.0:8000