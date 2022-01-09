# django-rest-framework-boilerplate

This is as RESTful-API boilerplate implemented with django rest_framework

`requirements.txt` Contains python packages required to run the app

`logging_config_FileRotator.ini` Contains logging configuration (Level, Message Formating,  Rotating Files configuration)

`logging_config_stream.ini` Contains logging configuration for stream handler 

You can however combine the two logging config files into one to have both streaming handler and the file rotator handler (more on this can be found in the official docs https://docs.python.org/3/library/logging.config.html#module-logging.config)

## 1. Production Ready Architecture:

![alt text](https://github.com/MustaphaAmine/django-rest-framework-boilerplate/blob/main/images/production_ready_architecture.png)

### 1.1 Why use WSGI servers ?

Frameworks are not made to process thousands of requests and determine how to best route them from the server. `WSGI` servers (Web Server Gateway Interface) are designed to handle many requests concurrently. 
There are numerous `WSGI` servers,In this boilerplate project, I used `Gunicorn` as it works with django right out of the box and it is easy to implement.

### 1.2 Why use Nginx ?

`Nginx` will handle requests for static ressource (in this project I didn't need to send any static files so I don't actually need it, However, in your own application, if you are building a website you will most certainly need it).

## 2. Kubernetes Deployment Architecture:

![alt text](https://github.com/MustaphaAmine/django-rest-framework-boilerplate/blob/main/images/k8s_architecture.png)

- The `Deployment` Will manage pods that runs the docker container
- The `ClusterIP Service` Will provide access to the pods inside of the deployment
- `Nginx Ingress Service` Will expose our `ClusterIP Service` (https://github.com/kubernetes/ingress-nginx)

## 4. CI/CD with `cloudbuild.yaml` file:

In order to implement the CI/CD pipeline I used GCP triggers, for that we configure the `cloudbuild.yaml` file.
For that we configuer the build trigger to watch for a Push to a branch/ Push new tag/ Pull request and execute the following sequence:
1. Create the docker image.
2. Push the image to the GCR (Google Cloud Registry)
3. We apply the update to Kubenetes components
4. To update a deployment's docker imgae we need to use an imperative command

## 5. Simple request with curl:

`GET /app-path/app-subpath/`

    curl -X GET http://your-domail-here/app-path/app-subpath/ \
            -H "Content-Type: application/json"  \
            --data @Example.json