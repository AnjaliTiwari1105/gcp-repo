# FPL GCP Pipeline

This project demonstrates how to use Google Cloud Platform (GCP) to fetch data from the Fantasy Premier League (FPL) public API, store it in Cloud Storage, and later load it into BigQuery.

## Files

- `main.py`: Cloud Run function to fetch and store FPL data.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Files to exclude from version control.
- `README.md`: Project overview and setup instructions.

## Setup Instructions

1. Create a GCP project and enable Cloud Run, Cloud Storage, and BigQuery APIs.
2. Create a Cloud Storage bucket and note the name.
3. Replace `"your-bucket-name"` in `main.py` with your actual bucket name.
4. Deploy the function to Cloud Run using the GCP Console or Cloud Shell.
5. Trigger the function to fetch and store data in your bucket.
