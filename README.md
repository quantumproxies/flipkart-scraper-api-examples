# Flipkart search API — examples

Product search on Flipkart India — price, MRP, discount, ratings, availability.

**Live page, full schema & pricing → [quanticdata.io/collectors/flipkart-scraper-api/](https://quanticdata.io/collectors/flipkart-scraper-api/)**

Searches Flipkart.com and delivers one row per product: title, brand, current price and MRP in INR, discount percent, average rating with ratings/reviews counts, stock state, product URL and image. Read from the server-rendered state through Indian residential exits. Prices are INR — Flipkart is India-only.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/flipkart_search/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "headphones", "max_results": 24}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `query` (string, required) — What to search, e.g. "headphones".
- `max_results` (integer) — How many products to deliver at most (1–90). You pay only for delivered products.

## Output — one row per product

| field | type | description |
|---|---|---|
| `rank` | integer | 1-based position. |
| `product_id` | string | Flipkart product id (pid). |
| `title` | string | Product title. |
| `subtitle` | string | Variant line (color, size…). |
| `brand` | string | Brand. |
| `rating` | number | Average rating (null when unrated). |
| `ratings_count` | integer | Number of ratings. |
| `reviews_count` | integer | Number of written reviews. |
| `price` | number | Current price (INR). |
| `mrp` | number | List price (INR). |
| `currency` | string | Always INR. |
| `discount_pct` | integer | Discount percent. |
…and 3 more fields — full schema on the [live page](https://quanticdata.io/collectors/flipkart-scraper-api/).

## Pricing

**$0.001 per delivered product** ($1 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 2,000 products — no card required.

## Links

- This collector: https://quanticdata.io/collectors/flipkart-scraper-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
