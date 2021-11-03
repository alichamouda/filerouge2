FROM python:3.8-alpine3.13
WORKDIR /app
COPY ./app/ .
RUN pip install -r requirements/development.txt && python manage.py migrate
CMD ["python", "manage.py","runserver","0.0.0.0:8001"]