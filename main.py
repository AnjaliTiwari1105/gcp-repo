import os
import json
import requests
from flask import Flask, jsonify
from google.cloud import storage, bigquery

app = Flask(__name__)

# Configuration
BUCKET_NAME = 'fpl-data-bucket-anjali'
DATASET_ID = 'fpl_dataset'
TABLE_ID = 'fpl_data'
API_URL = 'https://fantasy.premierleague.com/api/bootstrap-static/'

# Initialize clients
storage_client = storage.Client()
bq_client = bigquery.Client()

@app.route('/', methods=['GET'])
def fetch_and_store_fpl_data():
    try:
        # Fetch data from the Fantasy Premier League API
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # Save raw JSON to Cloud Storage
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob('fpl_data.json')
        blob.upload_from_string(json.dumps(data), content_type='application/json')

        # Load data into BigQuery
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            autodetect=True,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
        )

        uri = f'gs://{BUCKET_NAME}/fpl_data.json'
        load_job = bq_client.load_table_from_uri(
            uri,
            f"{DATASET_ID}.{TABLE_ID}",
            job_config=job_config
        )
        load_job.result()  # Wait for the job to complete

        return jsonify({'status': 'success', 'message': 'Data to loaded into BigQuery'}), 200

    except requests.RequestException as e:
        return jsonify({'status': 'error', 'message': f'API request failed: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Unexpected error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
