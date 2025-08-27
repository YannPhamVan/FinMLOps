import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

PROCESSED_DIR = Path("data/processed")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: dropna, remove duplicates."""
    logging.info("Cleaning data")
    df = df.dropna().drop_duplicates()
    return df

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add engineered features like moving averages, returns, volatility."""
    logging.info("Adding features")
    df["daily_return"] = df["Close"].pct_change()
    df["volatility_20d"] = df["daily_return"].rolling(20).std()
    df["ma_50"] = df["Close"].rolling(50).mean()
    return df

def save_processed(df: pd.DataFrame, filename: str = "processed_data.parquet") -> None:
    """Save processed dataframe into data/processed/"""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    filepath = PROCESSED_DIR / filename
    df.to_parquet(filepath, compression="brotli")
    logging.info(f"Processed data saved to {filepath}")
