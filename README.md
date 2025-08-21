# FinMLOps: Analysis and Portfolio Management Tool for PEA-Eligible ETFs

> Lightweight MLOps framework for PEA-eligible ETF analysis and portfolio management

---

## What is a PEA?
The **Plan d'Épargne en Actions (PEA)** is a French tax-advantaged investment account.  
It allows individuals to invest in European stocks and ETFs while benefiting from tax exemptions after a holding period (typically 5 years).  
To qualify, securities must be **PEA-eligible**, meaning they comply with EU rules.  
This project focuses specifically on **PEA-eligible ETFs**, which provide diversified exposure within the PEA framework.

---

## 1. Problem Description
The objective is to deliver a simple but functional system for analysis and portfolio management of PEA-eligible ETFs, balancing interpretability and performance.

## 2. Data
The dataset includes daily price and volume data of PEA-eligible ETFs, complemented with derived indicators such as moving averages, volatility measures, and momentum factors.

## 3. Data Preparation
- Data cleaning and alignment of time series  
- Feature engineering with technical indicators  
- Handling missing values and normalization  

## 4. Modeling
To keep the project interpretable and lightweight, a Decision Tree Classifier (`scikit-learn`) is used.  
The model predicts bullish or bearish signals for selected ETFs based on engineered features.

## 5. Backtesting
A simple trading strategy is simulated to evaluate model-driven decisions, including performance metrics such as cumulative returns, Sharpe ratio, and maximum drawdown.

## 6. Evaluation
The model and strategy are evaluated based on predictive accuracy and portfolio performance metrics, with emphasis on robustness and generalizability.

## 7. Deployment
The project includes a reproducible pipeline with clear steps for data ingestion, feature engineering, model training, and evaluation.  
Results are stored in a structured format to facilitate analysis and visualization.

## 8. Contributor
Independent Data Scientist specializing in anomaly detection, scoring, and MLOps for finance and industry.  
