from flask import Flask, render_template
import socket
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        version=os.getenv("APP_VERSION", "1.0.0"),
        environment=os.getenv("ENVIRONMENT", "Production"),
        current_time=str(datetime.datetime.now())
    )

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)