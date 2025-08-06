import base64
import json
import requests
from flask import Request

# Jenkins details (change these accordingly)
JENKINS_URL = "http://your-jenkins-domain.com"
JENKINS_USER = "your-jenkins-username"
JENKINS_API_TOKEN = "your-jenkins-api-token"

# Map branches to Jenkins jobs
BRANCH_JOB_MAP = {
    "main": "main-pipeline",
    "test": "test-pipeline"
}

def trigger_jenkins_job(job_name):
    job_url = f"{JENKINS_URL}/job/{job_name}/build"
    response = requests.post(
        job_url,
        auth=(JENKINS_USER, JENKINS_API_TOKEN)
    )
    return response.status_code, response.text

def github_webhook(request: Request):
    if request.method != 'POST':
        return "Method not allowed", 405

    try:
        payload = request.get_json(silent=True)
        if not payload:
            return "No JSON payload received", 400

        ref = payload.get("ref")  # format: "refs/heads/main"
        branch = ref.split("/")[-1] if ref else None

        if not branch:
            return "Branch not found in payload", 400

        job_name = BRANCH_JOB_MAP.get(branch)
        if not job_name:
            return f"No Jenkins job mapped for branch '{branch}'", 200

        status_code, response_text = trigger_jenkins_job(job_name)

        if status_code == 201:
            return f"Triggered Jenkins job '{job_name}' for branch '{branch}'", 201
        else:
            return f"Failed to trigger Jenkins job: {response_text}", status_code

    except Exception as e:
        return f"Error: {str(e)}", 500
