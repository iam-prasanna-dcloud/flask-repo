from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Here's a brief description of your project:Flask Docker Application Pipeline: This project automates the deployment of a simple Flask application using Docker. The pipeline is configured in Jenkins to clone the application's code from a GitHub repository, build a Docker image based on a specified Dockerfile, and then push the image to Docker Hub. It leverages a declarative Jenkins pipeline to streamline the Continuous Integration/Continuous Deployment (CI/CD) process, ensuring that the application is always up-to-date and easily deployable. This setup enhances development efficiency by enabling quick iterations and testing in isolated environment"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

