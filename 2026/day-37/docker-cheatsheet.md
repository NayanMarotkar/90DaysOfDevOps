# Docker Cheat Sheet

## Container Commands
- `docker run -d -p 8080:80 --name app nginx` — Run container in background
- `docker ps` — List running containers
- `docker ps -a` — List all containers
- `docker stop <container>` — Stop container
- `docker rm <container>` — Remove container
- `docker exec -it <container> /bin/sh` — Exec into container
- `docker logs -f <container>` — Follow container logs

## Image Commands
- `docker build -t myapp:latest .` — Build image from Dockerfile
- `docker pull nginx:latest` — Pull image from registry
- `docker push myrepo/myapp:latest` — Push image to registry
- `docker tag myapp:latest myrepo/myapp:v1` — Tag image
- `docker images` — List images
- `docker rmi <image>` — Remove image

## Volume Commands
- `docker volume create myvolume` — Create volume
- `docker volume ls` — List volumes
- `docker volume inspect myvolume` — Inspect volume
- `docker volume rm myvolume` — Remove volume

## Network Commands
- `docker network create mynet` — Create network
- `docker network ls` — List networks
- `docker network inspect mynet` — Inspect network
- `docker network connect mynet container` — Connect container to network

## Docker Compose Commands
- `docker compose up -d` — Start services in background
- `docker compose down` — Stop and remove services
- `docker compose ps` — List compose services
- `docker compose logs -f` — Follow compose logs
- `docker compose build` — Build services

## Cleanup Commands
- `docker system prune -f` — Remove unused data
- `docker container prune -f` — Remove stopped containers
- `docker image prune -f` — Remove dangling images
- `docker volume prune -f` — Remove unused volumes
- `docker system df` — Show disk usage

## Dockerfile Instructions
- `FROM ubuntu:22.04` — Base image
- `RUN apt-get update && apt-get install -y curl` — Run command during build
- `COPY . /app` — Copy files
- `WORKDIR /app` — Set working directory
- `EXPOSE 8080` — Expose port
- `CMD ["node","app.js"]` — Default command
- `ENTRYPOINT ["python","app.py"]` — Entrypoint command
