1. Create django project
a. django-admin startproject covidtracker
b. python manage.py runserver 
or python manage.py runserver 8080
2. Setup mysqlclient
https://studygyaan.com/django/how-to-use-mysql-database-with-django-project
a. pip install mysqlclient 
b. install mysql server
c. open mysql client: mysql> CREATE DATABASE covidtracker;
d. update settings.py
    # settings.py
    # Database

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DB_name',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'USER': 'DB_user',
            'PASSWORD': 'DB_password',
        }
    }
3. create app inside covidtracker project
python manage.py startapp covid_tracker_app

4. Create urls.py inside covid_tracker_app
5. Update urls inside covidtracker folder 
path('covid/',include('covid_tracker_app.urls')),
6. python manage.py runserver
7. create models in covid_tracker_app/models.py
8. add 'covid_tracker_app.apps.CovidTrackerAppConfig' in installed apps in settings.py
9. python manage.py makemigrations covid_tracker_app
10. python manage.py sqlmigrate covid_tracker_app 0001
11. python manage.py migrate
12. python manage.py createsuperuser