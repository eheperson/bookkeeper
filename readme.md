# bookkeeper

**Template repository for the dockerized django apps based on sqlite3 database..**

> `/app/main` directory created by `'$ django-admin startproject main'` command. You can use this project as your main project or just remove it and create new one.

> Default admin user is : `username: 'admin', password: '123456@@' ` for the django admin panel.

### **NOTE :** If yo run the development server locally (with manage.py), admin user won't be created automatically.
___
## Preparing : 

### Option 1(Docker-Compose): 
0. Clone the repo
1. Copy `env.txt` to `app/.env`
2. Change the specific fields in `app/.env` (optional)
3. Update the entrypoint.sh file permissions locally: `chmod +x app/entrypoint.sh`
4. Build the image : `docker-compose build`
5. Run the container : `docker-compose up -d`
6.  Follow outputs alive and track errors, to make continuous development: `docker logs --follow bookkeeper-app`

### Option 2 (Local): 
0. Clone the repo
1. Copy `env.txt` to `app/.env`
2. Change the specific fields in `app/.env` (optional)
3- Create virtualenv with any supported tool(conda, pipenv, venv, virtualenv etc ..)
    ```
        python3 -m vevn venv
        virtualenv --python=python3.9 venv
        conda create --python=3.9 name venv
    ```
4. Activate vevn, upgrade pip and install requirements.
    ```
        source venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
    ```
5. Run the development server :
    ```
        python manage.py runserver
    ```

## API Test Guide
### Don't forget to delete the comments that start with a sharp(#) in payload.

**library/api/list : GET**

```
    # example endpoint
    0.0.0.0:8006/library/api/list
```


```
    # no payload required
```

**library/api/detailed/&lt;int:pk&gt;: GET**

```
    # example endpoint
    0.0.0.0:8006/library/api/detailed/1

```

```
    # no payload required

```

**library/api/record : POST**

```
    # example endpoint
    0.0.0.0:8006/library/api/record
```

```
    # example data payload
    {
        "title": "2021 A Space Odyssey",
        "author": {
            "first_name": "Arthur",
            "middle_name": "Charles",
            "last_name": "Clarke",
            "date_of_birth": "1917-11-16",
            "date_of_death": "2008-03-19"
        },
        "publisher": {
            "name": "unknown",
            "address": "",
            "phone_no": ""
        },
        "genre": "1", 
        "format": "1", 
        "page_no": 340,
        "is_readed": true,
        "isbn": "unknown",
        "note": "Personal notes about book goes here",
        "published_date": "2016-08-22"
    }
```

**library/api/update/&lt;int:pk&gt; : PUT**

```
    # example endpoint
    0.0.0.0:8006/library/api/update/1
```

```
    # example data payload
    {
        "title": "2021 A Space Odyssey",
        "author": {
            "first_name": "Arthur",
            "middle_name": "Charles",
            "last_name": "Clarke",
            "date_of_birth": "1917-11-16",
            "date_of_death": "2008-03-19"
        },
        "publisher": {
            "name": "unknown",
            "address": "",
            "phone_no": ""
        },
        "genre": "1", 
        "format": "1", 
        "page_no": 340,
        "is_readed": true,
        "isbn": "unknown",
        "note": "Personal notes about book goes here",
        "published_date": "2016-08-22"
    }

```

**library/api/delete/&lt;int:pk&gt; : DELETE**

```
    # example endpoint
    0.0.0.0:8006/library/api/delete/1
```

```
    # no payload required

```
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


