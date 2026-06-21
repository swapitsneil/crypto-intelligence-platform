import pandas as pd
from pathlib import Path



# Paths

BASE_DIR = Path(__file__).resolve().parent.parent

SILVER_DIR = BASE_DIR / "data" / "silver"
GOLD_DIR = BASE_DIR / "data" / "gold"

GOLD_DIR.mkdir(parents=True, exist_ok=True)



# Latest Silver File

latest_file = max(
    SILVER_DIR.glob("*.csv"),
    key=lambda x: x.stat().st_mtime
)

print(f"Reading: {latest_file.name}")

df = pd.read_csv(latest_file)



# Top Gainers

top_gainers = (
    df.sort_values(
        by="price_change_percentage_24h",
        ascending=False
    )
    .head(10)
)

top_gainers.to_csv(
    GOLD_DIR / "top_gainers.csv",
    index=False
)



# Top Losers


top_losers = (
    df.sort_values(
        by="price_change_percentage_24h",
        ascending=True
    )
    .head(10)
)

top_losers.to_csv(
    GOLD_DIR / "top_losers.csv",
    index=False
)



# Top Volume


top_volume = (
    df.sort_values(
        by="total_volume",
        ascending=False
    )
    .head(10)
)

top_volume.to_csv(
    GOLD_DIR / "top_volume.csv",
    index=False
)



# Market Summary


positive = (
    df["price_change_percentage_24h"] > 0
).sum()

negative = (
    df["price_change_percentage_24h"] < 0
).sum()

avg_change = round(
    df["price_change_percentage_24h"].mean(),
    2
)

btc_market_cap = (
    df.loc[
        df["symbol"] == "btc",
        "market_cap"
    ]
    .iloc[0]
)

total_market_cap = df["market_cap"].sum()

btc_dominance = round(
    (btc_market_cap / total_market_cap) * 100,
    2
)

market_heat = (
    "Bullish"
    if positive > negative
    else "Bearish"
)

summary = pd.DataFrame({
    "metric": [
        "positive_coins",
        "negative_coins",
        "average_change_pct",
        "btc_dominance_pct",
        "market_heat"
    ],
    "value": [
        positive,
        negative,
        avg_change,
        btc_dominance,
        market_heat
    ]
})

summary.to_csv(
    GOLD_DIR / "market_summary.csv",
    index=False
)

print("Gold Layer Created Successfully")