import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the dataset
crops = pd.read_csv("soil_measures.csv")
# Check for missing values
print(crops.isna().sum().sort_values())
print(crops['crop'].unique())
# 22 different crops: ['rice' 'maize' 'chickpea' 'kidneybeans' 'pigeonpeas' 'mothbeans'
# 'mungbean' 'blackgram' 'lentil' 'pomegranate' 'banana' 'mango' 'grapes' 'watermelon'
# 'muskmelon' 'apple' 'orange' 'papaya' 'coconut' 'cotton' 'jute' 'coffee']

## 2200 observations of N, P, K, ph

X = crops.drop(columns='crop')
y = crops['crop']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42, shuffle=True)
features = ['N', 'P', 'K', 'ph']

feature_performance = {}
log_reg = LogisticRegression(multi_class="multinomial")

for feature in features:
    log_reg.fit(X_train[[feature]], y_train)
    y_pred = log_reg.predict(X_test[[feature]])
    f1 = metrics.f1_score(y_test, y_pred, average="weighted")
    feature_performance[feature] = f1
    print(f"F1-score for {feature}: {f1}")

best_feature = max(feature_performance, key = feature_performance.get)
best_predictive_feature = { best_feature:feature_performance[best_feature]}

print(best_predictive_feature)