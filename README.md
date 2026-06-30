# Banking ML Portfolio

Python and ML projects combining banking domain expertise 
with data science and AI engineering skills.

## Projects

### 1. Transaction Analyzer
Production-style Python module analyzing banking transactions.

Features:
- Credit and debit segregation
- High value transaction flagging
- Single pass loop optimization
- Above average transaction detection
- Summary report generation

File: transaction_analyzer.py

### 2. Fraud Detector
Pandas-based fraud detection module for banking transactions.

Features:
- High value transaction flagging (amount > 600)
- Suspicious transaction detection (amount > 5000)
- Transaction aggregation by country
- Average amount analysis by transaction type
- Risk-sorted transaction reporting

File: fraud_detector.py

### 3. Fraud Analysis Notebook
End-to-end data preparation and fraud analysis using Pandas and NumPy.

Features:
- CSV data loading and exploration
- Missing value detection and treatment
  - Mean imputation for numerical columns
  - Default value filling for categorical columns
  - Row dropping for missing key identifiers
- Risk score classification (high/medium/low)
- Country-level transaction analysis
- Cleaned data export to CSV

File: fraud_analysis.ipynb

### 4. Fraud Detection ML Pipeline
End-to-end ML model comparison for fraud detection.

Features:
- Synthetic banking transaction data generation
- Feature engineering (z-scores, risk flags, domain-driven features)
- Model comparison: Logistic Regression, Decision Tree, Random Forest
- Class imbalance handling (class weights)
- Feature importance analysis
- 5-fold cross validation
- Model persistence with joblib

File: fraud_model.ipynb

## Skills
- Python
- Pandas — data loading, cleaning, aggregation
- NumPy — conditional column creation
- Fraud Detection Logic
- Data Preparation for ML
- Jupyter Notebook
- ML (in progress)

## About
Finance professional transitioning into AI/ML engineering.
5+ years of banking and risk management experience at Wells Fargo
combined with hands-on ML engineering skills.

Target roles: AI/ML Engineer, Data Scientist, 
GenAI Developer in Financial Services.
