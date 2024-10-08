#!/bin/bash

kubectl apply -f gan-inference-deployment.yaml

kubectl apply -f gan-inference-service.yaml

kubectl apply -f gan-inference-autoscaler.yaml

kubectl apply -f ingress.yaml

echo "Deployment, Service, Autoscaler, and Ingress have been applied."