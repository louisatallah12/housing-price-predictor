import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# dataset
data = {
    "sqft": [800, 1200, 1500, 1800, 2000, 2200, 2400, 2600],
    "bedrooms": [2, 3, 3, 4, 4, 5, 4, 5],
    "price": [150000, 200000, 250000, 300000, 320000, 360000, 380000, 400000]
}

df = pd.DataFrame(data)

# Train model
X = df[['sqft', 'bedrooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, './backend/models/model.pkl')
print("✅ Model trained and saved as 'model.pkl'")
