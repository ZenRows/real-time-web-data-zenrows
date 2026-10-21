# pip install requests python-dotenv
import html
import os
import re

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("ZENROWS_API_KEY")
TARGET_URL = "https://www.amazon.com/dp/B0CHWRXH8B"

params = {
    "url": TARGET_URL,
    "apikey": API_KEY,
    "mode": "auto",
}

response = requests.get(
    "https://api.zenrows.com/v1/",
    params=params,
    timeout=180,
)
response.raise_for_status()

title_match = re.search(
    r"<title[^>]*>(.*?)</title>",
    response.text,
    re.IGNORECASE | re.DOTALL,
)
if not title_match:
    raise ValueError("The response does not contain a page title.")

page_title = html.unescape(title_match.group(1)).strip()

print(f"Status code: {response.status_code}")
print(f"Page title: {page_title}")
