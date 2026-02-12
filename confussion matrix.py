# 1. Import Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. Create Sample Telecom Customer Dataset
# (Since Kaggle dataset cannot be downloaded in lab PCs)

data = {
    "tenure": [1, 5, 12, 24, 36, 2, 8, 15, 20, 30, 40, 3, 10, 18, 25],
    "MonthlyCharges": [70, 80, 65, 90, 100, 75, 85, 60, 95, 110, 120, 72, 78, 88, 105],
    "TotalCharges": [70, 400, 780, 2160, 3600, 150, 680, 900, 1900, 3300, 4800, 200, 780, 1600, 2600],
    "Churn": [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

print("\nTelecom Customer Dataset:\n")
print(df)

# 3. Feature Selection
X = df.drop("Churn", axis=1)
y = df["Churn"]

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 5. Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Prediction
y_pred = model.predict(X_test)

# 7. Model Evaluation
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("\nAccuracy:", round(accuracy*100, 2), "%")
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", report)

# 8. Confusion Matrix Visualization
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
