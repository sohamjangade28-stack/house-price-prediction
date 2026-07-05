import sys

import pandas as pd
from sklearn.linear_model import LinearRegression

# Ensure the ₹ symbol prints on any console (e.g. Windows cp1252).
sys.stdout.reconfigure(encoding="utf-8")

# House Dataset
house_data = [
    [1000, 2, 1, 3500000],
    [1200, 2, 2, 4200000],
    [1400, 3, 2, 5000000],
    [1600, 3, 2, 5800000],
    [1800, 3, 3, 6500000],
    [2000, 4, 3, 7300000],
    [2200, 4, 3, 8100000],
    [2400, 4, 4, 9000000],
    [2600, 5, 4, 9800000],
    [3000, 5, 5, 11500000]
]

# Convert into DataFrame
df = pd.DataFrame(
    house_data,
    columns=["Area", "Bedrooms", "Bathrooms", "Price"]
)

print("House Dataset")
print(df)

# Features and Target
features = df.drop("Price", axis=1)
target = df["Price"]

# Train Model
lr = LinearRegression()
lr.fit(features, target)
print("\nTraining Completed!")

# Predict Price
print("\nEnter New House Details")
area = float(input("Square Footage: "))
bedrooms = int(input("Bedrooms: "))
bathrooms = int(input("Bathrooms: "))

new_house = pd.DataFrame(
    [[area, bedrooms, bathrooms]],
    columns=["Area", "Bedrooms", "Bathrooms"]
)

predicted_price = lr.predict(new_house)

print("\nEstimated House Price: ₹", round(predicted_price[0], 2))

# Model Parameters
print("\nIntercept:", lr.intercept_)
print("Area Coefficient:", lr.coef_[0])
print("Bedrooms Coefficient:", lr.coef_[1])
print("Bathrooms Coefficient:", lr.coef_[2])