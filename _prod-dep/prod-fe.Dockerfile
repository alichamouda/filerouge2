FROM nginx:1.21-alpine as FINAL
WORKDIR /usr/share/nginx/html
COPY ./frontend/ .
ENV VAPORMAP_BACKEND \
    VAPORMAP_BACKEND_PORT 

CMD apk add gettext && \
    envsubst '${VAPORMAP_BACKEND},${VAPORMAP_BACKEND_PORT}' < config.json.template > config.json && \
    nginx -g "daemon off;"