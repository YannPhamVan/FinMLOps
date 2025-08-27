import yfinance as yf
import pandas as pd
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

RAW_DATA_PATH = Path("data/raw")

def fetch_data(tickers, start_date, end_date, label="data"):
    """
    Download historical OHLCV data for a list of tickers (ETFs, indices, stocks).
    
    Args:
        tickers (list[str]): List of Yahoo Finance tickers
        start_date (str): Start date (YYYY-MM-DD)
        end_date (str): End date (YYYY-MM-DD)
        label (str): Tag to distinguish datasets (ETFs, Indices, Stocks, etc.)
    
    Returns:
        pd.DataFrame: Downloaded data
    """
    logging.info(f"Fetching data for {label}: {tickers}")
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        group_by="ticker",
        auto_adjust=True,
        progress=False,
    )
    logging.info(f"Data retrieved: {data.shape} rows")
    return data

def save_raw_data(df: pd.DataFrame, filename: str):
    """
    Save raw data as CSV inside data/raw/.
    
    Args:
        df (pd.DataFrame): Data to save
        filename (str): File name (without extension)
    """
    RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
    filepath = RAW_DATA_PATH / f"{filename}.csv"
    df.to_csv(filepath)
    logging.info(f"Raw data saved: {filepath}")

if __name__ == "__main__":
    # Example usage for local testing
    etfs = ["EWQ", "EXSA.DE"]       # Example: ETF France and MSCI World (PEA eligible)
    indices = ["^GSPC", "^GDAXI"]   # Example: S&P500 and DAX

    df_etfs = fetch_data(etfs, "2020-01-01", "2024-12-31", label="ETFs")
    save_raw_data(df_etfs, "etfs_data")

    df_indices = fetch_data(indices, "2020-01-01", "2024-12-31", label="Indices")
    save_raw_data(df_indices, "indices_data")
