from flask import Flask, render_template
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        environment=os.getenv("ENVIRONMENT", "Development"),
        version=os.getenv("APP_VERSION", "1.0.0"),
        time=datetime.now()
    )

@app.route("/health")
def health():
    return {
        "status": "UP"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)