#!/bin/bash
function clean_component {
  echo $1
  if [[ $1 != *".scss" ]]; then
    f="$2/$1"
    echo $f
    $(rm $f)
  fi
}

function clean_layouts {
  layout=$(ls css/layout)
  for l in $layout; do
    if [[ $l != *".scss" ]]; then
      f="css/layout/$l"
      echo $f
      $(rm $f)
    fi
  done
}

components=$(ls css/index/components)
for c in $components; do
  clean_component $c 'css/index/components'
done

components=$(ls css/comparing-courts/components)
for c in $components; do
  clean_component $c 'css/comparing-courts/components'
done

clean_layouts