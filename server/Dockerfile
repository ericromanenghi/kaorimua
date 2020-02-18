FROM nginx:1.13.9-alpine

COPY server/nginx.conf /etc/nginx/nginx.conf
COPY server/.htpasswd /etc/nginx/.htpasswd
COPY ./dist/ app/