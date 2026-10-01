import numpy as np
import pandas as pd
import time
from src.models.foundation_models import ChronosModel, TimesFMModel, FoundationModelPipeline

def test_chronos():
    print("Testing Chronos...")
    # Generate dummy data
    dates = pd.date_range(start="2020-01-01", periods=300, freq="D")
    values = np.sin(np.linspace(0, 20, 300)) + np.random.normal(0, 0.1, 300)
    df = pd.DataFrame({"Date": dates, "Nifty": values})

    model = ChronosModel(model_version="amazon/chronos-t5-tiny")
    
    pipeline = FoundationModelPipeline(model, window_length=252, forecast_horizon=21, step_size=20)
    results = pipeline.run(df, "Nifty", "Date")
    print(results.head())
    print("Chronos test passed.")

def test_timesfm():
    print("Testing TimesFM...")
    dates = pd.date_range(start="2020-01-01", periods=300, freq="D")
    values = np.sin(np.linspace(0, 20, 300)) + np.random.normal(0, 0.1, 300)
    df = pd.DataFrame({"Date": dates, "Nifty": values})

    model = TimesFMModel()
    pipeline = FoundationModelPipeline(model, window_length=252, forecast_horizon=21, step_size=20)
    results = pipeline.run(df, "Nifty", "Date")
    print(results.head())
    print("TimesFM test passed.")

if __name__ == "__main__":
    test_chronos()
    try:
        test_timesfm()
    except Exception as e:
        print(f"TimesFM test failed (maybe missing dependencies): {e}")
