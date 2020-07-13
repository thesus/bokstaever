FROM python:3.8

# Install gettext for compiling translations
RUN apt-get update && apt-get install -y gettext libgettextpo-dev

COPY requirements /requirements
COPY src /src/

# Python requirements
RUN pip install greenlet gevent gunicorn psycopg2
RUN pip install -r requirements/base.txt

WORKDIR /src

# Compile translations and remove gettext
RUN python manage.py compilemessages
RUN apt-get remove -y gettext libgettextpo-dev && \
  apt-get autoremove -y && rm -r /var/lib/apt/lists/*

# Setup with gunicorn
ENV DJANGO_SETTINGS_MODULE=bokstaever.conf.settings.base
CMD /usr/local/bin/gunicorn \
  -b 0.0.0.0:80 \
  --workers 3 \
  --worker-class gevent\
  bokstaever.wsgi:application
