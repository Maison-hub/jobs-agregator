FROM node:lts-alpine

WORKDIR /app

RUN apk update && apk upgrade
RUN apk add git
RUN apk add --no-cache bash

COPY ./app/package*.json ./


COPY ./app .

RUN npm install && npm cache clean --force

EXPOSE 3000

ENV PATH ./node_modules/.bin/:$PATH

CMD ["npm", "run", "dev"]