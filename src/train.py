import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load Data
df = pd.read_csv('data/housing.csv')
X = df.drop('median_house_value', axis=1).select_dtypes(include=['number'])
y = df['median_house_value']

# Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Metrics
preds = model.predict(X_test)
rmse = mean_squared_error(y_test, preds, squared=False)
r2 = r2_score(y_test, preds)

# Save Outputs
joblib.dump(model, 'model.pkl')
metrics = {
    "rmse": round(rmse, 2),
    "r2": round(r2, 4),
    "dataset_size": len(df)
}
with open('metrics.json', 'w') as f:
    json.dump(metrics, f)

print(f"Training Complete. Dataset size: {len(df)}")