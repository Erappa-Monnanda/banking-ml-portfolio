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

### 5. Credit Card Fraud Detection — Capstone Project
End-to-end ML pipeline on real Kaggle dataset (284,807 transactions).

Features:
- Exploratory Data Analysis with 4 visualization sets
- Class imbalance handling: baseline vs class weights vs SMOTE
- Model comparison: Logistic Regression vs Random Forest (6 models)
- Threshold tuning with Precision-Recall curves
- PR-AUC evaluation (Random Forest: 0.861)
- Production model persistence with deployment notes

Results: Random Forest achieved Precision=0.941, Recall=0.816, 
F1=0.874, PR-AUC=0.861 on 56,962 held-out test transactions.

Files: fraud_analysis_capstone.ipynb, fraud_model_final.pkl

## Skills
- Python — functions, OOP, list comprehensions, error handling
- Pandas & NumPy — data loading, cleaning, feature engineering
- Scikit-learn — Logistic Regression, Decision Trees, Random Forest
- Imbalanced-learn — SMOTE for class imbalance
- Matplotlib & Seaborn — EDA visualizations, PR curves
- ML Pipeline — preprocessing, train/test split, cross-validation
- Model Evaluation — Precision, Recall, F1, PR-AUC, threshold tuning
- Jupyter Notebook — professional notebook structure
- GitHub — version control, portfolio management
- Domain: Banking, Fraud Detection, Risk Analytics

## About
Finance professional transitioning into AI/ML engineering.
5+ years of experience in banking operations, trade desk, 
and governance & oversight roles in financial services, 
combined with hands-on ML engineering skills.

Target roles: AI/ML Engineer, Data Scientist, 
GenAI Developer in Financial Services.
