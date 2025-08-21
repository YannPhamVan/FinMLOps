import yfinance as yf
import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")

def fetch_etf_data(tickers, start_date, end_date):
    """
    Télécharge les données historiques OHLCV pour une liste d’ETFs.
    """
    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker', auto_adjust=True)
    return data

def fetch_index_data(index_tickers, start_date, end_date):
    """
    Télécharge les données historiques pour des indices de référence.
    """
    data = yf.download(index_tickers, start=start_date, end=end_date, group_by='ticker', auto_adjust=True)
    return data

def save_raw_data(df, filename):
    """
    Sauvegarde les données brutes en CSV.
    """
    RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
    filepath = RAW_DATA_PATH / f"{filename}.csv"
    df.to_csv(filepath)
    print(f"Données sauvegardées: {filepath}")

if __name__ == "__main__":
    # Exemple d’utilisation
    etfs = ["EWQ", "EXSA.DE"]   # Exemple : ETF France et ETF MSCI World éligibles PEA
    indices = ["^GSPC", "^GDAXI"]

    df_etfs = fetch_etf_data(etfs, "2020-01-01", "2024-12-31")
    df_indices = fetch_index_data(indices, "2020-01-01", "2024-12-31")

    save_raw_data(df_etfs, "etfs_data")
    save_raw_data(df_indices, "indices_data")
