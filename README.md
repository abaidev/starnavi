## Description

This project is a demonstration of acquired skills. 
Main backend configurations are set <br/>
API implemented with Django REST Framework. <br/>
Data for users and posts is fetched from random-data-api

## Enviroment 

create virtual enviroment via `virtualenv venv` <br/>
to activate enviroment use:<br/>
##### `source ./venv/bin/activate` [Linux]<br/>
##### `venv\Scripts\activate` [Windows]<br/>

## Install Requirements

#### `pip install -r requirements.txt`

## Setup

create  `.env` file in main directory and fill the followings:

	SECRET_KEY = YOUR_SECRET_KEY
	DB_NAME =  YOUR_DB_NAME
	DB_USER =  YOUR_DB_USER
	DB_PASSWORD =  YOUR_DB_PASSWORD
	DB_HOST =  YOUR_DB_HOST
	DB_PORT =  YOUR_DB_PORT

#### `Windows` users:

You need to specify all these in enviroment variables (example: [Youtube](https://www.youtube.com/watch?v=bEroNNzqlF4))

## Migration

after you declare all variables and input all needed data in them. run command:
#### `python manage.py migrate`
then you need to create a superuser:
#### `python manage.py createsuperuser`

## Run server

Now you ready to go, open terminal and type command: `python manage.py runserver`. It will run the project in the development mode.<br />
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view it in the browser.

### Hunter (email verifier)
PyHunter is used as a Python wrapper for the Hunter.io v2 API


## Learn More

You can learn more in the [Django documentation](https://docs.djangoproject.com/en/3.1/).

To learn DRF, check out the [Django Rest Framework documentation](https://www.django-rest-framework.org/).

JSON Web Token Authentication support for Django REST Framework [REST framework JWT Auth](https://jpadilla.github.io/django-rest-framework-jwt/).

For hosting static and media files use [Google Cloud Storage](https://cloud.google.com/storage/docs/hosting-static-website)

[Random Data Generator](https://random-data-api.com/)

[PyHunter Documentation](https://github.com/VonStruddle/PyHunter)


