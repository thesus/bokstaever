FROM python:3.6

COPY requirements/ /requirements

RUN pip install greenlet gevent gunicorn psycopg2
RUN pip install -r requirements/base.txt

COPY backend/ /src

WORKDIR /src
ENV DJANGO_SETTINGS_MODULE=bokstaever.conf.settings.base

CMD /usr/local/bin/gunicorn \
  -b 0.0.0.0:80 \
  --workers 3 \
  --worker-class gevent\
  bokstaever.wsgi:application
