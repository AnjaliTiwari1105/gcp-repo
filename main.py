import requests
import json
from google.cloud import storage

def fetch_and_store(request):
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(url)
    data = response.json()

    # Initialize Cloud Storage client
    client = storage.Client()
    bucket_name = "your-bucket-name"  # Replace with your bucket name
    bucket = client.bucket(bucket_name)
    blob = bucket.blob("fpl_data.json")

    # Upload JSON data to Cloud Storage
    blob.upload_from_string(data=json.dumps(data), content_type="application/json")

    return "Data uploaded to Cloud Storage"
