import json
import requests
from google.cloud import storage
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def fetch_and_store(request):
    try:
        url = "https://fantasy.premierleague.com/api/bootstrap-static/"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        client = storage.Client()
        bucket = client.bucket("fpl-data-bucket-anjali")
        blob = bucket.blob("fpl_data.json")
        blob.upload_from_string(data=json.dumps(data), content_type="application/json")

        return "Data uploaded to Cloud Storage", 200

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
