#!/usr/bin/env sh

# This script is for compiling the dashboard in the caddy container with the correct urls

cd /srv/src
rm dist

yarn

yarn build

rm /srv/dashboard
mv /srv/src/dist /srv/dashboard
