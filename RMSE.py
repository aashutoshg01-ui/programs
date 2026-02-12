import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_squared_error
from sklearn.preprocessing import StandardScaler

# --- PART 1: Error Metrics from Slides 68 & 70 ---
def calculate_manual_metrics(actual, forecast):
    actual = np.array(actual)
    forecast = np.array(forecast)
    
    # MSE Formula from Slide 68: Sum of Squared Errors / N
    mse = np.mean((actual - forecast) ** 2)
    
    # MAPE Formula from Slide 70: (100/n) * Sum(|Forecast - Actual| / Actual)
    mape = (100 / len(actual)) * np.sum(np.abs((forecast - actual) / actual))
    
    return mse, mape

# Data from Slide Table
actual_demand = [42, 45, 49, 55, 57, 60, 62, 58, 54, 50, 44, 40]
forecast_demand = [44, 46, 48, 50, 55, 60, 64, 60, 53, 48, 42, 38]

mse_val, mape_val = calculate_manual_metrics(actual_demand, forecast_demand)
print(f"Slide Results -> MSE: {mse_val:.4f}, MAPE: {mape_val:.2f}%")

# --- PART 2: Logistic Regression Experiment ---
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
data = pd.read_csv(url, header=None)
X, y = data.iloc[:, :-1], data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# --- PART 3: Drawing the Logistic Regression Curve ---
plt.figure(figsize=(10, 6))
# Raw model scores (log-odds)
logits = model.decision_function(X_test)
# Predicted probabilities
probs = model.predict_proba(X_test)[:, 1]

# Sort for smooth line plot
sort_idx = np.argsort(logits)
plt.plot(logits[sort_idx], probs[sort_idx], color='blue', label='Logistic Sigmoid Curve')
plt.scatter(logits, y_test, alpha=0.1, color='red', label='Actual Observations')
plt.axhline(y=0.5, color='green', linestyle='--', label='Decision Threshold (0.5)')
plt.title("Logistic Regression Curve (Sigmoid)")
plt.xlabel("Log-Odds (Decision Function)")
plt.ylabel("Probability of Spam")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# --- PART 4: Final Evaluation ---
y_pred = model.predict(X_test)
print("\nClassification Performance:")
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))