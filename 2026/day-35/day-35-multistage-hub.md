# Day 35 – Multi-Stage Builds & Docker Hub

---

## Challenge Tasks

### Task 1: The Problem with Large Images
1. Write a simple Go, Java, or Node.js app (even a "Hello World" is fine)
2. Create a Dockerfile that builds and runs it in a **single stage**
3. Build the image and check its **size**
<img width="1154" height="976" alt="Screenshot 2026-03-19 185326" src="https://github.com/user-attachments/assets/8f8fefb7-036b-4a80-a48f-8384a6854201" />
IMAGE SIZE =  421MB
Note down the size — you'll compare it later.

---

### Task 2: Multi-Stage Build
1. Rewrite the Dockerfile using **multi-stage build**:
   - Stage 1: Build the app (install dependencies, compile)
   - Stage 2: Copy only the built artifact into a minimal base image (`alpine`, `distroless`, or `scratch`)
2. Build the image and check its size again
3. Compare the two sizes
<img width="1362" height="747" alt="image" src="https://github.com/user-attachments/assets/acdc8d62-8bb6-4148-96a6-2f1196870c2f" />
<img width="993" height="457" alt="image" src="https://github.com/user-attachments/assets/6d22ca66-9689-4cba-ac5c-d452b86cd776" />

Write in your notes: Why is the multi-stage image so much smaller?

because i used distroless image in multistage Distroless images don’t include package managers or compilers
They only run pre-built binaries (like .class or .jar)

---

### Task 3: Push to Docker Hub
1. Create a free account on [Docker Hub](https://hub.docker.com) (if you don't have one)
2. Log in from your terminal
3. Tag your image properly: `yourusername/image-name:tag`
4. Push it to Docker Hub
  <img width="1329" height="822" alt="image" src="https://github.com/user-attachments/assets/de4a9bc3-a065-4533-836d-7a0321fbfc26" />
<img width="1847" height="806" alt="image" src="https://github.com/user-attachments/assets/32ca6a25-a72f-47c7-89ad-c47a4573cfe9" />

6. Pull it on a different machine (or after removing locally) to verify

---

### Task 4: Docker Hub Repository
1. Go to Docker Hub and check your pushed image
2. Add a **description** to the repository
3. Explore the **tags** tab — understand how versioning works
4. Pull a specific tag vs `latest` — what happens?
<img width="1534" height="872" alt="image" src="https://github.com/user-attachments/assets/9c9d8627-8cd2-493a-b4c9-e410cd92e3f5" />

---

### Task 5: Image Best Practices
Apply these to one of your images and rebuild:
1. Use a **minimal base image** (alpine vs ubuntu — compare sizes)
2. **Don't run as root** — add a non-root USER in your Dockerfile
3. Combine `RUN` commands to **reduce layers**
4. Use **specific tags** for base images (not `latest`)

Check the size before and after.


