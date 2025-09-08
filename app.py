from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Kubernetes CI/CD pipeline! This is the first time I experimented with CICD pipeline. so basically waht happens:Push code to GitHub → GitHub Actions builds Docker image → pushes to GitHub Container Registry.

ArgoCD auto-syncs repo → updates Kubernetes → deploys new version.

Your app is live with CI/CD on Kubernetes 🎯"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
