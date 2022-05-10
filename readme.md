# bookkeeper

**Template repository for the dockerized django apps based on postgresql database..**

> `/app/main` directory created by `'$ django-admin startproject main'` command. You can use this project as your main project or just remove it and create new one.

> Default admin user is : `username: 'admin', password: '123456@@' ` for the django admin panel. 
___
## Preparing : 

0. Clone the repo
1. Copy `env.txt` to `app/.env`
2. Change the specific fields in `app/.env`
3. Update the entrypoint.sh file permissions locally: `chmod +x app/entrypoint.sh`
4. Build the image : `docker-compose build`
4. Run the container : `docker-compose up -d`
5.  Follow outputs alive and track errors, to make continuous development: `docker logs --follow bookkeeper-app`

## Usefull Commands

```
# Start services at background :
    $ docker-compose up -d --build
```

```
# Follow outputs alive and track errors, to make continuous development : 
    $ docker logs --follow bookkeeper-app
```

```
# One-shot command :  
    $ docker-compose up -d --build; docker logs --follow bookkeeper-app
```

```
# Build the image: 
    $ docker-compose build
```

```
# Once the image is built, run the container : 
    $ docker-compose up -d
```

```
# Build the new image and spin up the two containers:
    $ docker-compose up -d --build
```

```
Run the migrations:
    $ docker-compose exec web python manage.py migrate --noinput
```

```
To remove the volumes along with the containers :
    $ docker-compose down -v
```

```
Ensure the default Django tables were created: 
    $ docker-compose exec db psql --username=enivicivokki_user --dbname=enivicivokki_db
    # \l
    # \c enivicivokki_db
    # \dt
    # \q
```

```
# You can check that the volume was created as well by running:
    $ docker volume inspect bookkeeper_postgresql_data
```

```
# Run migrations manually : 
    $ docker-compose exec web python manage.py flush --no-input
    $ docker-compose exec web python manage.py migrate
```


