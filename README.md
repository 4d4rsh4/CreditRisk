# Financial Credit Risk & Default Prediction
> **An end-to-end Machine Learning solution for high-dimensional credit scoring.**

## Project Overview
This project addresses the "Class Imbalance" challenge in Fintech by predicting loan default probability. Using the Home Credit dataset, I synthesized data from multiple relational tables (Applicants, Bureau, and Previous Applications) to build a robust risk-assessment engine.

# Tech Stack
- **Database:** SQLite (Relational aggregation of 3.5M+ records)
- **Language:** Python 3.x
- **Algorithm:** XGBoost (Gradient Boosted Trees)
- **Techniques:** Feature Engineering, Target Encoding, Cost-Sensitive Learning 
- **BI Visualization:** Tableau
  
# Data Engineering
I performed complex SQL aggregations to flatten a one-to-many relational schema into a single applicant-level feature set:
- **Bureau Integration:** Engineered features for "Loan Velocity" (active loans) and "Credit Utilization."
- **Internal History:** Aggregated 1.6M previous application records to identify historical rejection patterns.
- **Data Pipeline:** Developed a Python ETL process to handle multi-table joins and data type standardization.

# Model Performance
Given the extreme class imbalance (8% delinquency rate), I optimized the model for **Recall** to minimize financial loss.
- **Accuracy:** 71%
- **Recall (Class 1):** 0.65
- **Primary Drivers:** External Credit Scores, Educational Attainment, and Active Loan Count.

## 📊 Business Intelligence
[INSERT SCREENSHOT OF YOUR FEATURE IMPORTANCE CHART HERE]
[INSERT SCREENSHOT OF YOUR RISK DASHBOARD HERE]

---
*Developed by Adarsha Rai*
