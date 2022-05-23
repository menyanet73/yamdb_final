# Yamdb API final
![example workflow](https://github.com/menyanet73/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
Project with titles, scores, and reviews for it. Auth by jwt.

#### Stack: 
Python 3, Django 2.2, DRF, PyJWT

## How start project:

Clone a repository and go to command line:

```sh
git clone https://github.com/menyanet73/infra_sp2.git
```

```sh
cd infra_sp2/infra/
```
Create .env file in infra dir. Fill .env file with your data.

```sh
DB_NAME=postgres (default)
POSTGRES_USER=postgres (default)
POSTGRES_PASSWORD=postgres (default)
DB_HOST=db (default)
DB_PORT=5432 (default)
ALLOWED_HOST= your server ip (default - all allowed)
```

Create/download docker-compose images and containers

```sh
docker-compose up
```

Apply migrations:


```sh
docker-compose exec web python manage.py migrate
```

Create superuser:

```sh
docker-compose exec web python manage.py createsuperuser
```

Collect static:

```sh
docker-compose exec web python manage.py collectstatic --no-input
```

Done!

### Documentation of API will be aviable in
```sh
127.0.0.1:8000/redoc/
```
### Авторы
##### https://github.com/menyanet73
##### https://github.com/sproggi 
##### https://github.com/eraline