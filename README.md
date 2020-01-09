# DailySpokesMan

DailySpokesMan (DSM) is server side rendered web app that serves a local copy of Turkish newspaper [Sözcü](https://www.sozcu.com.tr/).

## Table of Contents

- [DailySpokesMan](#dailyspokesman)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [How to Install](#how-to-install)
    - [Usage](#usage)
  - [Built Using](#built-using)
  - [Authors](#authors)

## About

DailySpokesMan (DSM) is an web app that serves a modified local copy of Sözcü newspaper. DSM is a personal project for teaching myself full-stack development by building a Flask server that serves both a REST API, and frontend views.

## Features

- DSM automatically stores news articles from [Sözcü](https://www.sozcu.com.tr/) newspaper in SQL-Lite database.
- REST API for querying articles, and state of the database
- Serverside rendered pages

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### How to Install

Make sure you have installed Python 3.7.0 or higher with Pipenv package and Node.js with npm package manager. After cloning the repository cd into it run following commands.

- Create virtual environment using Pipenv.

```shell
$ pipenv shell # create virtual enviroment
```

- Install dependencies to the virtual environment.

```shell
$ pipenv install # install dependencies
```

- After installing the dependencies initialize the SQL-Lite database

```shell
$ export FLASK_APP=run.py
$ flask db init
$ flask db migrate -m "initialize database"
$ flask db upgrade
```

Now all the dependencies are installed, and database has been initialized complete.

- Install Redis server

```shell
$ .scripts/redis.sh
```

### Usage

- Run Celery worker

```shell
$ .scripts/celery.sh
```

- Run task scheduler provided by Celery

```shell
$ .scripts/scheduler.sh
```

- Run the web server

```shell
$ .scripts/run.sh
```

## Built Using

- [Pipenv](https://docs.pipenv.org/en/latest/) for handling Python dependencies.
- [Flask](http://flask.pocoo.org/), micro web development framework for Python.
- [SQL-Alchemy](https://www.sqlalchemy.org/) Python wrapper around SQL databases, this project uses SQL-Lite.
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/), used for web scrapping, gathering news from [Sözcü](https://www.sozcu.com.tr/) newspaper.
- [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) for migrations.
- [Celery](http://www.celeryproject.org/) for scheduling, and handling web scrapping tasks.

## Authors

- [@atahanyorganci](https://github.com/atahanyorganci) - Idea & Implementation
