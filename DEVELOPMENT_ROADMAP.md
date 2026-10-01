# Development Roadmap

This 15-day timeline outlines the AI-accelerated agile methodology for building the Bayesian Regime Detection Engine.

### Phase 1: Data & Foundations
- **Day 1: Domain Orientation and Environment Setup** 
  - Conda env setup, library installation (PyMC, TensorFlow, PyTorch, hmmlearn, etc.).
- **Day 2: Indian Market Data Ingestion and Exploration** 
  - Ingest OHLC, VIX, macro, flow data. Perform EDA and quality checks.
- **Day 3: Feature Engineering for Regime Classification** 
  - Build point-in-time features, topological (TDA), and graph (GNN) embeddings.

### Phase 2: Core Regime Modelling
- **Day 4: Frequentist HMM Implementation** 
  - 5-state Gaussian HMM baseline, regime labelling, BIC comparisons.
- **Day 5: Bayesian HMM via PyMC** 
  - Dirichlet priors, NUTS sampling, MCMC diagnostics (R-hat, ESS).
- **Day 6: Regime-Switching VAR and Multivariate Dynamics** 
  - Multivariate PyMC/NumPyro model, regime-conditional cross-asset covariances.
- **Day 7: Bayesian Deep Learning** 
  - MC Dropout, Variational BNNs, Deep Ensembles, SHAP explainability.
- **Day 8: Foundation Model Integration** 
  - Integrate Chronos, TimesFM, etc., with Bayesian classification heads.

### Phase 3: Ensembling & Sequential Inference
- **Day 9: Model Ensembling, Stacking, and Selection** 
  - Bayesian Model Averaging, Constrained Stacking, WAIC/LOO comparison.
- **Day 10: Sequential and Online Regime Inference** 
  - Particle Filter, BOCPD, intraday vs batch reconciliation.
- **Day 11: Conformal Prediction and Calibration** 
  - Split-conformal, APS, EnBPI, ECE reliability diagrams.

### Phase 4: Validation & Delivery
- **Day 12: Indian Market Case Study Research and Replication** 
  - Replay 2008, 2013, 2018, 2020, 2024 crises. P&L impact analysis.
- **Day 13: Backtesting, Monte Carlo, and Allocation Overlay** 
  - Regime-conditioned VaR, allocation backtester, Deflated Sharpe.
- **Day 14: Validation, Polish, and Integration** 
  - End-to-end pipeline validation, R vs Python cross-checks, final report drafting.
- **Day 15: Final Submission and Handover** 
  - GitHub repo transfer, video recording, Investment Committee artefact delivery.
