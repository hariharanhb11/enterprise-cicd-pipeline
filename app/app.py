from flask import Flask, render_template, jsonify
import os
import socket

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "dev")[:7]
ENVIRONMENT = os.getenv("ENVIRONMENT", "Practice")
DEPLOY_TIME = os.getenv("DEPLOY_TIME", "Not Available")
POD_NAME = socket.gethostname()

@app.route("/")
def home():
    return render_template(
        "index.html",
        version=APP_VERSION,
        environment=ENVIRONMENT,
        deploy_time=DEPLOY_TIME,
        pod_name=POD_NAME
    )

@app.route("/health")
def health():
    return jsonify(
        {
            "status": "UP",
            "application": "enterprise-cicd-pipeline"
        }
    )

@app.route("/version")
def version():
    return jsonify(
        {
            "version": APP_VERSION,
            "environment": ENVIRONMENT
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)