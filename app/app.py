from flask import Flask
import redis
import os

app = Flask(__name__)

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = 6379
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.route("/")
def index():
    count = r.incr("counter")
    return f"<h1>Hello! This page has been visited {count} times.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
