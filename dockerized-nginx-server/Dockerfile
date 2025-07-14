FROM ubuntu:latest

RUN apt-get update && \
# apt-get upgrade -y && \
apt-get install nginx -y && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*
# COPY ./index.html /usr/share/nginx/html/index.html

EXPOSE 81
CMD [ "nginx", "-g", "daemon off;" ]
