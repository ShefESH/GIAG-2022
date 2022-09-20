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

To be tested