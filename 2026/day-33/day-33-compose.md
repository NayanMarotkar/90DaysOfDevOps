# Day 33 – Docker Compose: Multi-Container Basics

---

## Challenge Tasks

### Task 1: Install & Verify
1. Check if Docker Compose is available on your machine
2. Verify the version
<img width="543" height="63" alt="Screenshot 2026-03-17 214640" src="https://github.com/user-attachments/assets/46c97269-9020-4310-bb24-d487416d4448" />

'Docker Compose version v5.0.1'

---

### Task 2: Your First Compose File
1. Create a folder `compose-basics`
2. Write a `docker-compose.yml` that runs a single **Nginx** container with port mapping
3. Start it with `docker compose up`
4. Access it in your browser
   <img width="1916" height="965" alt="Screenshot 2026-03-17 220413" src="https://github.com/user-attachments/assets/03d0d5e6-8aeb-40dd-b9e8-9ef871b77ea7" />

6. Stop it with `docker compose down`
<img width="1427" height="849" alt="image" src="https://github.com/user-attachments/assets/0e41a4d8-a112-4f28-ac22-c0362e6ab01f" />

---

### Task 3: Two-Container Setup
Write a `docker-compose.yml` that runs:
- A **WordPress** container
- A **MySQL** container

They should:
- Be on the same network (Compose does this automatically)
- MySQL should have a named volume for data persistence
- WordPress should connect to MySQL using the service name

Start it, access WordPress in your browser, and set it up.
<img width="1894" height="950" alt="Screenshot 2026-03-17 224024" src="https://github.com/user-attachments/assets/fbef4a1f-2d9d-42e4-b7e1-612e7549f232" />


**Verify:** Stop and restart with `docker compose down` and `docker compose up` — is your WordPress data still there?
<img width="886" height="143" alt="image" src="https://github.com/user-attachments/assets/6612889c-5c53-4555-8932-b54e3205510f" />
<img width="1895" height="152" alt="image" src="https://github.com/user-attachments/assets/1675e180-f459-4083-8121-194988ec1c42" />
<img width="1898" height="844" alt="image" src="https://github.com/user-attachments/assets/3d450067-49a1-42dd-8913-14b51a4ceaee" />

---

### Task 4: Compose Commands
Practice and document these:
1. Start services in **detached mode**
   <img width="1890" height="161" alt="image" src="https://github.com/user-attachments/assets/22fa0863-1642-4af8-873a-bc55265f3526" />

3. View running services
  <img width="1717" height="133" alt="image" src="https://github.com/user-attachments/assets/6dc7194a-81f2-4010-b4b7-1cbe39a48f35" />

4. View **logs** of all services
<img width="1902" height="963" alt="image" src="https://github.com/user-attachments/assets/f388b45f-4260-4800-9d55-68a266db79fa" />

5. View logs of a **specific** service
   <img width="1919" height="745" alt="image" src="https://github.com/user-attachments/assets/8629181f-a666-4fda-a687-89791c502046" />

7. **Stop** services without removing
   <img width="765" height="120" alt="image" src="https://github.com/user-attachments/assets/c5947cf4-88a4-4df9-b2d5-de9081e904d8" />

9. **Remove** everything (containers, networks)
<img width="1034" height="149" alt="image" src="https://github.com/user-attachments/assets/3a0a4949-3379-4959-a649-d729a7f28b5c" />

10. **Rebuild** images if you make a change
<img width="1615" height="441" alt="image" src="https://github.com/user-attachments/assets/e3ae5d1b-50a2-49ab-bc05-753c1826f8dd" />

---

### Task 5: Environment Variables
1. Add environment variables directly in your `docker-compose.yml`
2. Create a `.env` file and reference variables from it in your compose file
3. Verify the variables are being picked up
   <img width="946" height="302" alt="image" src="https://github.com/user-attachments/assets/dba1c4d4-a267-4b9c-8170-f4c7f3c57586" />


