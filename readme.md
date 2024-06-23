# Setting Up Django Project with PostgreSQL

This guide will walk you through setting up a Django project with PostgreSQL as the database backend.

## Installation Steps

### 1. Install PostgreSQL

If PostgreSQL is not already installed on your system, follow these steps to install it:

```sh
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Create PostgreSQL Database and User
Once PostgreSQL is installed, you need to create a database and a user for your Django project:

```sh
- sudo -i -u postgres
- psql
```

In the PostgreSQL prompt, execute the following commands:

```sh
CREATE DATABASE schooldb;
CREATE USER root WITH PASSWORD 'root';
ALTER ROLE root SET client_encoding TO 'utf8';
ALTER ROLE root SET default_transaction_isolation TO 'read committed';
ALTER ROLE root SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE schooldb TO root;
```

Then change the settings.py

```sh

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'schooldb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

```sh
python manage.py makemigrations
python manage.py migrate
```

```sh
python manage.py runserver
```

