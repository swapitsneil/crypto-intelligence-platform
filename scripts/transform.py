import json
import sqlite3
import pandas as pd

from pathlib import Path
from datetime import datetime


# Paths

BASE_DIR = Path(__file__).resolve().parent.parent

BRONZE_DIR = BASE_DIR / "data" / "bronze"
SILVER_DIR = BASE_DIR / "data" / "silver"
DB_PATH = BASE_DIR / "database" / "crypto.db"

POWERBI_DIR = BASE_DIR / "powerbi"

POWERBI_DIR.mkdir(parents=True, exist_ok=True)

SILVER_DIR.mkdir(parents=True, exist_ok=True)


# Latest Bronze File

latest_file = max(
    BRONZE_DIR.glob("*.json"),
    key=lambda x: x.stat().st_mtime
)

print(f"Reading: {latest_file.name}")


# Read JSON

with open(latest_file, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)


# Select Columns

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



# Cleaning

silver_df["price_change_percentage_24h"] = (
    silver_df["price_change_percentage_24h"]
    .fillna(0)
)

silver_df["last_updated"] = pd.to_datetime(
    silver_df["last_updated"]
)

silver_df["fetch_time"] = datetime.now()



# Save Silver CSV


timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

silver_file = SILVER_DIR / f"silver_{timestamp}.csv"

silver_df.to_csv(
    silver_file,
    index=False
)

print(f"Silver file saved: {silver_file.name}")

# Power BI Export

powerbi_file = POWERBI_DIR / "crypto_market.csv"

silver_df.to_csv(
    powerbi_file,
    index=False
)

print(f"Power BI file saved: {powerbi_file.name}")




# Load to SQLite


conn = sqlite3.connect(DB_PATH)

silver_df.to_sql(
    "crypto_market",
    conn,
    if_exists="append",
    index=False
)

conn.close()

print(f"Inserted {len(silver_df)} rows")