#!/bin/bash

for d in esims/*; do
  echo "$d"
  (cd $d; python ../../src/main.py .)
  echo ""
done
