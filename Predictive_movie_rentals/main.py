import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE

pd.set_option('display.max_columns', None)

rental = pd.read_csv('rental_info .csv')
print(rental.info())
rental['rental_date'] = pd.to_datetime(rental['rental_date'])
rental['return_date'] = pd.to_datetime(rental['return_date'])
rental['rental_length_days'] = (rental['return_date'] - rental['rental_date']).dt.days
rental['deleted_scenes'] = rental['special_features'].apply(lambda x: 1 if 'Deleted Scenes' in x else 0)
rental['behind_the_scenes'] = rental['special_features'].apply(lambda x: 1 if 'Behind the Scenes' in x else 0)
print(rental.head())

subset_1 = ['rental_length_days', 'amount', 'release_year', 'rental_rate', 'length', 'replacement_cost',
            'amount_2', 'length_2', 'rental_rate_2']
cov_matrix = np.cov(rental[subset_1], rowvar=False)  # Columns as variables

# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cov_matrix, annot=True, fmt=".3f", cmap='coolwarm',
            xticklabels=subset_1,
            yticklabels=subset_1)
plt.title("Covariance Matrix")
#plt.show()

### Model 1:
features = ['amount', 'release_year', 'rental_rate', 'length', 'replacement_cost', 'NC-17',
                 'PG', 'PG-13', 'R', 'amount_2', 'length_2', 'rental_rate_2', 'deleted_scenes', 'behind_the_scenes']
X = rental[features]
y = rental['rental_length_days']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=9)
model = LinearRegression()
selector = RFE(model, n_features_to_select=8, step=1)
selector.fit(X_train, y_train)
print("Selected features are: ", selector.get_feature_names_out())
y_pred = selector.predict(X_test)
print("MSE for full model: {.3%f}", mean_squared_error(y_test, y_pred))

'''
from scipy import stats
mse = mean_squared_error(model_full.predict(X_train), y_train)
X_with_intercept = np.c_[np.ones(X_train.shape[0]), X_train]  # Add intercept term
cov_matrix = mse * np.linalg.inv(X_with_intercept.T @ X_with_intercept)
se = np.sqrt(np.diag(cov_matrix))[1:] # Remove intercept
t_stats = model_full.coef_ / se
p_values = 2 * (1 - stats.t.cdf(np.abs(t_stats), df=X.shape[0] - X.shape[1] - 1))
print(p_values)
'''