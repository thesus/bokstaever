# DJANGO BUILDER
FROM python:3.8 as django_builder

# Install gettext for compiling translations
RUN apt-get update && apt-get install -y npm && npm install -g sass

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

# Compile scss and remove sources
RUN sass bokstaever dashboard

# Collectstatic
RUN python manage.py collectstatic --noinput

FROM nginx:alpine

# Copy django's static files
COPY --from=django_builder /src/static /srv/static

COPY /deployment/nginx/default.conf /etc/nginx/conf.d/default.conf

