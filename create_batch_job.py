# pip install requests python-dotenv
import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ZENROWS_API_KEY")
batch_url = "https://async.api.zenrows.com/v1/jobs"

headers = {
    "X-API-Key": api_key,
    "Content-Type": "application/json",
}

payload = {
    "type": "regular",
    "status": "closed",
    "zenrows_params": {
        "mode": "auto",
        "extract": "auto",
    },
    "tasks": [
        {"url": "https://www.amazon.com/dp/B0CHWRXH8B"},
        {"url": "https://www.amazon.com/dp/B09HM94VDS"},
    ],
}

response = requests.post(
    batch_url,
    headers=headers,
    json=payload,
    timeout=30,
)
response.raise_for_status()

job = response.json()
print(job["job_id"], job["latest_run"]["status"])
