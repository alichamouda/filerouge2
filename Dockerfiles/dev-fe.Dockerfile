# ENVSUBST N'existe pas
FROM alpine:3.13.6 as INIT

WORKDIR /app
COPY ./frontend/config.json.template .
ARG VAPORMAP_BACKEND
ARG VAPORMAP_BACKEND_PORT
RUN apk add gettext
RUN envsubst '${VAPORMAP_BACKEND},${VAPORMAP_BACKEND_PORT}' < config.json.template > config.json

FROM python:3.8-alpine3.13 AS FINAL
WORKDIR /app
COPY ./frontend/ .
COPY --from=INIT /app/config.json .
CMD [ "python", "-m", "http.server" ]
