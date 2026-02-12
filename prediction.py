import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given data
demand = np.array([65, 66, 67, 67, 68, 69, 70, 72]).reshape(-1, 1)
price = np.array([67, 68, 65, 68, 72, 72, 69, 71])

# Create Linear Regression model
model = LinearRegression()
model.fit(demand, price)

# Get slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

print("Slope (m):", round(slope, 3))
print("Intercept (c):", round(intercept, 3))

# Regression equation
print("\nRegression Equation:")
print(f"Price = {round(slope,3)} * Demand + {round(intercept,3)}")

# Prediction
predicted_price = model.predict(demand)

# Plot
plt.scatter(demand, price)
plt.plot(demand, predicted_price)
plt.xlabel("Demand")
plt.ylabel("Price")
plt.title("Demand vs Price Regression")
plt.show()
