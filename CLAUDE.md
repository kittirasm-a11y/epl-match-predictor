# EPL Match Outcome Predictor
Portfolio project. Predict home win / draw / away win for Premier League matches.
Stack: pandas, scikit-learn, xgboost, matplotlib. Python 3.11+. Windows, PowerShell.

## Structure
- data/raw/ – original CSVs from football-data.co.uk (not committed)
- data/processed/ – cleaned and feature-engineered data
- src/ – reusable scripts
- notebooks/ – exploration and charts
- reports/figures/ – saved plots for the README

## Rules
- All features must use only data from BEFORE the match (shift rolling windows).
- Use time-based train/test splits, never random shuffling.
- Explain non-obvious code with brief comments; I need to understand every line.
- I'm learning: explain your reasoning before making changes.