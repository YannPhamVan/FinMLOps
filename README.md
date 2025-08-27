# FinMLOps – ETF Algo-Trading Pipeline

This repository presents an end-to-end workflow for **systematic trading on PEA-eligible ETFs**.  
It explores the full lifecycle of a financial ML project, from **data collection** to **modeling** and **trading simulation**, with a focus on building reproducible and scalable pipelines.

---

## Problem statement
European investors face restrictions on which ETFs are available through the **PEA account (Plan d’Épargne en Actions)**.  
The project aims to:  
- Identify and track these ETFs  
- Collect and process their historical market data  
- Build baseline predictive models  
- Simulate trading strategies to benchmark performance  

---

## Data sources
- **Yahoo Finance API** (`yfinance`) for historical price data  
- **pandas-datareader** for complementary feeds  
- Custom ETF list stored in [`data/raw/isin_list.csv`](data/raw/isin_list.csv)  

---

## Data processing & EDA
- Consolidation of raw ETF data into a single DataFrame  
- Computation of features such as returns, volatility and technical indicators  
- Export to compressed Parquet format for reproducibility:  
`data/processed/etf_df_combined_2025_08_25.parquet.brotli`

---

## Modeling
Implemented baseline models to predict ETF returns:  
- **Decision Tree**  
- **Random Forest**  

These models establish first benchmarks and highlight areas for improvement (e.g. advanced time-series models, deep learning architectures).  

---

## Trading simulation
A vectorized trading engine was developed to compare:  
- **Buy & hold strategy**  
- **ML-driven allocation strategy**  

This provides a first evaluation of the feasibility of systematic ETF strategies within the PEA framework.  

---

## Automation & MLOps
- Current workflow implemented in the notebook [`notebooks/finmlops.ipynb`](notebooks/finmlops.ipynb)  
- Next steps:  
    - Refactor into modular Python scripts  
    - Orchestrate with a workflow manager (Prefect, Airflow)  
    - Add CI/CD and monitoring  

---

## Repository structure
FinMLOps/
│
├── data/
│ ├── raw/ # ETF list (ISIN)
│ └── processed/ # Cleaned and combined datasets
│
├── notebooks/
│ ├── dataset_generation.ipynb # Data extraction & processing
│ └── finmlops.ipynb # Modeling + trading simulation
│
├── Pipfile
├── Pipfile.lock
└── README.md

---

## Installation
Clone the repository and install dependencies with **pipenv**:

```bash
git clone https://github.com/YannPhamVan/FinMLOps.git
cd FinMLOps

pipenv install
pipenv shell

jupyter notebook
```

---

## Evaluation guide (for reviewers)
The project can be evaluated on the following aspects:
- **Problem definition** → see *Problem statement*
- **Data sources** → see *Data sources*
- **Transformations** → see *Data processing & EDA* and `dataset_generation.ipynb`
- **Modeling** → see *Modeling* and `finmlops.ipynb`
- **Simulation** → see *Trading simulation*
- **Automation** → see *Automation & MLOps*

This ensures clarity on coverage and makes it easy to align with standard peer review grids.

---

## Roadmap
- Integrate **deep learning models** (LSTMs, Temporal CNNs)
- Add **robust backtesting** with transaction costs, drawdowns and risk metrics
- Package notebooks into maintainable Python modules
- Automate pipelines with CI/CD and orchestration tools

---

## Acknowledgments
Special thanks to the open-source ecosystem and communities making financial data and ML tools widely accessible.