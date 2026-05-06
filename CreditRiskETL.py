import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('sqlite:///CreditRisk.db')


df = pd.read_csv('data/application_train.csv')
df.to_sql('applicants', con = engine, if_exists = 'replace', index = False)
print(df.shape)
del df

df = pd.read_csv('data/previous_application.csv')
df.to_sql('previous', con = engine, if_exists = 'replace', index = False)
print(df.shape)
del df

df = pd.read_csv('data/bureau.csv')
df.to_sql('bureau', con = engine, if_exists = 'replace', index = False)
print(df.shape)
del df


all_df = pd.read_sql('''SELECT a.*,
                        IFNULL(p.cnt_prev_app, 0) as cnt_prev_app,
                        IFNULL(p.avg_prev_credit, 0) as avg_prev_credit,
                        IFNULL(b.cnt_bureau, 0) as cnt_bureau,
                        IFNULL(b.sum_bureau_debt, 0) as sum_bureau_debt,
                        IFNULL(b.sum_bureau_limit, 0) as sum_bureau_limit,
                        IFNULL(b.cnt_active_loans, 0) as cnt_active_loans
                        FROM applicants a
                     LEFT JOIN(
                        SELECT SK_ID_CURR,
                        count(SK_ID_PREV) as cnt_prev_app,
                        avg(AMT_CREDIT) as avg_prev_credit
                        FROM previous GROUP BY SK_ID_CURR) p
                        ON a.SK_ID_CURR = p.SK_ID_CURR
                     LEFT JOIN(
                        SELECT SK_ID_CURR,
                        count(SK_ID_BUREAU) as cnt_bureau,
                        sum(AMT_CREDIT_SUM_DEBT) as sum_bureau_debt,
                        sum(AMT_CREDIT_SUM) as sum_bureau_limit,
                        sum(CASE WHEN CREDIT_ACTIVE = 'Active' THEN 1 ELSE 0 END) as cnt_active_loans 
                        FROM bureau GROUP BY SK_ID_CURR) b
                        ON a.SK_ID_CURR = b.SK_ID_CURR''',engine)

all_df.to_csv('data/ModelInput.csv')


