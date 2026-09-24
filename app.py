from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Module 5 - DevOps CI/CD</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0b1220;
                color: white;
                text-align: center;
                padding-top: 100px;
            }

            h1 {
                color: #22d3ee;
            }

            .card {
                max-width: 700px;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                background: #111827;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>DevOps CI/CD Project</h1>
            <h2>Sikandar Shah</h2>
            <p>
                Automated testing, Docker build, deployment and monitoring.
            </p>
            <p>Module 5 — Codomax Digital Solutions</p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "module-5-devops-cicd"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)