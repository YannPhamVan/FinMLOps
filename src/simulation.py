import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def backtest_strategy(df: pd.DataFrame, initial_capital: float = 10000) -> float:
    """Naive backtest: invest when signal == 1, cash otherwise."""
    logging.info("Running backtest")

    capital = initial_capital
    position = 0

    for i in range(1, len(df)):
        if df["signal"].iloc[i-1] == 1:  # buy signal
            position = capital / df["Close"].iloc[i]
            capital = 0
        elif df["signal"].iloc[i-1] == 0 and position > 0:  # sell signal
            capital = position * df["Close"].iloc[i]
            position = 0

    # Final value
    if position > 0:
        capital = position * df["Close"].iloc[-1]

    logging.info(f"Final capital: {capital:.2f}")
    return capital
