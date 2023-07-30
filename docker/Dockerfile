FROM nginx:1.23.4-alpine-slim

COPY ./docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./frontend/build /usr/share/nginx/html

EXPOSE 80
CMD [ "nginx", "-g", "dameon off;"]