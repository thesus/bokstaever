#!/bin/bash

# Default options
VERSION=develop

# Argument parsing
function print_help {
    echo "Update script for bokstaever"
    echo ""
    echo "Options:"
    echo "  -p, --pull                Pulls all images"
    echo "  -b, --build               Builds docker containers for web, worker and nginx"
    echo "                            If used with pull, self build images will still be used"
    echo "  -v, --version VERSION     Version of the bokstaever images, default: $VERSION"
    echo "  -i, --bundle BUNDLE       Download bundle from given url and extract it"
    echo "                            under ./bundle"
    echo "  -c, --current             Use directory of caller instead of the scriptpath."

}


while :; do
    case $1 in
        -p|--pull)
            DO_PULL=true
        ;;
        -b|--build)
            DO_BUILD=true
        ;;
        -v|--version)
            VERSION=$2
            shift
        ;;
        -i|--bundle)
            BUNDLE_URL=$2
            shift
        ;;
        -c|--current)
            STAY=true
        ;;
        -h|--help)
            print_help
            exit 0
        ;;
        *) break
        ;;
    esac
    shift
done

if [ ! "$STAY" = true ]; then
    # cd to folder of update script
    cd "$(dirname $0)" || exit $?
fi

# File existence
if [ ! -f .env ]; then
    echo "Environment file is missing."
    exit 1
fi

if [ ! -f docker-compose.yml ]; then
    echo "Compose file is missing."
    exit 1
fi

# Download and extract bundle if specified
if [ ! -z $BUNDLE_URL ]; then
    echo "bundle is set $BUNDLE_URL"

    if [ ! -f "bundle" ]; then
        mkdir bundle
    fi

    # Download bundle
    wget -O download.zip "$BUNDLE_URL"

    rm -rf dist

    # Unzip and overwrite files in ./bundle
    unzip download.zip -d bundle .
    cp -r dist/* bundle/
fi


echo "Updating bokstaever to $VERSION"

export VERSION=$VERSION

if [ "$DO_PULL" = true ]; then
    docker-compose pull || exit $?
fi

if [ "$DO_BUILD" = true ]; then
    docker-compose build || exit $?
fi

docker-compose up -d || exit $?

echo "Applying migrations."
docker-compose run --rm web python manage.py migrate --no-input || exit $?

echo "Loading fixtures"
docker-compose run --rm web sh -c 'if [ -f bundle/fixtures.yaml ]; then python manage.py loaddata bundle/fixtures.yaml; fi'

echo "Update of bokstaever finished."
