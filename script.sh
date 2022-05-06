#!/bin/bash

minikube start --ports=30000:30000,32000:32000 \
&& kubectl apply -f Deployments/json-app-deployment.yaml \
&& kubectl apply -f Services/json-app-service.yml \
&& kubectl apply -f Deployments/string-app-deployment.yaml \
&& kubectl apply -f Services/string-app-service.yml