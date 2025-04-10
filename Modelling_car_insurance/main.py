import pandas as pd
import numpy as np
from statsmodels.formula.api import logit

# 1. Identify the single feature of the data that is the best predictor of
#    whether a customer will put in a claim (the "outcome" column), excluding the "id" column.
car_ins = pd.read_csv('car_insurance.csv')
#print(car_ins.head())

vars=car_ins.columns[1:17]
# All columns:  ['id', 'age', 'gender', 'driving_experience', 'education', 'income',
#        'credit_score', 'vehicle_ownership', 'vehicle_year', 'married',
#        'children', 'postal_code', 'annual_mileage', 'vehicle_type',
#        'speeding_violations', 'duis', 'past_accidents', 'outcome']

res = pd.DataFrame(np.nan, index=range(len(vars)), columns=['Feature', 'Accuracy'])

for i in range(len(vars)):
    form = 'outcome~'+vars[i]
    mdl = logit(form, data=car_ins).fit()
    conf_mat = mdl.pred_table()
    accur = (conf_mat[0,0]+conf_mat[1,1])/(conf_mat[0,0] + conf_mat[0,1]+ conf_mat[1,0]+ conf_mat[1,1])
    res.loc[i, 'Feature'] = vars[i]
    res.loc[i, 'Accuracy'] = accur

print(res)
best_accuracy = max(res['Accuracy'])
best_feature = res['Feature'][res['Accuracy']==best_accuracy]

# 2. Store as a DataFrame called best_feature_df, containing columns named "best_feature"
#    and "best_accuracy" with the name of the feature with the highest accuracy,
#    and the respective accuracy score.

best_feature_df = pd.DataFrame({"best_feature": best_feature, "best_accuracy":best_accuracy})
print(best_feature_df)