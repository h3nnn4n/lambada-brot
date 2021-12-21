#!/bin/bash

BODY="{
  \"xmin\": \"-0.742030\",
  \"ymin\": \"0.125433\",
  \"xmax\": \"-0.744030\",
  \"ymax\": \"0.127433\",
  \"size\": \"256\"
}"

curl -XPOST https://4j10ejf71g.execute-api.us-east-1.amazonaws.com/mandel -d "${BODY}"
