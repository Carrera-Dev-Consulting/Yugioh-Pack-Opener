FROM nginx:alpine-slim


COPY cached/cards /www/data/images/cards
COPY cached/sets /www/data/images/sets
COPY ./docker/nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]