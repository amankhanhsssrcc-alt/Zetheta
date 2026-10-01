import os
import mlflow
import numpy as np
from src.utils.logger import logger
from src.data.ingestion import DataIngestor
from src.data.cleaning import clean_data
from src.data.quality import DataQualityChecker
from src.data.point_in_time import enforce_pit
from src.features.engineering import engineer_regime_features
from config.settings import PROCESSED_DATA_DIR

def run_pipeline():
    logger.info("Starting Phase 1 Data Pipeline (Strict Compliance)...")
    
    mlflow.set_experiment("Regime_Engine_Phase1")
    
    with mlflow.start_run():
        # 1. Ingestion
        ingestor = DataIngestor()
        raw_df = ingestor.ingest_all()
        
        # 2. Quality Check (Raw)
        logger.info("--- Quality Check: Raw Data ---")
        DataQualityChecker.run_all_checks(raw_df)
        
        # 3. Clean
        clean_df = clean_data(raw_df)
        
        # 4. Quality Check (Cleaned)
        logger.info("--- Quality Check: Cleaned Data ---")
        DataQualityChecker.run_all_checks(clean_df)
        
        # 5. Feature Engineering (including TDA & GNN)
        features_df = engineer_regime_features(clean_df)
        
        # 6. Enforce PIT
        pit_features = enforce_pit(features_df)
        
        # Output saving
        os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
        out_path = os.path.join(PROCESSED_DATA_DIR, "pit_features.csv")
        pit_features.to_csv(out_path)
        
        logger.info("=========================================")
        logger.info("PIPELINE EXECUTION SUMMARY")
        logger.info("=========================================")
        logger.info(f"Output saved to: {out_path}")
        logger.info(f"Date Range: {pit_features.index.min()} to {pit_features.index.max()}")
        logger.info(f"Observations: {len(pit_features)}")
        logger.info(f"Features Generated: {len(pit_features.columns)}")
        
        # Count NaNs in features
        nan_counts = pit_features.isna().sum()
        logger.info(f"Missing Values in Output:\n{nan_counts[nan_counts > 0]}")
        
        mlflow.log_param("num_features", len(pit_features.columns))
        mlflow.log_param("num_observations", len(pit_features))
        mlflow.log_artifact(out_path)

if __name__ == "__main__":
    run_pipeline()
