# Retail Transaction Insights 📊

## Overview
Analyzes retail transaction data to uncover insights on customer behavior, promotions, and seasonal trends through an interactive menu-driven interface.

## Installation

```bash
cd c:\Users\310275285\retail-transaction-insights
pip install -r requirements.txt
```

## How to Run

```bash
python main.py
```

## Features

1. **Data Preparation** - CSV loading, date parsing, feature engineering
2. **Basic Exploration** - Transactions, customers, top products, cities
3. **Customer Behavior** - Spending by category, payment preferences
4. **Promotion Impact** - Discount effectiveness, promotion analysis
5. **Seasonality Trends** - Revenue by season, average spending
6. **Visualizations** - Generate all plots (bar, pie, line, heatmap)
7. **Run All** - Execute all analyses at once

## Project Structure

```
retail-transaction-insights/
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── analysis.py
│   └── visualization.py
├── data/
│   └── Retail_Transactions_Dataset.csv
├── outputs/plots/
├── main.py
└── README.md
```

## Output Files

Visualizations saved to `outputs/plots/`:
- `city_transactions.png` - Transactions per city
- `payment_distribution.png` - Payment method distribution
- `monthly_revenue.png` - Monthly revenue trends
- `heatmap.png` - Revenue by season & customer category

## Technology Stack

- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn