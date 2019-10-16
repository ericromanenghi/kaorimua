# Kaori MUA

**Disclaimer:** This is still work in progress.

## Description
Source code for [kaorimua.nl](http://kaorimua.nl).

## Architecture
The website consists in three service:
  * Frontend (not implemnted yet)
  * Admin (vue.js application to create galleries and add photos)
  * Backend (REST API implemnted in flask to interact both with the frontend service and admin)

## Set up
You need to have [Docker](https://docs.docker.com/v17.09/engine/installation/) and [Docker compose](https://docs.docker.com/compose/install/)

Build a service:
`$ docker-compose build <service>` where service should be either `admin`, `frontend` or `backend`

Start a service:
`$ docker-compose up <service>` where service should be either `admin`, `frontend` or `backend`

The docker-compose file is configured to mount the files in the containers, and the dev servers are configured to reload after you save your changes, so you don't need to rebuild the services unless you change the Dockerfiles or the docker-compose file (you might need to restart the services though using same command as for starting the service).