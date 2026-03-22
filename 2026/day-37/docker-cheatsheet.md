# Docker Cheat Sheet (Quick Reference)

# ------------------------------
# Container Commands
# ------------------------------
docker run -d -p 8080:80 --name app nginx     # Run container
docker ps                                      # Running containers
docker ps -a                                   # All containers
docker stop <container>                        # Stop container
docker rm <container>                          # Remove container
docker exec -it <container> sh                 # Shell into container
docker logs -f <container>                     # Follow logs

# ------------------------------
# Image Commands
# ------------------------------
docker build -t app:latest .                   # Build image
docker pull nginx:latest                       # Pull image
docker push repo/app:latest                    # Push image
docker tag app:latest repo/app:v1              # Tag image
docker images                                  # List images
docker rmi <image>                             # Remove image

# ------------------------------
# Volume Commands
# ------------------------------
docker volume create data                      # Create volume
docker volume ls                               # List volumes
docker volume inspect data                     # Inspect volume
docker volume rm data                          # Remove volume

# ------------------------------
# Network Commands
# ------------------------------
docker network create app-net                  # Create network
docker network ls                              # List networks
docker network inspect app-net                 # Inspect network
docker network connect app-net container       # Connect container

# ------------------------------
# Docker Compose Commands
# ------------------------------
docker compose up -d                           # Start services
docker compose down                            # Stop services
docker compose ps                              # List services
docker compose logs -f                         # Follow logs
docker compose build                           # Build services

# ------------------------------
# Cleanup Commands
# ------------------------------
docker system prune -f                         # Remove unused resources
docker container prune -f                      # Remove stopped containers
docker image prune -f                          # Remove unused images
docker volume prune -f                         # Remove unused volumes
docker system df                               # Disk usage

# ------------------------------
# Dockerfile Instructions
# ------------------------------
FROM node:18                                   # Base image
WORKDIR /app                                   # Set working dir
COPY . .                                       # Copy files
RUN npm install                                # Install deps
EXPOSE 3000                                    # Expose port
CMD ["npm","start"]                            # Default command
ENTRYPOINT ["node","server.js"]                # Entrypoint
