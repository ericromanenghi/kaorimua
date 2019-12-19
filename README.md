# Kaori MUA

**Disclaimer:** This is still work in progress.

## Description
Source code for [kaorimua.nl](http://kaorimua.nl).

## Architecture
The website consists in three services:
  * Frontend (not implemnted yet)
  * Admin (vue.js application to create galleries and upload photos)
  * Backend (REST API implemented in flask to interact both with the frontend service and admin)

## Set up
You need to have [Docker](https://docs.docker.com/v17.09/engine/installation/) and [Docker compose](https://docs.docker.com/compose/install/)

Then, you can build and start the services with `docker-compose up <service>`:

`$ docker-compose up backend`, after service is up you should be able to access the API in `http://localhost:5000/`

`$ docker-compose up admin`, after service is up you should be able to access the API in `http://localhost:8000/`

`$ docker-compose up frontend`, after service is up you should be able to access the API in `http://localhost/`


If a change is made in the Dockerfile, you mgiht need to re-build the container using the `build` command:

`$ docker-compose build <service>` where service should be either `admin`, `frontend` or `backend`

The docker-compose file is configured to mount the files in the containers, and the dev servers are configured to reload after you save your changes, so you don't need to rebuild the services unless you change the Dockerfiles or the docker-compose file. If for some reason you need to restart a service, just run again the `docker-compose up <service>` command.
