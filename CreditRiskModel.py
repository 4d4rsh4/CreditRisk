import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('data/ModelInput.csv')

cols = ['NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','CODE_GENDER']

for col in cols:
    df[col] =df[col].fillna('Unknown')

df_dummies = pd.get_dummies(df[cols], drop_first = True)

df['AGE'] = df['DAYS_BIRTH'] / -365.25
df['EMPLOYED'] = df['DAYS_EMPLOYED'] / -365.25

num_cols = ['EXT_SOURCE_1', 
            'EXT_SOURCE_2', 
            'EXT_SOURCE_3',
            'AMT_INCOME_TOTAL', 
            'AMT_CREDIT', 
            'AGE',
            'EMPLOYED',    
            'cnt_prev_app', 
            'avg_prev_credit', 
            'sum_bureau_debt', 
            'cnt_active_loans']

X = pd.concat([df[num_cols], df_dummies], axis = 1)
y = df['TARGET']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state = 42)

weight = (y_train == 0).sum()/(y_train == 1).sum()
model = XGBClassifier( scale_pos_weight = weight, n_estimators = 2000, learning_rate=0.01, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('Accuracy Score')
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
})
importance_df.to_csv('data/FeatureImportance.csv', index = False)
