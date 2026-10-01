# Project Architecture

## 1. High-Level System Overview
The Bayesian Regime Detection Engine is a production-grade, two-speed machine learning system designed for a Tier 1 Indian Asset Management Company. It consumes point-in-time market, macro, flow, and topological data to emit calibrated probabilities over five discrete Indian equity regimes (Risk-On, Risk-Off, Transitional, Late-Cycle, Post-Shock). 

## 2. Core Components

### 2.1 Data & Feature Store
- **Ingestion**: Fetches NSE OHLC, VIX, Gilt yields, USD/INR, and FII/DII flow data.
- **Feature Engineering**: Calculates technicals, volatility surfaces, breadth, macroeconomic proxies, and topological features (Persistent Homology via `giotto-tda`, Sector Graph Embeddings via `torch_geometric`).
- **Point-in-Time Discipline**: Implements strict lag rules (`enforce_pit`) and NSE calendar alignment to prevent look-ahead and survivorship bias.

### 2.2 Model Stack
- **Frequentist Baselines**: Gaussian HMMs (`hmmlearn`) and single-feature Markov-switching regression (`statsmodels`).
- **Bayesian HMM**: PyMC implementation yielding full posterior distributions over transition probabilities and regime means/volatilities.
- **Regime-Switching VAR (RS-VAR)**: Multivariate Bayesian engine capturing cross-asset covariance shifts and regime-conditional impulse responses.
- **Bayesian Deep Learning (BDL)**: MC Dropout, Variational Inference (VI), and Deep Ensembles to capture non-linear relationships with calibrated epistemic and aleatoric uncertainty.
- **Foundation Models**: Utilizing `Chronos`, `TimesFM`, `Lag-Llama`, and `Moirai` for zero-shot embedding extraction, fed into a Bayesian classification head.

### 2.3 Sequential Inference & Online Tracking
- **Two-Speed Design**: A computationally heavy nightly batch refit sets the reference posterior.
- **Intraday Tracking**: A Bootstrap Particle Filter and Bayesian Online Changepoint Detection (BOCPD) track regime evolution and sudden breaks between batch runs.
- **Health Checks**: Monitors online/batch reconciliation gaps and Population Stability Index (PSI) for feature drift.

### 2.4 Ensembling & Calibration
- **Model Ensembling**: Combines base models using Bayesian Model Averaging (BMA) and Time-Aware Constrained Stacking.
- **Conformal Prediction**: Wraps point probabilities into prediction sets with guaranteed finite-sample coverage (e.g., Adaptive Prediction Sets, EnBPI for shift-robustness).

### 2.5 Simulation & Allocation Overlay
- **Regime-Conditioned Monte Carlo**: Generates forward paths conditioned on current regime probabilities for VaR and CVaR estimation.
- **Black-Litterman Allocation**: Maps regime conviction into portfolio tilts, enforcing constraints like SEBI categories, no-trade turnover bands, and hysteresis limits.

### 2.6 Evaluation & Backtesting
- **Strict Cross-Validation**: Uses purged and embargoed folds, and walk-forward evaluation.
- **Proper Scoring Rules**: Evaluated strictly on Ranked Probability Score (RPS), Brier Score, and Log Loss against persistence baselines.
- **Deflated Sharpe & PBO**: Corrects backtest Information Ratio for the multiple-testing problem and estimates Probability of Backtest Overfitting.
