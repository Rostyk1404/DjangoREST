# DjangoREST

DjangoREST

Description
ToDo

Technologies
Python (3.8.2)
PostgreSQL (10.5)
Install
For the next steps of service installation, you will need setup of Ubuntu OS

Install and configure PostgreSQL server on your local machine:
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql postgres

postgres=# \password
Enter new password:
Enter it again:

postgres=# CREATE DATABASE your_custom_db_name;

postgres=# \q
Go to the cloned repository and install requirement project's packages
pip install -r requirements.txt
Go to the iBudget/ibudget project directory and create your own local_settings.py in the folder with settings.py and configure correct database connection.
SECRET_KEY = "YOUR_SECRET_KEY_FOR_DJANGO_APP"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_custom_db_name',
        'USER': 'your_custom_db_user',
        'PASSWORD': 'your_password_for_user_above',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Djangorestframework Installation
Install using pip, including any optional packages you want...

pip install djangorestframework

# Markdown support for the browsable API.
pip install markdown

# Filtering support       
pip install django-filter  

...or clone the project from github.

git clone https://github.com/encode/django-rest-framework

Add 'rest_framework' to your INSTALLED_APPS setting.

INSTALLED_APPS = [
    ...
    'rest_framework',
]
If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.

urlpatterns = [
    ...
    url(r'^api-auth/', include('rest_framework.urls'))
]

Run Django Project

Go to the folder with manage.py file, run DjangoREST.api

python manage.py runserver
