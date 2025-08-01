import os
from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()
secret_id = 'secret-name'
project_id="projectid"
request={"name":f"copyofpath"}
response=client.access_secret_version(request)
secret_string = response.payload.data.decode("UTF-8")

def hello_world(request):
    return  secret_string