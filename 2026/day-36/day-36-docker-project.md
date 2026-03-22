# Day 36 – Docker Project: Dockerize a Full Application

---

## Challenge Tasks

### Task 1: Pick Your App
Choose **one** of these (or use your own project):
- A **Python Flask/Django** app with a database
- A **Node.js Express** app with MongoDB
- A **static website** served by Nginx with a backend API
- Any app from your GitHub that doesn't have Docker yet
<img width="1919" height="843" alt="image" src="https://github.com/user-attachments/assets/9a50dd9f-dbc6-4076-8e11-76df97c3b294" />
 <img width="1723" height="86" alt="image" src="https://github.com/user-attachments/assets/9fa7719e-1dad-4014-862e-96aa04036274" />

If you don't have an app, clone a simple open-source one and Dockerize it.

---

### Task 2: Write the Dockerfile
1. Create a Dockerfile for your application
2. Use a **multi-stage build** if applicable
3. Use a **non-root user**
4. Keep the image **small** — use alpine or slim base images
5. Add a `.dockerignore` file
<img width="1723" height="86" alt="image" src="https://github.com/user-attachments/assets/ef60b43c-bdb3-40ca-b551-84ec3ee589df" />

Build and test it locally.

---

### Task 3: Add Docker Compose
Write a `docker-compose.yml` that includes:
1. Your **app** service (built from Dockerfile)
2. A **database** service (Postgres, MySQL, MongoDB — whatever your app needs)
3. **Volumes** for database persistence
4. A **custom network**
5. **Environment variables** for configuration (use `.env` file)
6. **Healthchecks** on the database

Run `docker compose up` and verify everything works together.
<img width="1723" height="86" alt="image" src="https://github.com/user-attachments/assets/31b965f8-a128-43d2-9c8c-5ba54e2026a8" />

---

### Task 4: Ship It
1. Tag your app image
2. Push it to Docker Hub
3. Share the Docker Hub link
4. Write a `README.md` in your project with:
   - What the app does
     
   - How to run it with Docker Compose
   - Any environment variables needed
<img width="1136" height="332" alt="image" src="https://github.com/user-attachments/assets/f2d65df2-658f-4aaf-a69a-2c8158af6f91" />
https://github.com/NayanMarotkar/task-manager-app
---

### Task 5: Test the Whole Flow
1. Remove all local images and containers
2. Pull from Docker Hub and run using only your compose file
3. Does it work fresh? If not — fix it until it does
   <img width="1916" height="402" alt="image" src="https://github.com/user-attachments/assets/54904136-95ff-45a9-bca2-b07477d4de2d" />


---
