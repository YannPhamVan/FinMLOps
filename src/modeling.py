import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

logging.basicConfig(level=logging.INFO)

def train_model(df: pd.DataFrame, target_col: str = "signal"):
    """Train a simple classifier to predict buy/sell signal."""
    logging.info("Training model")

    X = df.drop(columns=[target_col]).select_dtypes(include=["float64", "int64"]).fillna(0)
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    logging.info("\n" + classification_report(y_test, preds))

    return model
