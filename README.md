# pywu
Python Workstation Update

## Requirements
    Python 3.6.9

## Dependencies
    django
    django_extensions
    psycopg2_binary


## Database
```sh
    docker run -d \
        --name pywudb \
        -e POSTGRES_PASSWORD=admin \
        -e PGDATA=/var/lib/postgresql/data/pgdata \
        -p 5432:5432 \
        -v /pg_data:/var/lib/postgresql/data:z \
        postgres
```