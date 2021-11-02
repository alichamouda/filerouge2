FROM python:3.8-alpine3.13
WORKDIR /app
COPY ./app/ .
# RUN apk add libssl-dev
RUN pip install wheel && pip install -r requirements/production.txt

ENV  PYTHONDONTWRITEBYTECODE=1
ENV  PYTHONUNBUFFERED=1

ENV VAPOR_DBNAME=db_vapormap
ENV VAPOR_DBUSER=user_vapormap
ENV VAPOR_DBPASS=vapormap
ENV VAPOR_DBHOST=mysql
ENV DJANGO_SETTINGS_MODULE="vapormap.settings.production"

CMD ["gunicorn" ,"vapormap.wsgi:application", "--bind", "0.0.0.0:8001"]