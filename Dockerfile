FROM ubuntu:latest

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y python3 sqlite3 python3.8-venv sudo python3-pip

COPY app/ /var/www/html
RUN chown -R www-data:www-data /var/www/html

WORKDIR /var/www/html

#install requirements as root
RUN python3 -m pip install -r requirements.txt

USER www-data

#setup flask
RUN sqlite3 db.sqlite < seed.sql

#run flask
ENV FLASK_APP=app.py
EXPOSE 5000

RUN flask run --host 0.0.0.0