# Blinkit Sales Analysis – Retail Inventory & Sales

Analyzing product category efficiency and profitability to support strategic purchasing, pricing, campaign planning, and inventory decisions using **SQL, Python, and Power BI**.

---

## 📌 Overview

This project evaluates Blinkit’s sales performance and retail inventory dynamics to generate actionable business insights.

A complete data pipeline was built using:
- **SQL** for ETL and data modeling
- **Python** for analysis and statistical validation
- **Power BI** for interactive dashboards and reporting

---

## 🧩 Business Problem

Effective inventory and sales management are critical in the retail sector. This project focuses on:
- Identifying high-performing and underperforming product categories & brands
- Determining category-wise contribution to sales and profits
- Analyzing stock received vs damaged stock ratio
- Statistically validating profitability differences
- Understanding customer segments

---

## 📂 Dataset

- Multiple CSV files located in the `/data/` folder:
  - Sales
  - Delivery
  - Stock
  - Damaged Stock
- Summary table created from ingested data and used for analysis

---

## 🛠️ Tools & Technologies

- SQL (CTEs, Joins, Filtering)
- Python (Pandas, Matplotlib, Seaborn, SciPy)
- Power BI (Interactive Dashboards)
- GitHub

---

## 📁 Project Structure

```
vendor-performance-analysis/
│
├── README.md
├── .gitignore
├── requirements.txt
├── Blinkit_sales_Report.pdf
│
├── notebooks/
│   ├── exploratory_data_analysis.ipynb
│   └── blinkit_sales_analysis.ipynb
│
├── scripts/
│   ├── ingestion_db.py
│   └── get_ingestion_db.py
│
├── dashboard/
│   └── blinkit_sales_dashboard.pbix
```

---

## 🧹 Data Cleaning & Preparation

- Created summary tables for brands needing promotion and price adjustment
- Converted data types and handled outliers
- Merged lookup and transactional tables

---

## 📊 Exploratory Data Analysis (EDA)

### Delivery Status
- Delivered on time
- Significantly delayed

### Correlation Analysis
- Weak negative correlation between Profit Margin & Price (-0.06)
- Strong correlation between Stock Received & Damaged Stock

---

## 🔍 Research Questions & Key Findings

- **Brands for Promotion**: 23 brands that give 8% to 10% profitMargin
- **Top Categories**: Top 5 categories contribute 56.83% of total sales
- **Order Size Impact**: Medium-sized orders provide better cost savings
- **Category Profitability**:
  - Highest mean margin: 11.13%
  - Lowest mean margin: 7.19%

---

## 📈 Dashboard

Power BI dashboard includes:
- Category-wise sales and margins
- Category turnover
- Bulk purchase savings
- Campaign performance
- Customer segmentation

---

## ▶️ How to Run This Project

1. Clone the repository:
```
git clone https://github.com/yourusername/Blinkit-Sales-analysis.git
```

2. Ingest data:
```
python scripts/ingestion_db.py
```

3. Create summary table:
```
python scripts/get_ingestion_db.py
```

4. Run notebooks:
- exploratory_data_analysis.ipynb
- blinkit_sales_analysis.ipynb

5. Open Power BI dashboard:
- blinkit_sales_dashboard.pbix

---

## ✅ Final Recommendations

- Optimize bulk order strategies
- Reprice slow-moving, high-margin brands & categories
- Improve marketing for underperforming products
- Strengthen market campaigns

---

## 👤 Author & Contact

**Mohan Saini**  
Data Analyst  

📧 Email: mohan1486saini@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/mohan-saini-69727828b
