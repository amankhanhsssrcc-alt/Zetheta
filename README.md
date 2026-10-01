# Bayesian Regime Detection Engine

## Overview
This repository contains a production-grade Bayesian Regime Detection Engine tailored for the Indian equity market. Developed as part of the Zetheta Algorithms quantitative assessment, the engine classifies market conditions into discrete states (Risk-On, Risk-Off, Transitional, Late-Cycle, Post-Shock) using a rigorous, probabilistic, and audit-defensible methodology.

## Key Capabilities
- **Multivariate Regime Detection**: Integrates Hidden Markov Models (Frequentist & Bayesian), Regime-Switching VAR, Bayesian Neural Networks, and Time-Series Foundation Models.
- **Calibrated Uncertainty**: Utilizes Conformal Prediction to provide finite-sample valid prediction sets, shifting focus from point estimates to calibrated probability distributions.
- **Two-Speed Inference**: Combines nightly batch MCMC/VI refits with intraday tracking via Particle Filtering and Bayesian Online Changepoint Detection (BOCPD).
- **Regime-Aware Allocation**: Bridges probabilistic regime forecasts to portfolio actions via Black-Litterman tilts and regime-conditioned Monte Carlo VaR estimation.
- **Robust Evaluation**: Strictly assessed using proper scoring rules (RPS, Brier), purged/embargoed cross-validation, Deflated Sharpe Ratio, and PBO to prevent backtest overfitting.

## Repository Structure
- `/src/` - Python implementation of the core engine, models, and backtesting suite.
- `/R/` - R implementations (depmixS4, MSwM, bcp) for cross-language validation.
- `/notebooks/` - Exploratory analysis, feature engineering, and case study replay scenarios.
- `/docs/` - Project documentation, Model Cards, Main Report, and presentation materials.

## Getting Started
1. Clone the repository.
2. Setup the environment using `conda create -n regime python=3.10` and install dependencies from `requirements.txt` (to be created).
3. Follow the sequence defined in `DEVELOPMENT_ROADMAP.md` to run the ingestion, training, and evaluation pipelines.

## Project Deliverables
1. Main Project Report (40+ pages)
2. Python Codebase
3. R Codebase
4. Backtesting and Simulation Engine
5. Model Card, Calibration and Validation Pack
6. Final Presentation and 10-minute demo video
