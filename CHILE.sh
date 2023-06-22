#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/scripts/

python3 CHILE.py > ../CHILE.m3u

echo m3u grabbed
