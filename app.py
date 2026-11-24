import sys
import os

from flask import Flask, jsonify

app = Flask(__name__)

# Injected at build time by the pipeline (git SHA), so a running
# container can tell you which commit it was built from.
APP_VERSION = os.environ.get("APP_VERSION", "dev")


@app.route("/")
def index():
    return jsonify(message="Hello from the CI/CD POC", version=APP_VERSION)


@app.route("/health")
def health():
    # Later used by smoke tests, the load balancer, and ECS health checks.
    return jsonify(status="ok"), 200


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify(result=a + b)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
