FROM node:alpine as builder

WORKDIR '/app'

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

RUN yarn

COPY ./ ./
RUN yarn build
CMD ["yarn", "start"]