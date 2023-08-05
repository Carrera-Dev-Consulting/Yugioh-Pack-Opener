FROM node:16-buster-slim as build
WORKDIR /app
COPY . .
RUN yarn install --frozen-lockfile
RUN yarn build 




FROM nginx:1.23.4-alpine-slim

COPY ./docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY  --from=build /app/build /usr/share/nginx/html

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;"]