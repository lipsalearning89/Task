# Task

## Problem Statement:

### Containerized microservice challenge
1. Implement a piece of software exposing a JSON document:
    ```
    {
        "id": "1 "
        "message": "Hello world"
    }
    ``` 
    when visited with a HTTP client

2. Dockerize the application
3. Put the application to Minikube Kubernetes
4. Create a second application, that utilizes the first and displays a fully reversed message text rendered dynamically
5. Automate deployment of the 2 applications using a script
6. As a result of the task, provide us an archive with the deployment script (called script.sh') and all necessary files which we can use to deploy your applications and verify the solution

## Solution:

### Prerequisite:

- Docker [Installations Steps](https://docs.docker.com/engine/install/)
    - Add your user to the 'docker' group: `sudo usermod -aG docker $USER && newgrp docker` <https://docs.docker.com/engine/install/linux-postinstall/> 
- Kubectl [Installations Steps](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
- Minikube [Installations Steps](https://minikube.sigs.k8s.io/docs/start/)
- System Requirements:
    - CPU: 4 Cores
    - Memory: 4 GB
    - HDD: 25GB


### Execution Steps:

- Make the deployment script executable

    ```
    chmod +x script.sh
    ```
- Execute the deployment script
    ```
    ./script.sh
    ```
#### NOTE: This deployment script will start a Minikube cluster and deploy the Kubernetes resources in it


### Access Applications:
1. To access JSON Application visit 

    `http://localhost:30000`
    
    or from command prompt run:
    `curl localhost:30000`

2. To access Reverse String Application visit 

    `http://localhost:32000`
    
    or from command prompt run:
    `curl localhost:32000`
    
### Cleanup the cluster:
    To cleanup the resources provisioned on your machine, run:
    `minikube delete`


### Additional Information:
The docker images are created and published to Dockerhub in a publick repository.
To create docker image on your own, please use `docker build` with Dockerfiles located at 
- https://github.com/lipsalearning89/Task/blob/main/json-app/Dockerfile
- https://github.com/lipsalearning89/Task/blob/main/string-app/Dockerfile 
