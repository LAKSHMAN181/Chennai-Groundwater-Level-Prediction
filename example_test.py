"""Quick smoke test for the repository environment.

This uses synthetic data only. It does not reproduce the manuscript results.
Run with: python example_test.py
"""

import numpy as np
import pandas as pd
import sklearn
import xgboost
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor


def main():
    # Reproducible synthetic monthly example; no research data are required.
    rng = np.random.default_rng(42)
    n = 48
    dates = pd.date_range("2018-01-01", periods=n, freq="MS")
    rainfall = rng.uniform(0, 250, size=n)
    seasonal = 2.0 * np.sin(2 * np.pi * np.arange(n) / 12)
    noise = rng.normal(0, 0.15, size=n)
    groundwater = 8.0 + seasonal - 0.004 * rainfall + noise

    sample = pd.DataFrame(
        {
            "Time": dates,
            "Rainfall_mm": rainfall,
            "Groundwater_Level_mbgl": groundwater,
        }
    )
    sample["GWL_lag_1"] = sample["Groundwater_Level_mbgl"].shift(1)
    sample["Month"] = sample["Time"].dt.month
    sample = sample.dropna().reset_index(drop=True)

    feature_cols = ["Rainfall_mm", "GWL_lag_1", "Month"]
    split = int(len(sample) * 0.8)
    X_train = sample.loc[: split - 1, feature_cols]
    X_test = sample.loc[split:, feature_cols]
    y_train = sample.loc[: split - 1, "Groundwater_Level_mbgl"]
    y_test = sample.loc[split:, "Groundwater_Level_mbgl"]

    model = XGBRegressor(
        n_estimators=20,
        max_depth=2,
        learning_rate=0.05,
        objective="reg:squarederror",
        random_state=42,
        n_jobs=1,
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    print("Smoke test passed.")
    print(f"pandas: {pd.__version__}")
    print(f"scikit-learn: {sklearn.__version__}")
    print(f"xgboost: {xgboost.__version__}")
    print(f"Synthetic example RMSE: {rmse:.4f}")


if __name__ == "__main__":
    main()
