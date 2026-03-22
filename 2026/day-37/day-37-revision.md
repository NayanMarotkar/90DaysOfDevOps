# Docker Interview Q&A (Quick Revision)

## 1. What is the difference between an image and a container?
Image = blueprint/template (read-only)  
Container = running instance of an image (with writable layer)

## 2. What happens to data inside a container when you remove it?
All container data is deleted unless stored in volumes or bind mounts

## 3. How do two containers on the same custom network communicate?
They communicate using container name as hostname (built-in DNS)

## 4. What does docker compose down -v do differently from docker compose down?
docker compose down     → removes containers & network  
docker compose down -v  → removes containers, network, AND volumes

## 5. Why are multi-stage builds useful?
They reduce image size by keeping only final build artifacts

## 6. What is the difference between COPY and ADD?
COPY = simple file copy  
ADD  = copy + supports URL download and auto extract tar files

## 7. What does -p 8080:80 mean?
Maps host port 8080 → container port 80

## 8. How do you check how much disk space Docker is using?
docker system df
