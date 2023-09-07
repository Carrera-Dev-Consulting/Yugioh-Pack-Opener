FROM node:16-buster-slim

WORKDIR /app

COPY src src
COPY yarn.lock yarn.lock
COPY package.json package.json

RUN yarn install --frozen-lockfile

ENTRYPOINT [ "yarn", "test" ]