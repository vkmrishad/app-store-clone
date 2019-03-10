## Starting app

    $ python manage.py runserver

The app will be served by django **runserver**

Access it through **http://localhost:8000**

## Running tests

    $ python manage.py test

## Setup of development environment

First install required dependencies.

After that, create your virtualenv:

    $ virtualenv -p python3.6 env3
    
Activate virtualenv:

    $ source <path>/env3/bin/activate

Install Requirements:

    $ pip install -r requirements.txt
    
Migrate:

    $ ./manage.py migrate
    
And to start the django dev server:

    $ ./manage.py runserver
    
## Missing Features
* Not saving any images.
* Improve scraping, searching and caching.
