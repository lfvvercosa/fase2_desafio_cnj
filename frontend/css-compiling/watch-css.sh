#!/bin/bash
css-compiling/clean-css.sh

function watch_component {
  if [[ $1 == *".scss" ]]; then
    f="$2/"$1
    sass --watch $f $(echo $f | sed "s/scss/css/") &
    echo "watching $f"
  fi
}

function watch_layouts {
  layout=$(ls css/layout)
  for l in $layout; do
    if [[ $l == *".scss" ]]; then
      f="css/layout/"$l
      sass --watch $f $(echo $f | sed "s/scss/css/") &
      echo "watching $f"
    fi
  done
}

components=$(ls css/index/components)
for c in $components; do
  watch_component $c 'css/index/components'
done

components=$(ls css/comparing-courts/components)
for c in $components; do
  watch_component $c 'css/comparing-courts/components'
done

watch_layouts