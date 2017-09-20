#! /bin/bash

echo "Compressing..."
zip -r -q pkg.zip csv/ lib/ matches/ main.py
echo "Folders csv, lib, matches compressed."