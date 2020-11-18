## Introduction

This is simple restful api project build with flask. This is open source, you can fork, clone, share and edit. If you have any question, feel free to ask me.

</br>

### Getting Started

---

#### Clone the repo

```
$ git clone https://github.com/nukumalik/flask-restful.git
$ cd flask-restful
```

#### Install virtualenv if you don't installed yet,

```
$ sudo apt install python3-virtualenv
```

#### Create new env

```
$ python3 -m virtualenv venv
```

#### Activate your env

```
$ source venv/bin/activate
```

#### Install requirement packages

```
$ pip install -r requirements.txt
```

#### Init Flask Env

```
$ export FLASK_APP=run.py
```

#### Migration

```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

#### Running app

```
$ flask run
```

or

```
$ python run.py
```

</br>

## Packages

- flask
- flask-sqlalchemy
- flask-marshmallow
- flask-restful
- flask-migrate
- flask-jwt
