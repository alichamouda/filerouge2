FROM python:3.8-alpine3.13
WORKDIR /app
ENV VAPORMAP_BACKEND \
    VAPORMAP_BACKEND_PORT
RUN apk add gettext
COPY ./frontend/ .
EXPOSE 8000
CMD envsubst '${VAPORMAP_BACKEND},${VAPORMAP_BACKEND_PORT}' < config.json.template > config.json && \
    python -m http.server
