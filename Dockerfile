FROM alpine
MAINTAINER ymlai.89@gmail.com
EXPOSE 8080
RUN apk update
RUN apk add python2
COPY main.py /tmp/main.py
COPY start.sh /tmp/start.sh
USER 1000
CMD ["sh","/tmp/start.sh"]