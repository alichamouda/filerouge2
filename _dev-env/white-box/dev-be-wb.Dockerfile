FROM python:3.8-alpine3.13
WORKDIR /app
EXPOSE 8001
CMD pip install -r requirements/development.txt && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8001