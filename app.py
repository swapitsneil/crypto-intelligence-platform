import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from pathlib import Path

from scripts.ai_analyst import generate_market_report


# page configuration

st.set_page_config(
    page_title="Crypto Intelligence Platform",
    page_icon="🚀",
    layout="wide"
)


# database

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "crypto.db"

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql(
    "SELECT * FROM crypto_market",
    conn
)

conn.close()


# sidebar

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Overview",
        "Market Intelligence",
        "AI Market Analyst",
        "About Project"
    ]
)


# latest snapshot

latest_time = df["fetch_time"].max()

latest_df = (
    df[df["fetch_time"] == latest_time]
    .copy()
)


# KPIs

total_coins = latest_df["symbol"].nunique()

total_market_cap = latest_df["market_cap"].sum()

total_volume = latest_df["total_volume"].sum()

avg_change = (
    latest_df["price_change_percentage_24h"]
    .mean()
)

positive_coins = len(
    latest_df[
        latest_df["price_change_percentage_24h"] > 0
    ]
)

negative_coins = len(
    latest_df[
        latest_df["price_change_percentage_24h"] < 0
    ]
)

market_health = (
    "🟢 Bullish"
    if positive_coins > negative_coins
    else "🔴 Bearish"
)


# top movers

gainers = (
    latest_df
    .sort_values(
        "price_change_percentage_24h",
        ascending=False
    )
    .head(10)
)

losers = (
    latest_df
    .sort_values(
        "price_change_percentage_24h",
        ascending=True
    )
    .head(10)
)

top_gainer = gainers.iloc[0]["name"]
top_loser = losers.iloc[0]["name"]


# overview

if page == "Overview":

    st.title("🚀 Crypto Intelligence Platform")
    st.caption("Real-Time Market Monitoring & Analytics")

    st.divider()

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Total Coins",
        total_coins
    )

    col2.metric(
        "Market Cap",
        f"${total_market_cap/1e12:.2f}T"
    )

    col3.metric(
        "Total Volume",
        f"${total_volume/1e9:.2f}B"
    )

    col4.metric(
        "Avg 24H Change",
        f"{avg_change:.2f}%"
    )

    col5.metric(
        "Market Health",
        market_health
    )

    st.divider()

    fig_gainers = px.bar(
        gainers,
        x="name",
        y="price_change_percentage_24h",
        title="Top 10 Gainers"
    )

    fig_losers = px.bar(
        losers,
        x="name",
        y="price_change_percentage_24h",
        title="Top 10 Losers"
    )

    c1, c2 = st.columns(2)

    with c1:
        st.plotly_chart(
            fig_gainers,
            use_container_width=True
        )

    with c2:
        st.plotly_chart(
            fig_losers,
            use_container_width=True
        )

    st.divider()

    latest_df["volume_ratio"] = (
        latest_df["total_volume"]
        / latest_df["market_cap"]
    )

    liquidity = (
        latest_df
        .sort_values(
            "volume_ratio",
            ascending=False
        )
        .head(10)
    )

    fig_liquidity = px.bar(
        liquidity,
        x="volume_ratio",
        y="name",
        orientation="h",
        title="Top Liquidity Coins"
    )

    st.plotly_chart(
        fig_liquidity,
        use_container_width=True
    )


# market intelligence

elif page == "Market Intelligence":

    st.title("📊 Market Intelligence")
    st.caption("Market Structure, Volume & Capitalization Analysis")

    volume_df = (
        latest_df
        .sort_values(
            "total_volume",
            ascending=False
        )
        .head(10)
    )

    fig_volume = px.bar(
        volume_df,
        x="name",
        y="total_volume",
        title="Top Volume Leaders"
    )

    st.plotly_chart(
        fig_volume,
        use_container_width=True
    )

    cap_df = (
        latest_df
        .sort_values(
            "market_cap",
            ascending=False
        )
        .head(10)
    )

    fig_cap = px.treemap(
        cap_df,
        path=["name"],
        values="market_cap",
        title="Top Market Cap Leaders"
    )

    st.plotly_chart(
        fig_cap,
        use_container_width=True
    )


# AI market analyst

elif page == "AI Market Analyst":

    st.title("🤖 AI Market Analyst")
    st.caption(
        "Generate AI-powered insights from live crypto market data."
    )

    summary = f"""
    Market Health: {market_health}

    Positive Coins: {positive_coins}

    Negative Coins: {negative_coins}

    Total Coins: {total_coins}

    Total Market Cap: {total_market_cap/1e12:.2f} Trillion USD

    Total Volume: {total_volume/1e9:.2f} Billion USD

    Average 24H Change: {avg_change:.2f}%

    Top Gainer: {top_gainer}

    Top Loser: {top_loser}
    """

    st.subheader("Current Market Snapshot")

    st.code(summary)

    if st.button("Generate AI Market Report"):

        with st.spinner("Analyzing market..."):

            prompt = f"""
            You are a Senior Crypto Market Analyst.

            Analyze the following live crypto market data.

            {summary}

            Generate:

            1. Market Sentiment
            2. Key Observations
            3. Risk Assessment
            4. Trading Opportunities

            Keep the response concise.

            Use bullet points.

            Maximum 250 words.
            """

            report = generate_market_report(
                prompt
            )

            st.success(
                "Analysis Complete"
            )

            st.markdown(
                "## 📋 AI Market Report"
            )

            st.markdown(
                report
            )

            


# about project

elif page == "About Project":

    st.title("ℹ️ About Project")

    st.markdown("""
    ### Crypto Intelligence Platform

    Real-Time Crypto Analytics Platform built using:

    - Python
    - CoinGecko API
    - SQLite
    - Power BI
    - Streamlit
    - Plotly
    - Gemini AI

    ### Data Engineering Pipeline

    Bronze → Raw API Data

    Silver → Cleaned Data

    Gold → Business KPIs

    ### Features

    - Live Crypto Monitoring
    - Real-Time ETL Pipeline
    - Market Health Tracking
    - Liquidity Analysis
    - Market Cap Analysis
    - Power BI Dashboard
    - Streamlit Dashboard
    - Gemini AI Market Analyst

    ### Project Goal

    Build a modern Analytics + AI platform
    that combines Data Engineering,
    Business Intelligence and Generative AI.
    """)


# footer

st.divider()

st.caption(
    f"Last Updated : {latest_time}"
)