import base64
import json
import requests
from flask import Request

# Jenkins details (change these accordingly)
JENKINS_URL = "http://jenkins-server:8080"
JENKINS_USER = "username"
JENKINS_API_TOKEN = "token"

# Map branches to Jenkins jobs
BRANCH_JOB_MAP = {
    "main": "testblp2",
    "test": "test-pipeline"
}

def trigger_jenkins_job(job_name):
    job_url = f"{JENKINS_URL}/job/{job_name}/build"
    response = requests.post(job_url, auth=(JENKINS_USER, JENKINS_API_TOKEN))
    return response.status_code, response.text

def pubsub_trigger(request: Request):
    if request.method != "POST":
        return "Method not allowed", 405

    envelope = request.get_json(silent=True)
    if not envelope or "message" not in envelope:
        return "Invalid Pub/Sub message format", 400

    pubsub_message = envelope["message"]
    if "data" not in pubsub_message:
        return "No data in Pub/Sub message", 400

    # Decode base64 data
    payload_str = base64.b64decode(pubsub_message["data"]).decode("utf-8")
    payload = json.loads(payload_str)

    branch = payload.get("branch")
    if not branch:
        return "No branch found", 400

    job_name = BRANCH_JOB_MAP.get(branch)
    if not job_name:
        return f"No Jenkins job mapped for branch '{branch}'", 200

    status_code, response_text = trigger_jenkins_job(job_name)

    if status_code == 201:
        return f"Triggered Jenkins job '{job_name}' for branch '{branch}'", 201
    else:
        return f"Failed to trigger Jenkins job: {response_text}", status_code
