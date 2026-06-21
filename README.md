# 🚀 Crypto Intelligence Platform

A Real-Time Cryptocurrency Analytics Platform built using **Python, CoinGecko API, SQLite, Power BI, Streamlit, Plotly, and Gemini AI**.

The platform collects live cryptocurrency market data, processes it through a modern Data Engineering pipeline, stores it in SQLite, visualizes insights using Power BI and Streamlit, and generates AI-powered market reports using Google Gemini.

---

## 🌐 Live Demo

Streamlit Cloud: https://kkd9lh2h9sstchadvjvbc3.streamlit.app/

---

# 📌 Project Overview

The Crypto Intelligence Platform is designed to monitor cryptocurrency markets in real time and provide actionable insights through interactive dashboards and AI-generated analysis.

The project follows a complete analytics workflow:

```text
CoinGecko API
      ↓
 Bronze Layer (Raw JSON)
      ↓
 Silver Layer (Cleaned Data)
      ↓
 SQLite Database
      ↓
 Power BI Dashboard
      ↓
 Streamlit Dashboard
      ↓
 Gemini AI Market Analyst
```

---

# 🎯 Business Objectives

- Monitor live cryptocurrency market activity
- Identify top gainers and losers
- Analyze market capitalization distribution
- Track liquidity and trading volume
- Evaluate overall market health
- Generate AI-powered market reports
- Create executive dashboards for decision-making

---

# 🏗️ Architecture

```text
┌───────────────────┐
│   CoinGecko API   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Bronze Layer      │
│ Raw JSON Storage  │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Silver Layer      │
│ Data Cleaning     │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ SQLite Database   │
└─────────┬─────────┘
          │
 ┌────────┴────────┐
 ▼                 ▼
Power BI      Streamlit
Dashboard     Dashboard
                     │
                     ▼
              Gemini AI
              Market Analyst
```

---

# 📂 Project Structure

```text
crypto-intelligence-platform/
│
├── data/
│   ├── bronze/
│   └── silver/
│
├── database/
│   └── crypto.db
│
├── notebook/
│   └── crypto_analysis.ipynb
│
├── powerbi/
│   └── crypto_dashboard.pbix
│
├── screenshots/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── ai_analyst.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Tech Stack

## Programming

- Python

## Data Engineering

- Requests
- JSON
- SQLite
- Pandas

## Visualization

- Power BI
- Streamlit
- Plotly

## AI

- Google Gemini
- Google AI Studio

## Version Control

- Git
- GitHub

---

# 📊 Power BI Dashboard

The Power BI solution consists of three dashboard pages.

## Dashboard 1 — Market Overview


Features:

- Total Coins
- Total Market Cap
- Total Volume
- Average 24H Change
- Top 10 Gainers
- Top 10 Losers

---

## Dashboard 2 — Market Intelligence

Features:

- BTC Dominance
- Positive Coins
- Negative Coins
- Market Health
- Top Volume Leaders
- Market Cap Distribution
- Treemap Analysis

---

## Dashboard 3 — Advanced Analytics

Features:

- Market Cap vs Price
- Volume vs Market Cap
- Liquidity Analysis
- Price Change Distribution

---

# 🌐 Streamlit Dashboard

Interactive web application providing:

## Overview

![Overview Dashboard](screenshots/streamlit/overview.png)

- KPI Monitoring
- Top Gainers
- Top Losers
- Liquidity Leaders

## Market Intelligence

![Market Intelligence Dashboard](screenshots/streamlit/market_intelligence.png)

- Volume Analysis
- Market Cap Analysis
- Treemap Visualization

## AI Market Analyst

![AI Market Analyst Dashboard](screenshots/streamlit/ai_market_analysis.png)

Powered by Google Gemini.

Generates:

- Market Sentiment
- Key Observations
- Risk Assessment
- Trading Opportunities

---

# 🤖 AI Market Analyst

The platform integrates Google Gemini to automatically generate market reports from live cryptocurrency data.

Example:

```text
Market Sentiment: Bearish

Key Observation:
More coins are declining than advancing.

Risk Assessment:
Current market conditions suggest cautious positioning.

Opportunity:
Strong momentum coins may provide short-term trading opportunities.
```

---

# 🗄️ Database Schema

Table:

```sql
crypto_market
```

Columns:

| Column | Description |
|----------|------------|
| id | Coin ID |
| symbol | Coin Symbol |
| name | Coin Name |
| current_price | Current Price |
| market_cap | Market Capitalization |
| market_cap_rank | Market Rank |
| total_volume | Trading Volume |
| price_change_percentage_24h | 24 Hour Change |
| circulating_supply | Circulating Supply |
| last_updated | API Update Time |
| fetch_time | ETL Load Time |

---

# 🔄 ETL Pipeline

## Extract

Collects live data from CoinGecko API.

Output:

```text
data/bronze/*.json
```

---

## Transform

Performs:

- Column Selection
- Missing Value Handling
- Datetime Conversion
- Data Validation

Output:

```text
data/silver/*.csv
```

---

## Load

Loads cleaned data into SQLite.

Destination:

```text
database/crypto.db
```

---

# 📸 Project Screenshots

## Streamlit Dashboard

Add screenshots:

```text
screenshots/overview.png
screenshots/market_intelligence.png
screenshots/ai_market_analyst.png
```

## Power BI Dashboard

Add screenshots:

```text
screenshots/powerbi_dashboard_1.png
screenshots/powerbi_dashboard_2.png
screenshots/powerbi_dashboard_3.png
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/swapitsneil/crypto-intelligence-platform.git

cd crypto-intelligence-platform
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create:

```text
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get API Key:

https://aistudio.google.com

---

## Run Streamlit App

```bash
streamlit run app.py
```

---

# ☁️ Streamlit Community Cloud Deployment

This project is fully compatible with:

- Python 3.11 ✅
- Python 3.12 ✅

Recommended:

```text
Python 3.11
```

Why?

- Most stable for Streamlit deployments
- Better package compatibility
- Fewer dependency issues

---

# 📈 Key Insights

- Bitcoin dominates overall market capitalization.
- Stablecoins generate significant trading volume.
- Liquidity varies substantially across assets.
- Market health can quickly shift between bullish and bearish conditions.
- AI-generated reports provide instant market summaries.

---

# 🔮 Future Enhancements

- Historical Price Tracking
- Automated ETL Scheduling
- Cryptocurrency Forecasting
- Portfolio Optimization
- Real-Time Alerts
- RAG-based Crypto Research Assistant
- Multi-Agent Crypto Intelligence System

---

# 👨‍💻 Author

**Swapnil Nicolson Dadel**

Aspiring Data Analyst

Skills:

- Python
- SQL
- Power BI
- Streamlit
- Data Engineering
- Machine Learning
- Generative AI

GitHub: https://github.com/swapitsneil


LinkedIn: 

---

# ⭐ If you found this project useful

Please consider starring the repository.

```text
⭐ Star the repo
🍴 Fork the project
📢 Share your feedback
```
