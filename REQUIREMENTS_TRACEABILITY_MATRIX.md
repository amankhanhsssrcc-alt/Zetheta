# Requirements Traceability Matrix

## 1. Project Requirements & Business Logic
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Regime Detection Engine | Build engine classifying Indian equity into 5 discrete states | `src/engine/classifier.py` | Market, Macro, Flow data | Walk-forward cross-validation | Python Codebase | NOT STARTED |
| Point-in-Time Data | Implement lag-aware feature engineering to prevent look-ahead bias | `src/data/feature_store.py` | Release lag days mapping | Alignment test, No future leaks | Python Codebase | NOT STARTED |
| Two-Speed Architecture | Nightly batch refit + intraday online tracking | `src/deployment/serving.py` | Live feeds, Historical db | Online/batch reconciliation gap | Python Codebase | NOT STARTED |
| Explainability (SHAP) | Generate SHAP values for regime probabilities | `src/evaluation/explainability.py` | Model, feature matrix | Feature stability, Local accuracy | Model Card | NOT STARTED |

## 2. Required Deliverables
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Main Report | Write min 40-page report covering theory, methodology, results | `docs/Main_Report.pdf` | Model outputs, metrics | Peer review | Main Report | NOT STARTED |
| Python Codebase | Complete implementation of all pipelines and models | `src/` | All datasets | Unit tests, e2e pipeline run | Python Codebase | NOT STARTED |
| R Codebase | HMM, MSwM, Conformal, Stan implementations | `R/` | All datasets | Cross-language reconciliation | R Codebase | NOT STARTED |
| Backtesting Engine | Regime-overlay allocation backtester, MC VaR engine | `src/backtest/engine.py` | Regime probs, Returns | Deflated Sharpe, PBO | Simulation Engine | NOT STARTED |
| Model Card & Validation | Document inputs, priors, diagnostics, ECE | `docs/Model_Card.pdf` | MCMC traces, Predictions | Diagnostic checks | Validation Pack | NOT STARTED |
| Final Presentation | 18 slides + 10-minute demo video | `docs/Presentation.pdf` | IC artefact, pipeline | Timing, clarity | Final Presentation | NOT STARTED |

## 3. Required Datasets and Data Sources
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Equity OHLC | Nifty 50, Midcap 100, Smallcap 100 | `src/data/ingestion.py` | NSE Indices, Bhavcopy | Missing values, splits adjustment | Python Codebase | NOT STARTED |
| Market & Flow Features | India VIX, USD/INR, 10Y Gilt, AAA spread, FII/DII, SIPs | `src/data/ingestion.py` | RBI, AMFI, Yahoo Finance | Alignment to NSE calendar | Python Codebase | NOT STARTED |

## 4. Required Features
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Technical & Volatility | Returns (1d-63d), Trend (MA50/200), Volatility (21d, 63d), VIX | `src/features/technical.py` | OHLC, VIX | Stationarity, PSI | Python Codebase | NOT STARTED |
| Breadth & Flow | Advance/Decline, Pct above 50DMA, FII/DII flow divergence | `src/features/flow.py` | NSE Bhavcopy, FII/DII | Leakage checks | Python Codebase | NOT STARTED |
| Macro Indicators | Repo rate proxy, inflation, INR change, credit spread | `src/features/macro.py` | RBI DBIE, Gilt yields | Lag adjustment | Python Codebase | NOT STARTED |
| Topological (TDA) | Persistent homology on rolling correlation matrices | `src/features/topology.py` | Cross-asset returns | Persistence landscapes | Python Codebase | NOT STARTED |
| Graph (SectorGCN) | Temporal GNN for sector relationships | `src/features/graph.py` | Sector returns | GCN embedding quality | Python Codebase | NOT STARTED |

## 5. Required Models
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Frequentist HMM | 5-state Gaussian HMM using `hmmlearn` | `src/models/frequentist_hmm/` | Nifty returns | Log-likelihood, BIC | Python Codebase | BLOCKED (Missing MSVC) |
| Bayesian HMM | PyMC implementation with Dirichlet priors | `src/models/bayesian_hmm/` | Nifty returns | R-hat, ESS, divergences | Python Codebase | BLOCKED (Missing MSVC) |
| Regime-Switching VAR | statsmodels baseline + PyMC multivariate RS-VAR | `src/models/rs_var/` | Returns, vol, breadth, flow | Impulse response sanity | Python Codebase | BLOCKED (Missing MSVC) |
| Bayesian Deep Learning | MC Dropout, Variational BNN, Deep Ensembles | `src/models/bdl/` | Full feature matrix | CV, Epistemic/Aleatoric split | Python Codebase | BLOCKED (Missing HMM Labels) |
| Foundation Models | Chronos embedding + TimesFM/Lag-Llama/Moirai with Bayesian head | `src/models/foundation_models/` | Full feature matrix | Attention weights, clustering | Python Codebase | VALIDATED |
| Particle Filter | Sequential Monte Carlo for online state estimation | `src/sequential/particle_filter.py`| Daily online observations| Effective Sample Size | Python Codebase | COMPLETE |
| BOCPD | Bayesian Online Changepoint Detection | `src/sequential/bocpd.py` | Sequential features | False-positive rate tuning | Python Codebase | COMPLETE |
| Bayesian Model Averaging | Weighting models by marginal evidence | `src/ensemble/bayesian_model_averaging.py` | Model predictive lik. | WAIC / PSIS-LOO | Python Codebase | PARTIAL |
| Constrained Stacking | Time-aware meta-learner (simplex weights) | `src/ensemble/constrained_stacking.py` | Out-of-fold probs | Brier, RPS against members | Python Codebase | PARTIAL |
| Conformal Prediction | Split-conformal, APS, CQR, EnBPI/ACI | `src/conformal/integration.py`| Model probs, labels | Empirical coverage tracking | Python Codebase | COMPLETE |
| Monte Carlo Simulation | Regime-conditioned path simulation | `src/simulation/mc_engine.py` | Regime probs, covariance | VaR distribution sanity | Simulation Engine | NOT STARTED |

## 6. Required Backtesting and Validation
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Purged & Embargoed CV | Custom TimeSeriesSplit preventing overlap leakage | `src/evaluation/cv.py` | Time series index | Purge overlap visualization | Simulation Engine | NOT STARTED |
| Walk-Forward Eval | Expanding and rolling window evaluation | `src/evaluation/walk_forward.py`| Full feature matrix | Out-of-sample metrics | Simulation Engine | NOT STARTED |
| Proper Scoring Rules | RPS, Brier Score (with Murphy decomp), Log Loss, CRPS | `src/evaluation/metrics.py` | Probs, True labels | Score vs Naive benchmark | Model Card | NOT STARTED |
| Deflated Sharpe & PBO | Discount observed Sharpe for multiple testing | `src/evaluation/pbo.py` | Strategy returns | Skew, kurtosis checks | Main Report | NOT STARTED |
| Case Study Validation | Replay 2020 COVID, 2018 IL&FS, 2013 Taper, 2024 Election | `notebooks/Case_Studies.ipynb`| Crisis episode data | Scenario performance | Main Report | NOT STARTED |

## 7. Required Python Implementation
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Complete Python Stack | Integrate all required libraries (PyMC, TF, PyTorch, hmmlearn, etc.) | `requirements.txt` | N/A | Environment setup script | Python Codebase | NOT STARTED |

## 8. Required R Implementation
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| R Codebase | Implement depmixS4, MSwM, bcp | `R/models.R` | Processed data (CSV) | Match Python outputs | R Codebase | NOT STARTED |

## 9. Required Reports and Documentation
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Documentation | Main report, Model card, IC artefact generator | `docs/` | Results, metrics | Formatting checks | All Docs | NOT STARTED |

## 10. Required Presentation and Demo
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Final Presentation | 18 slides & 10-minute video | `docs/Presentation/` | System outputs | Time constraint check | Final Presentation| NOT STARTED |

## 11. Submission Requirements
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Formatting & Access | Zetheta template, PDF/editable formats, Repo transfer | `docs/` | N/A | Permissions check | Submission | NOT STARTED |

## 12. AI-Use and Validation Requirements
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Strict Validation | Test AI code on real data, check MCMC diags, cross-check Py/R | `tests/` | Real Indian data | CI/CD pipeline | Python Codebase | NOT STARTED |

## 13. Phase 12 - Python/R Numerical Reconciliation
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Python/R numerical reconciliation | Cross-validate implementations | `artifacts/reconciliation/` | Reconciliation dataset | Tolerance checks | Docs | FAIL (Missing R) |
| Cross-language financial metrics | Ensure exact match of VaR/Returns | `artifacts/reconciliation/` | Validation data | Absolute tolerance | Docs | FAIL |
| Reproducibility | Document environment, versions | `docs/` | Config | Execution check | Docs | PASS |

## 14. Phase 13 - Final Report, Model Cards & Technical Documentation
| PDF Requirement | Implementation Needed | Proposed File/Module | Data Required | Validation/Test | Final Deliverable | Status |
|---|---|---|---|---|---|---|
| Main Report | 40-page PDF report | `docs/Main_Report.md` | Artifacts | Audit | Report | PARTIAL (Markdown generated) |
| Model Cards | Technical specs for models | `docs/model_cards/` | Outputs | Review | MD Files | COMPLETE |
| Validation Pack | Package phase 11 artifacts | `validation_pack/` | Phase 11 artifacts | Review | Directory | COMPLETE |
| Result Provenance | Traceability from report to code | `docs/result_provenance_matrix.csv` | Artifacts | Audit | CSV | COMPLETE |


