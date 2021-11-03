FROM nginx:1.20.0-alpine
COPY ./gateway/nginx /etc/nginx

ENV FRONTEND_URL \
    FRONTEND_PORT \
    BACKEND_URL \
    BACKEND_PORT \
    SERVER_PORT=80 \
    SERVER_ADDRESS=localhost
RUN apk add gettext
ENTRYPOINT  envsubst '${BACKEND_URL},${BACKEND_PORT},${FRONTEND_URL},${FRONTEND_PORT},${SERVER_PORT},${SERVER_ADDRESS}' \
                 < /etc/nginx/api_gateway.template.conf \
                 > /etc/nginx/api_gateway.conf && \ 
            nginx -g 'daemon off;'
