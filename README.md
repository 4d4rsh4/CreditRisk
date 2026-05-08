# Financial Credit Risk & Default Prediction

# Project Overview
This project addresses the "Class Imbalance" challenge in Fintech by predicting loan default probability. Using the Home Credit dataset, I synthesized data from multiple relational tables (Applicants, Bureau, and Previous Applications) to build a robust risk-assessment engine.

# Tech Stack
- Dataset: Kaggle, Home Credit Default Risk 
- Database: SQLite 
- Language: Python
- Libraries: Pandas, Scikit-Learn, SQLAlchemy, Matplotlib
- Visualization: Tableau
  
# Data Engineering
I performed complex SQL aggregations to flatten a one-to-many relational schema into a single applicant-level feature set:
- Bureau Data: Calculated No. of active loans and active debts for each applicant.
- Bank History: Aggregated 1.6M previous application records to identify historical rejection records for each applicant.
- Data Pipeline: Developed a Python ETL process to handle multi-table joins and data type standardization.

# Model Performance
Given the extreme class imbalance (8% delinquency rate), I optimized the model for **Recall** to minimize financial loss.
- Accuracy: 71%
- Recall (Class 1): 0.65
- Primary Drivers: External Credit Scores, Educational Attainment, and Active Loan Count.
  
# Tableau Visualization

<img width="1184" height="881" alt="image" src="https://github.com/user-attachments/assets/427062c4-c29b-4da6-8fd8-c27525b407b2" />


<img width="1186" height="883" alt="image" src="https://github.com/user-attachments/assets/c8e3995a-ee88-4c8a-b7ab-fdf76f4ffec2" />
