# Bokstaever
[![pipeline status](https://dev.cryptec.at/root/bokstaever/badges/develop/pipeline.svg)](https://dev.cryptec.at/root/bokstaever/commits/develop)
[![coverage report](https://dev.cryptec.at/root/bokstaever/badges/develop/coverage.svg)](https://dev.cryptec.at/root/bokstaever/commits/develop)

Host your own website. It's a kind of cms written in Python featuring the
awesome webframework Django.

Current Features:

- Upload and manage Images
- Use Galleries to display images in your posts
- Post your Stories
- Format Text in markdown

# Getting started

To quickly setup a development environment create a virtual environment
and install the requirements.

````bash
pip install -r requirements/base.txt

# in dashboard
yarn
````

After installing the requirements, compile your javascript, migrate the database
and start the development server.

````bash
# in dashboard
yarn build --mode development --watch --dest ../server/contrib
````

The templates for django are split into different repositories. Download a bundle that suits you and include it in `server/bokstaever/bundles`.

Migrate the database. By default it expects a postgresql database. If you're in a
hurry use a sqlite database with ``export DATABASE_URL=sqlite:////tmp/bokstaever.sqlite``.
````bash
# in server
python manage.py migrate
````

Start your development server with:
````bash
# in server
python manage.py runserver
````
