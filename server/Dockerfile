FROM node:9.5 AS jsbuilder

COPY ./admin /admin
WORKDIR /admin

RUN npm install
RUN npm run build

COPY ./frontend/ /frontend
WORKDIR /frontend

RUN npm install
RUN npm run build

FROM nginx:1.13.9-alpine

COPY server/nginx.conf /etc/nginx/nginx.conf

COPY --from=jsbuilder /admin/dist/ app/admin/
COPY --from=jsbuilder /frontend/dist/ app/