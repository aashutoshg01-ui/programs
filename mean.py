import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Create dataset
data = {
    "Species": ["Bream","Bream","Bream","Bream","Bream","Bream",
                "Roach","Roach","Roach","Roach","Roach","Roach","Roach"],
    "Weight": [242,290,340,363,500,1000,200,180,290,390,160,140,40],
    "Length": [25.4,26.3,26.5,29,29.7,37,23.5,25.2,26,31.7,22.5,20.8,14.5]
}

df = pd.DataFrame(data)
print("\nFish Dataset:\n", df)

# Step 2: Separate data by species
bream = df[df["Species"] == "Bream"]
roach = df[df["Species"] == "Roach"]

# Step 3: Prepare input (X) and output (Y)
X_bream = bream[["Length"]]
y_bream = bream["Weight"]

X_roach = roach[["Length"]]
y_roach = roach["Weight"]

# Step 4: Train Linear Regression Models
model_bream = LinearRegression()
model_roach = LinearRegression()

model_bream.fit(X_bream, y_bream)
model_roach.fit(X_roach, y_roach)

# Step 5: Extract Slope and Intercept
print("\n--- Regression Model Parameters ---")

print("\nBream Species:")
print("Slope (m):", round(model_bream.coef_[0], 2))
print("Intercept (c):", round(model_bream.intercept_, 2))

print("\nRoach Species:")
print("Slope (m):", round(model_roach.coef_[0], 2))
print("Intercept (c):", round(model_roach.intercept_, 2))

# Step 6: Plot Regression Lines
plt.figure(figsize=(10,5))

# Bream Plot
plt.subplot(1,2,1)
plt.scatter(X_bream, y_bream)
plt.plot(X_bream, model_bream.predict(X_bream))
plt.title("Bream: Weight vs Length")
plt.xlabel("Length (cm)")
plt.ylabel("Weight (g)")

# Roach Plot
plt.subplot(1,2,2)
plt.scatter(X_roach, y_roach)
plt.plot(X_roach, model_roach.predict(X_roach))
plt.title("Roach: Weight vs Length")
plt.xlabel("Length (cm)")
plt.ylabel("Weight (g)")

plt.tight_layout()
plt.show()
