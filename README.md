# GIAG-2022
Repository for 2022 Give it a Go Challenge

## Run App

### On Windows

`sqlite3` not tested on Windows.

Can run and test static aspect of site:

```
PS > cd .\app\
PS > $env:FLASK_APP = "app"
PS > $env:FLASK_DEBUG = "true"
PS > python -m flask run
```

### On Linux

```
$ python3 -m pip install app/requirements.txt
$ sudo apt install sqlite3
$
```

### Using Docker

```
$ sudo docker build -t giag .
$ sudo docker run -d -p 5000:5000 giag
```

### Using AWS

In conjunction with Docker

Transfer files:

```
scp -i [PATH_TO_PEM] -r [PATH_TO_GIAG-2022] ubuntu@[IP]:/home/ubuntu
```

Make sure to expose port 5000 in security group.

## Challenges

### Challenge 1: Robots

Go to `/robots.txt` and find the URL `/yournextchallenge`. Enter this into URL bar.