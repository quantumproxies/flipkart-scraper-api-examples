"""Minimal Flipkart search API call — one typed row per product.

Docs & schema: https://quanticdata.io/collectors/flipkart-scraper-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/flipkart_search/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "query": "headphones",
        "max_results": 24
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("product_id"), row.get("title"), row.get("subtitle"))
print(f"{len(data['results'])} products, cost ${data['cost']}")
