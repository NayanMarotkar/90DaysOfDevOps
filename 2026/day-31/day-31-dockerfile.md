# Day 31 – Dockerfile: Build Your Own Images

---

## Challenge Tasks

### Task 1: Your First Dockerfile
1. Create a folder called `my-first-image`
2. Inside it, create a `Dockerfile` that:
   - Uses `ubuntu` as the base image
   - Installs `curl`
   - Sets a default command to print `"Hello from my custom image!"`
3. Build the image and tag it `my-ubuntu:v1`
   <img width="691" height="235" alt="image" src="https://github.com/user-attachments/assets/f36574cd-bb53-4123-8565-e2a26c65fb37" />

5. Run a container from your image
<img width="906" height="77" alt="image" src="https://github.com/user-attachments/assets/84c073ac-8073-431b-ac61-48b42b00f3fa" />

**Verify:** The message prints on `docker run`

---

### Task 2: Dockerfile Instructions
Create a new Dockerfile that uses **all** of these instructions:
- `FROM` — base image
- `RUN` — execute commands during build
- `COPY` — copy files from host to image
- `WORKDIR` — set working directory
- `EXPOSE` — document the port
- `CMD` — default command

Build and run it. Understand what each line does.
<img width="1905" height="1005" alt="image" src="https://github.com/user-attachments/assets/f656c8c4-e9e1-43e8-9e30-1175d192c7dd" />


---

### Task 3: CMD vs ENTRYPOINT
1. Create an image with `CMD ["echo", "hello"]` — run it, then run it with a custom command. What happens?
   <img width="1013" height="428" alt="image" src="https://github.com/user-attachments/assets/1fa585fa-fcd7-4d99-85d4-a202a3835d26" />
  without custom comand it run default command and when pass argument it overwrite it and print custom command

3. Create an image with `ENTRYPOINT ["echo"]` — run it, then run it with additional arguments. What happens?
    <img width="777" height="306" alt="image" src="https://github.com/user-attachments/assets/7d4b7d86-c940-42c7-9295-fdad7821bcb1" />
  without arg it returns empty value, when passing argument it prints arg

5. Write in your notes: When would you use CMD vs ENTRYPOINT?
 CMD - command provided in cmd can be overwrite while running container.
 Entrypoint - when you pass command in entrypoint it will remain same it will not overwrite.
---

### Task 4: Build a Simple Web App Image
1. Create a small static HTML file (`index.html`) with any content
2. Write a Dockerfile that:
   - Uses `nginx:alpine` as base
   - Copies your `index.html` to the Nginx web directory
3. Build and tag it `my-website:v1`
4. Run it with port mapping and access it in your browser
   <img width="1915" height="998" alt="Screenshot 2026-03-12 062844" src="https://github.com/user-attachments/assets/a436be81-7af4-4d3f-842f-b74482b6cae1" />


---

### Task 5: .dockerignore
1. Create a `.dockerignore` file in one of your project folders
2. Add entries for: `node_modules`, `.git`, `*.md`, `.env`
3. Build the image — verify that ignored files are not included
   <img width="976" height="98" alt="image" src="https://github.com/user-attachments/assets/30dadeb0-a3f3-4a08-b2b9-7e5ab46eed25" />


---

### Task 6: Build Optimization
1. Build an image, then change one line and rebuild — notice how Docker uses **cache**
2. Reorder your Dockerfile so that frequently changing lines come **last**
   <img width="1777" height="761" alt="image" src="https://github.com/user-attachments/assets/117c436a-aa3d-41a5-bac4-e93f6b0d2dc7" />
   it will rebuild and cach will be take only for before change lines

4. Write in your notes: Why does layer order matter for build speed?
   
   Docker builds images in layers and caches each layer.
If a layer changes,Docker rebuilds that layer and all layers after it.
By placing:
Rarely changing files (dependencies) first
Frequently changing files (source code) last
Docker can reuse cached layers,resulting in faster rebuilds.

---

