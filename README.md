# Cloud Computing Project SS24 - Technische Universität Ilmenau
## By Ismail Farooq, Komal Ashraf and Ghazal Ashraf - GROUP K
Implementing autoscaling for image classification Inference service in a K8s cluster

Components Include

## Load Tester
Sending queries to the ML service based on a workload pattern (queries/s).

- Sample images for testing - https://github.com/EliSchwartz/imagenet-sample-images
- Load tester provided - https://github.com/reconfigurable-ml-pipeline/load_tester

## Dispatcher
A centralized queue to receive queries and dispatch/load balance them to the ML service replicas.


## Containerized Image Classification Service


## Monitoring Tool


## Autoscaler


## MISC
- Deploying Pods using declarative method (Using yaml files): 
```kubectl apply –f nginx_pod.yaml```


## Steps to run the application

### Step 1: Install Load Tester
``` pip install git+https://github.com/reconfigurable-ml-pipeline/load_tester ```

