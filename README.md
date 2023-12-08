# ACMEVita

REST API developed with Python 3, Flask and Postgres. Application that exemplifies management system for a small company, with departments, employees and their dependents, conceptually coded in this way.

## Structure

Project based on the *factory* standard, architecture with *blueprints* and *Twelve Factor* practices.

Main files:

* ```/app/__init__.py```: instantiates configurations and blueprints;

* ```/app/config.py```: application settings, determined by type of environment;

* ```/app/blueprints/```: endpoints of business rules and others;

* ```/app/extensions/```: instantiates and configures third-party extensions;

* ```/app/tests/```: project testing.

**Overview:**

```
.
├── app
│   ├── blueprints
│   │   ├── business
│   │   │   ├── __init__.py
│   │   │   └── v1
│   │   │       ├── departament
│   │   │       │   ├── __init__.py
│   │   │       │   ├── models.py
│   │   │       │   ├── resources.py
│   │   │       │   ├── schemas.py
│   │   │       │   └── swagger.py
│   │   │       ├── dependent
│   │   │       │   ├── __init__.py
│   │   │       │   ├── models.py
│   │   │       │   ├── resources.py
│   │   │       │   └── schemas.py
│   │   │       ├── employee
│   │   │       │   ├── __init__.py
│   │   │       │   ├── models.py
│   │   │       │   ├── resources.py
│   │   │       │   ├── schemas.py
│   │   │       │   └── swagger.py
│   │   │       └── __init__.py
│   │   ├── common
│   │   │   ├── __init__.py
│   │   │   └── pagination.py
│   │   └── __init__.py
│   ├── extensions
│   │   ├── __init__.py
│   │   ├── cors
│   │   │   └── __init__.py
│   │   ├── database
│   │   │   └── __init__.py
│   │   ├── migrate
│   │   │   └── __init__.py
│   │   └── schema
│   │       └── __init__.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_departament.py
│   │   ├── test_dependent.py
│   │   └── test_employee.py
│   ├── __init__.py
│   ├── config.py
│   └── wsgi.py
├── contrib/
├── docs/
├── scripts/
├── .env
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── README.md
└── requirements.txt
```

The application must be run in *development* or *production* environments, via Docker. To run without Docker, install Python 3, the `requirements.txt` dependencies, Postgres and create the databases/credentials according to `.env` (.env file just for example).

## Settings

Requirements:

* Git - https://git-scm.com/downloads

* Docker - https://docs.docker.com/engine/install/

* Docker Compose - https://docs.docker.com/compose/install/

After installing the requirements:

1. Clone the repository: `git clone https://github.com/daltroedu/acmevita.git`
2. Access the directory: `cd acmevita/`
3. Export the *development* environment: `export FLASK_ENV=development`
4. *Build* the containers: `make build`
    * The first build may take a while
    * The application listens on port 5000 and the database on 5432
5. Execute the containers: `make run`
    * To run with logs/stdout: `make run-stdout`
    * Stop: `make stop`
    * These and other commands/shortcuts are available in the file `Makefile`
6. Create the migrations: `make db-init`
7. Execute: `make db-migrate`
	* `db-migrate` and `db-upgrade` work only after all Postgres configurations
8. Export to Postgres: `make db-upgrade`
9. Running the tests: `make run-tests`

## Endpoints

The endpoints are divided by context: *departaments*, *employees* and *dependents*, with *employees* being a parent resource of *dependents*.

If you use Postman, in the `contrib/` directory you have the collections for export.

API documentation (Swagger) can be accessed at: `http://localhost:5000/v1`

![swagger](docs/imgs/swagger.png)
