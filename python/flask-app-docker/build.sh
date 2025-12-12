#!/bin/bash

IMAGE_NAME="flask-app"

docker build -t ${IMAGE_NAME} . || exit 1
