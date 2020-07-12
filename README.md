# Bokstaever
[![pipeline status](https://dev.cryptec.at/root/bokstaever/badges/develop/pipeline.svg)](https://dev.cryptec.at/root/bokstaever/commits/develop) [![coverage report](https://dev.cryptec.at/root/bokstaever/badges/develop/coverage.svg)](https://dev.cryptec.at/root/bokstaever/commits/develop)

Host your own website with support for blogging, editing pages and external static content. It's a cms written in Python featuring the
awesome webframework Django.

Current Features:

- formatting of posts and pages via markdown
- fully customizable templates
- ability to load static pages with external dependencies
- Image upload and resizing

# Getting started

To quickly setup a development environment create a virtual environment
and install the requirements.

````bash
pip install -r requirements/base.txt
````

The templates are split into different repositories. Download a bundle that suits you and include it in `src/bokstaever/bundles`.

Migrate the database. The default is a postgresql database named `bokstaever`  If you're in a hurry use a sqlite database with ``export DATABASE_URL=sqlite:////tmp/bokstaever.sqlite``.

````bash
# in /src
python manage.py migrate
````

The dashboard requires some staticfile dependencies, they can be installed with:
````bash
# in /src
python manage.py install_dependencies ../requirements/static.json
````

Start your development server with:
````bash
# in /src
python manage.py runserver
````
