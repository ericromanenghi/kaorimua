DOCKER_COMPOSE_YAML="-f docker-compose.yaml -f docker-compose.prod.yaml"

stop_container() {
    docker stop $(docker ps --filter "label=service.name=$1" -a -q)    
}

echo "Stoping running containers"
stop_container api
stop_container server

echo "Build containers"
docker-compose $DOCKER_COMPOSE_YAML build backend server

echo "Run containers"
docker-compose $DOCKER_COMPOSE_YAML up backend server