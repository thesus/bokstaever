#!/usr/bin/env bash

# This script downloads dependencies needed for the themes
# Run from repository root (../)

declare -a packages=("https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"
                     "https://unpkg.com/imagesloaded@4/imagesloaded.pkgd.min.js"
)

for i in "${packages[@]}"
do
    case $i in
        *.js) destination=server/bokstaever/static/js;;
        *.css) destination=server/bokstaever/static/css;;
        * ) echo "\033[0;31m Unknown extension format. Don't know where to put!" && exit 1;;
    esac
    wget -N --content-disposition -P "$destination" "$i"
done
