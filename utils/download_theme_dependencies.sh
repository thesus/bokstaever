#!/usr/bin/env bash

# This script downloads dependencies needed for the themes
# Run from repository root (../)

if [ -z "$DESTINATION" ]; then
    echo "Setting destination to server/bokstaever/static/"
    DESTINATION=server/bokstaever/static/
fi

declare -a packages=("https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"
                     "https://unpkg.com/imagesloaded@4/imagesloaded.pkgd.min.js"
)

for i in "${packages[@]}"
do
    case $i in
        *.js) extension=js;;
        *.css) extension=css;;
        * ) echo "Unknown extension format. Don't know where to put!" && exit 1;;
    esac
    wget -N --content-disposition -P "$DESTINATION$extension" "$i"
done
