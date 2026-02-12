import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# --- PART 1: MAPE Calculation (from Slide 70) ---
def calculate_mape(actual, forecast):
    actual, forecast = np.array(actual), np.array(forecast)
    # Formula: MAPE = (100/n) * sum(|Forecast - Actual| / Actual)
    mape = (100 / len(actual)) * np.sum(np.abs((forecast - actual) / actual))
    return mape

# Example data from your slide table
actual_demand = [42, 45, 49, 55, 57, 60, 62, 58, 54, 50, 44, 40]
forecast_demand = [44, 46, 48, 50, 55, 60, 64, 60, 53, 48, 42, 38]
print(f"Calculated MAPE from Slide Data: {calculate_mape(actual_demand, forecast_demand):.2f}%")


# --- PART 2: Logistic Regression (Week 4 Experiment) ---
# Load Spambase Dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
data = pd.read_csv(url, header=None)

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split and Scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# --- PART 3: Logistic Regression Curve (Sigmoid) ---
plt.figure(figsize=(10, 5))
# Get decision scores (log-odds) for the X-axis
decision_scores = model.decision_function(X_test)
# Get probabilities for the Y-axis
probabilities = model.predict_proba(X_test)[:, 1]

# Sort values for a smooth sigmoid curve line
sort_idx = np.argsort(decision_scores)
plt.plot(decision_scores[sort_idx], probabilities[sort_idx], color='blue', label='Logistic Curve')
plt.scatter(decision_scores, y_test, alpha=0.1, color='red', label='Actual Data')
plt.axhline(y=0.5, color='black', linestyle='--', label='Threshold')
plt.title("Logistic Regression Curve (Sigmoid)")
plt.xlabel("Log-Odds")
plt.ylabel("Probability of Spam")
plt.legend()
plt.show()

# --- PART 4: Evaluation Metrics ---
y_pred = model.predict(X_test)
print("\n--- Model Requirements ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))