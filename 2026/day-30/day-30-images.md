# Day 30 – Docker Images & Container Lifecycle

## Challenge Tasks

### Task 1: Docker Images
1. Pull the `nginx`, `ubuntu`, and `alpine` images from Docker Hub

<img width="928" height="569" alt="image" src="https://github.com/user-attachments/assets/b6f81843-6ede-402f-90e0-84d4c8881fbf" />

3. List all images on your machine — note the sizes
 <img width="645" height="128" alt="image" src="https://github.com/user-attachments/assets/1691fb14-b032-4106-a60f-e8c4faa30312" />

4. Compare `ubuntu` vs `alpine` — why is one much smaller?
   Ubuntu is a full-featured Linux distribution, while Alpine is a minimal distribution optimized for containers.
Ubuntu is larger because it includes GNU tools and glibc, whereas Alpine uses BusyBox and musl, making it much smaller.
6. Inspect an image — what information can you see?
<img width="1481" height="972" alt="image" src="https://github.com/user-attachments/assets/a3d31e89-29b4-4b02-8924-5c69bb0becdc" />

7. Remove an image you no longer need
<img width="983" height="331" alt="image" src="https://github.com/user-attachments/assets/2182188e-5c42-4b1b-9b18-9faaccf663d4" />

---

### Task 2: Image Layers
1. Run `docker image history nginx` — what do you see?
   <img width="1210" height="428" alt="image" src="https://github.com/user-attachments/assets/25711a85-acfc-47ad-8852-a8075402a4b0" />
A list of instructions used to build the nginx image (e.g., CMD, EXPOSE, ENTRYPOINT, COPY, RUN, ENV, LABEL) Each instruction corresponds to a layer
3. Each line is a **layer**. Note how some layers show sizes and some show 0B
Layers with a size (MB or kB) were created by instructions that modify the filesystem,such as RUN, COPY, or ADD.
Layers showing 0B were created by instructions that only change metadata, such as ENV, CMD, EXPOSE, LABEL, or ENTRYPOINT.These do not change the filesystem.
4. Write in your notes: What are layers and why does Docker use them?
   Docker layers are read-only filesystem snapshots created by each instruction in a Dockerfile (such as FROM, RUN, COPY, etc.) in Docker. Each instruction creates a new layer that stores the changes made at that step, and all the layers are stacked together to form the final Docker image. Docker uses layers because they speed up the build process through caching (unchanged layers are reused), save storage space since multiple images can share common layers, and make image downloads faster because only the missing or new layers need to be pulled instead of downloading the entire image again.

---

### Task 3: Container Lifecycle
Practice the full lifecycle on one container:
1. **Create** a container (without starting it)
3. **Start** the container
4. **Pause** it and check status
5. **Unpause** it
6. **Stop** it
7. **Restart** it
8. **Kill** it
9. **Remove** it

Check `docker ps -a` after each step — observe the state changes.
<img width="1288" height="850" alt="image" src="https://github.com/user-attachments/assets/8aa1ec41-7ab5-4e40-89f3-1ad5d97bc3b7" />


---

### Task 4: Working with Running Containers
1. Run an Nginx container in detached mode
2. View its **logs**
   <img width="1090" height="433" alt="image" src="https://github.com/user-attachments/assets/3650041c-2184-495c-b6cb-83bbfb67f98e" />

4. View **real-time logs** (follow mode)
   <img width="1897" height="534" alt="image" src="https://github.com/user-attachments/assets/793dc1e9-306e-4ae2-b7ce-203384c0c70d" />

6. **Exec** into the container and look around the filesystem
<img width="631" height="119" alt="image" src="https://github.com/user-attachments/assets/ee20901b-fb8a-4357-b63d-609e3337605b" />

8. Run a single command inside the container without entering it
<img width="855" height="102" alt="image" src="https://github.com/user-attachments/assets/dfbfd0d7-4aeb-4a9b-bbd0-b7c4bf7f7eb9" />

10. **Inspect** the container — find its IP address, port mappings, and mounts
    <img width="983" height="351" alt="image" src="https://github.com/user-attachments/assets/39e25d78-fc49-4049-b2c4-6a4bc399c861" />
    <img width="394" height="212" alt="image" src="https://github.com/user-attachments/assets/a82f6707-cdfd-43e8-b73b-24ecfced32bf" />
    <img width="399" height="82" alt="image" src="https://github.com/user-attachments/assets/b973b39a-8650-47c2-8535-31d79bed7943" />


---

### Task 5: Cleanup
1. Stop all running containers in one command
2. Remove all stopped containers in one command
3. Remove unused images
4. Check how much disk space Docker is using
   <img width="1023" height="758" alt="image" src="https://github.com/user-attachments/assets/e3695415-39a0-4731-b843-8363fc55f5b5" />


