#!/usr/bin/env bash

/usr/local/bin/mogrify -resize 420 -path $HOME/Sites/church_site/images/sermon $1
cp /Users/wade/Pictures/fbc_podcast_logo.png $HOME/Desktop/fbc_podcast_logo.png
open $HOME/Sites/church_site/images/sermon