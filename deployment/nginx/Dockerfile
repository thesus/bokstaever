# DJANGO BUILDER
FROM python:3.8 as django_builder

COPY requirements/ /requirements
COPY src/ /src

# Install requirements.
RUN pip install -r /requirements/base.txt

# Collect static files
WORKDIR /src

# Mock external template/static folder
RUN mkdir -p bundle/static/

# Download static dependencies
RUN python manage.py install_dependencies ../requirements/static.json

# Collectstatic
RUN python manage.py collectstatic --noinput

FROM nginx:alpine

# Copy django's static files
COPY --from=django_builder /src/static /srv/static

COPY /deployment/nginx/default.conf /etc/nginx/conf.d/default.conf

