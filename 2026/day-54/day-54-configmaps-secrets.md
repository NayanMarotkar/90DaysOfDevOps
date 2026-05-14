
# Day 54: ConfigMaps and Secrets in Kubernetes

## 1. What are ConfigMaps and Secrets?

### **ConfigMap**
- Used to store **non-sensitive** configuration data.
- Stores data in plain text.
- Ideal for environment-specific settings, feature flags, configuration files, etc.

### **Secret**
- Used to store **sensitive** information (passwords, API keys, certificates, tokens, etc.).
- Data is **Base64-encoded** (not encrypted by default).
- Provides better access control and security practices compared to ConfigMaps.

**When to use each:**

| Use Case                    | ConfigMap          | Secret              |
|----------------------------|--------------------|---------------------|
| Application settings       | Yes                | No                  |
| Database credentials       | No                 | Yes                 |
| API keys / Tokens          | No                 | Yes                 |
| TLS certificates           | No                 | Yes                 |
| Nginx / App config files   | Yes                | Yes (if sensitive)  |

---

## 2. Environment Variables vs Volume Mounts

### **Environment Variables** (`env` / `envFrom`)
- Injected at **pod startup**.
- Simple key-value configuration.
- **Do NOT update** automatically when ConfigMap/Secret is updated.
- Best for simple settings (`APP_ENV`, `DB_HOST`, etc.).

### **Volume Mounts**
- Files are created inside the container.
- **Automatically updated** (for ConfigMaps) when the source changes.
- Best for complex configuration files (`nginx.conf`, `application.yml`, etc.).
- Each key becomes a separate file.

**Recommendation:**
- Use **environment variables** for simple values.
- Use **volume mounts** for full configuration files.

---

## 3. Why Base64 is Encoding, Not Encryption


# Example from earlier task
echo -n 's3cureP@ssw0rd' | base64
# Output: czNjdXJlUEBzc3cwcmQ=

## Important Concepts

### 1. Base64 Encoding in Secrets

**Base64 is encoding, NOT encryption.**

- It is **reversible** — anyone who can read the Secret can decode it easily.
- It only prevents accidental exposure of binary data or special characters.
- **Not secure** against determined attackers.

**Real security comes from:**
- Proper **RBAC** (restrict who can read Secrets)
- **Encryption at Rest** (enabled in etcd)
- External secret managers (Vault, AWS Secrets Manager, etc.)

> **Rule of thumb**: Never treat Kubernetes Secrets as strongly encrypted storage.

---

### 2. ConfigMap Update Propagation Behavior

| Method                  | Updates Automatically? | Requires Pod Restart? | Recommended Use Case          |
|-------------------------|------------------------|-----------------------|-------------------------------|
| Volume Mount            | Yes (after ~1 min)     | No                    | Config files (recommended)    |
| Environment Variables   | No                     | Yes                   | Simple settings               |

**Key Takeaway:**

- When a ConfigMap is updated:
  - **Volume-mounted files** are automatically refreshed by the kubelet.
  - **Environment variables** remain unchanged until the pod is restarted.

This is why **mounting configuration as volumes** is preferred for applications that support hot-reloading or need dynamic configuration updates.

---

**Best Practices Summary:**

- Use **ConfigMaps** for non-sensitive configuration.
- Use **Secrets** for sensitive data (with proper RBAC).
- Prefer **volume mounts** for configuration files.
- Prefer **environment variables** for simple key-value settings.
- Always assume Secrets can be decoded if someone has read access.
