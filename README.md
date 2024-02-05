# README - Project Monitoring Tools Backend

This project is primarily a backend containing APIs, developed with Django REST Framework. It is currently in active development phase and this documentation is intended for the infrastructure team for configuring and deploying the application.

## Prerequisites

- Python 3.x
- Django 4.2.7
- MariaDB

## Installing Dependencies

Install the necessary dependencies by running:

pip install -r requirements.txt

## Database Configuration

The database configuration must be completed by the infrastructure team. In settings.py, define the database parameters as follows:

'ENGINE': 'django.db.backends.mysql',
'NAME': 'db_monitoring_tools',
'USER': '<Username>',
'PASSWORD': '<Password>',
'HOST': '<Host_Address>',
'PORT': '<Port>',

Replace <Username>, <Password>, <Host_Address>, and <Port> with the specific details for your deployment environment.

## Running Migrations

To initialize the database, run:

python manage.py migrate

### Starting the Application

To start the development server:

python manage.py runserver
