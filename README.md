# HSE Web App project written in Django

A prototype for a bicycle booking website was developed as a project coursework. The adaptive website allows users to register on the website, view updated bicycle information and leave booking requests and questions regarding certain points about the bike.

## The technology stack

The backend chosen was the Python programming language and the Django web framework, which allows for the creation of full-fledged web applications with the possibility of connecting multiple libraries in a short period of time.
A PostgreSQL database was  chosen to store data as a more powerful and feature-rich database engine that can handle large amounts of data and support advanced features.
HTML, CSS, JS and Bootstrap library were chosen as the frontend, which provides the ability to create adaptive website layouts.

## How to set up

To install you will need to clone the repository on your local machine: `git clone https://github.com/temiksvyatov/HSERentDjango.git`

Next you will need to activate create and activate the virtual environment using the following commands:
- `virtualenv venv`
- `venv/Scripts/activate` (`source ./venv/scripts/activate`)

Then install the required libraries using pip: `pip install -r requirements`

Once installed, there are two ways to run it: via the python manage.py runserver command or via Docker.

- *In the first case*, you will need to go to the settings via the following path: `bikerenter/settings.py` and substitute your database settings in these fields (as in the example):

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cardealer_db',
        'USER': 'postgres',
        'PASSWORD': 'postgresaccount',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}`

- Next, a database is created to match your settings.
- Two commands are then run:
- `python manage.py makemigrations`
- `python manage.py migrate`

After that a single command remains to run the server: `python manage.py runserver`. The site will be accessible at `127.0.0.1:8000`.

---

- The second case requires you to uncomment the database settings located just below in the same settings file:

`DATABASES = {
    "default": ENV.db(
        "DATABASE_URL",
        default="sqlite:////{BASE_DIR}/db.sqlite3",
    )
}`

- Then run the build_docker_env.bat file (for Windows) located in the root folder: `build_docker_env.bat` (`./build_docker_env.bat`)
- With the last command, start docker containers: docker-compose up.

> To stop the server, press `Ctrl+C`. To stop the containers, use the command `docker-compose down`. To dock containers, use the command `docker-compose down -v --rmi local`.
