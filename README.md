# Yamdb API final
![example workflow](https://github.com/menyanet73/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Project with titles, scores, and reviews for it. Auth by jwt.

Project can be viewed at:
http://51.250.29.80/redoc/

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
Create github secrets with your data.

```sh
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
ALLOWED_HOST=web
DOCKER_PASSWORD=your_dockerpassword
DOCKER_USERNAME=your_dockerusername
HOST=ip_server
SSH_KEY=ssh_for_server
TELEGRAM_TO=id_your_tg
TELEGRAM_TOKEN=tg_bot_token
USER=username_for_server
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