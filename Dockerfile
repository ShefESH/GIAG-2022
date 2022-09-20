FROM ubuntu:latest

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y python3 sqlite3 python3.8-venv openssh-client openssh-server sudo python3-pip cron firefox wget

COPY app/ /var/www/html
RUN chown -R www-data:www-data /var/www/html

WORKDIR /var/www/html

#install requirements as root
RUN python3 -m pip install -r requirements.txt

USER www-data

#setup flask
RUN python3 -c 'from application import db, create_app, models; db.create_all(app=create_app())'
RUN sqlite3 application/db.sqlite < application/seed.sql

#run flask
ENV FLASK_APP=application
EXPOSE 5000

RUN FLASK_APP=application
RUN flask run --host 0.0.0.0