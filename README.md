# FastAPI+MongoDB Boilerplate Code

## 1 About

`fastapi-mongodb-boilerplate` is a boilerplate code containing REST APIs developed using FastAPI and MongoDB as database.

## 2 Technical Specifications

### 2.1 Technologies

Below are the list of technologies used in this project:

1. [Python][1] - Programming language. Version >= 3.11.
1. [FastAPI][2] - Python Web framework.
1. [MongoDB][3] - NoSQL Database.
1. [Docker][4] - Containerizing the application.

### 2.2 Libraries

Libraries used in this project:

1. [PyMongo][6] - Native Python driver for MongoDB.
1. [Motor][7] - Asynchronous Python driver for MongoDB built on top of PyMongo.
1. [Prisma][8] - ORM (or ODM) for Python and MongoDB.

## 3 Setup

This project can be setup in two ways.

### 3.1 Local setup

Steps to setup `fastapi-mongodb-boilerplate` on your local machine.

#### STEP 1: Clone repository

Clone this repository and traverse to the project folder using below commands:

```sh
git clone https://github.com/DheemanthBhat/fastapi-mongodb-boilerplate.git
cd fastapi-mongodb-boilerplate
```

#### STEP 2: Setup virtual environment

Create and activate virtual environment.

##### Windows

```sh
python -m venv .venv
.venv\Scripts\activate
```

##### Linux

```sh
python -m venv .venv
source .venv/bin/activate
```

#### STEP 3: Install python packages

```sh
pip install -r requirements.txt
```

#### STEP 4: Setup Environment variables

1. Create duplicate of `.env.sample` file and rename it to `.env`.
1. Update environment variables with proper values based on your requirements.
1. For example change `MONGO_CONNECTION_STRING` to a valid MongoDB Atlas URL.

#### STEP 5: Start web server

```sh
uvicorn src.main:app --reload
```

### 3.2 Container setup

To setup `fastapi-mongodb-boilerplate` using Docker, open [Docker Desktop][5] and run below command.

```sh
docker-compose up -d
```

## 4 API docs

### 4.1 Swagger docs

Launch Swagger docs in browser: <http://127.0.0.1:8000/docs>

### 4.2 Redoc

Launch Redoc docs in browser: <http://127.0.0.1:8000/redoc>

[1]: https://www.python.org/
[2]: https://fastapi.tiangolo.com/
[3]: https://www.mongodb.com/
[4]: https://www.docker.com/
[5]: https://www.docker.com/products/docker-desktop/
[6]: https://pymongo.readthedocs.io/en/stable/
[7]: https://motor.readthedocs.io/en/stable/
[8]: https://www.prisma.io/docs/orm/overview/databases/mongodb
