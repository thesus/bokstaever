FROM python:3.6

COPY requirements/ /requirements

RUN pip install gunicorn psycopg2
RUN pip install -r requirements/base.txt

COPY src/ /src

WORKDIR /src
ENV DJANGO_SETTINGS_MODULE=bokstaever.conf.settings.base

CMD ["/usr/local/bin/gunicorn", "-b" "0.0.0.0:80", "bokstaever.wsgi:application"]
