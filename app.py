from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Kubernetes CI/CD pipeline! This is the first time I experimented with CICD pipeline. so basically waht happens:"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
