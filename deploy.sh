#!/bin/bash

rm *.zip
zip -r main main.py
cd tf
cp ../main.zip .
aws s3 cp main.zip s3://lambada-brot/main.zip
terraform apply -auto-approve
cd ..
