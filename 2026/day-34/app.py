from flask import Flask, jsonify
import mysql.connector
import redis
import os

app = Flask(__name__)

# Environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_USER = os.getenv("MYSQL_USER", "user")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
MYSQL_DB = os.getenv("MYSQL_DB", "testdb")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")

# Redis client
cache = redis.Redis(host=REDIS_HOST, port=6379)

def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

@app.route("/")
def home():
    # Redis counter
    count = cache.incr("hits")

    # MySQL check
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        conn.close()
    except Exception as e:
        db_name = str(e)

    return jsonify({
        "message": "Flask + MySQL + Redis 🚀",
        "visits": int(count),
        "database": db_name
    })

@app.route("/health")
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
