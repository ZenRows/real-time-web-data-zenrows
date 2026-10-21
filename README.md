# Best Web Scraping API for Real-Time Data

Two Python scripts that collect real-time web data with Zenrows: one fetches the current version of a protected Amazon product page on demand, and one submits a list of product pages as a single Batch job that returns structured JSON.

This repository accompanies the Zenrows article [Best Web Scraping API for Real-Time Data (2026)](https://www.zenrows.com/blog/best-web-scraping-api-for-real-time-data).

## Features

- Fetches a protected, JavaScript-heavy product page with Zenrows Fetch and Adaptive Stealth Mode (`mode=auto`)
- Verifies the response by reading the page title from the returned HTML
- Submits several product URLs as one asynchronous Zenrows Batch job
- Requests structured JSON for every page with Zenrows Extract (`extract=auto`)
- Reads the API key from a `.env` file, so no key lives in the code

## Prerequisites

- Python 3.10 or later
- A Zenrows API key ([sign up free](https://app.zenrows.com/register))

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ZenRows/real-time-web-data-zenrows.git
cd real-time-web-data-zenrows
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

```bash
# macOS and Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` in the project root and add your key:

```bash
cp .env.example .env
```

```
ZENROWS_API_KEY=your_zenrows_api_key
```

You can find your API key in the [Zenrows dashboard](https://app.zenrows.com/register) after signing up.

## Project structure

```
.
├── fetch_product_page.py   # on-demand request with Fetch and mode=auto
├── create_batch_job.py     # submits product URLs as one Batch job with Extract
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## How it works

```
Product page URL
  ↓
Zenrows Fetch (mode=auto picks rendering and proxies)
  ↓
HTML of the current page
  ↓
Page title printed to confirm the right page came back

List of product URLs
  ↓
Zenrows Batch job (mode=auto, extract=auto)
  ↓
Job ID and run status printed; results are collected after the run
```

`fetch_product_page.py` is the on-demand path: your application asks for a page and gets the current version back in one request. `create_batch_job.py` is the collection path: it submits a list of URLs as one job, and Batch manages the queue, retries and job status while the pages are processed.

## Running the project

Fetch one product page:

```bash
python fetch_product_page.py
```

Submit the Batch job:

```bash
python create_batch_job.py
```

## Output

`fetch_product_page.py` prints the status code and the product page title:

```
Status code: 200
Page title: Amazon.com: Apple AirPods Pro (2nd Generation) Wireless Ear Buds with USB-C Charging, Up to 2X More Active Noise Cancelling Bluetooth Headphones, Transparency Mode, Adaptive, Personalized Spatial Audio, White : Electronics
```

`create_batch_job.py` prints the new job's ID and the status of its first run:

```
01M5ERCYJ7TSGP713TNMR1E8XY running
```

Your job ID will differ. When the run completes, each task's result holds the page HTML and a `parsed` object with the product's pricing, availability, specifications and reviews. See [Get your results](https://docs.zenrows.com/batch/setup#get-your-results) in the Batch docs to download them.

## Technologies

- Python
- Requests
- python-dotenv
- Zenrows Fetch, Extract and Batch

## Related article

This repository accompanies the Zenrows article:

**Best Web Scraping API for Real-Time Data (2026)**

https://www.zenrows.com/blog/best-web-scraping-api-for-real-time-data
