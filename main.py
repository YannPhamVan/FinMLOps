import logging
from src import data_ingestion

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_pipeline():
    """
    Main orchestration function for the ML pipeline.
    Steps:
      1. Fetch raw data (ETFs and indices)
      2. Save raw data
      3. (Next steps: feature engineering, modeling, simulation)
    """
    logging.info("=== Starting pipeline ===")

    # Example tickers
    etfs = ["EWQ", "EXSA.DE"]       # Example: ETF France and MSCI World
    indices = ["^GSPC", "^GDAXI"]   # Example: S&P500 and DAX

    # Step 1 - Data ingestion
    df_etfs = data_ingestion.fetch_data(etfs, "2020-01-01", "2024-12-31", label="ETFs")
    data_ingestion.save_raw_data(df_etfs, "etfs_data")

    df_indices = data_ingestion.fetch_data(indices, "2020-01-01", "2024-12-31", label="Indices")
    data_ingestion.save_raw_data(df_indices, "indices_data")

    logging.info("=== Pipeline finished successfully ===")

if __name__ == "__main__":
    run_pipeline()
