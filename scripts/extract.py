import os
import json
import sqlite3
import requests
import pandas as pd

from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv


# Load API Key


load_dotenv()

API_KEY = os.getenv("API_KEY")


# Paths


BASE_DIR = Path(__file__).resolve().parent.parent

BRONZE_DIR = BASE_DIR / "data" / "bronze"

DB_PATH = BASE_DIR / "database" / "crypto.db"

BRONZE_DIR.mkdir(parents=True, exist_ok=True)


# API Request


url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": False
}

headers = {
    "x-cg-demo-api-key": API_KEY
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=30
)

response.raise_for_status()

data = response.json()

print(f"Fetched {len(data)} records")


# Save Raw JSON (Bronze)


timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

json_file = BRONZE_DIR / f"{timestamp}.json"

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Bronze file saved: {json_file.name}")


# Create DataFrame


df = pd.DataFrame(data)

keep_cols = [
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "market_cap_rank",
    "total_volume",
    "price_change_percentage_24h",
    "circulating_supply",
    "last_updated"
]

silver_df = df[keep_cols].copy()

# Fix Nulls

silver_df["price_change_percentage_24h"] = (
    silver_df["price_change_percentage_24h"]
    .fillna(0)
)

# Datetime

silver_df["last_updated"] = pd.to_datetime(
    silver_df["last_updated"]
)

silver_df["fetch_time"] = datetime.now()


# SQLite Load


# conn = sqlite3.connect(DB_PATH)

# silver_df.to_sql(
#     "crypto_market",
#     conn,
#     if_exists="append",
#     index=False
# )

# conn.close()

# print(f"Inserted {len(silver_df)} rows into crypto_market")