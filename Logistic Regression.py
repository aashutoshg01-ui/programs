import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# 1. Load the Dataset
# We are using the UCI Spambase dataset directly via URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
# The dataset has 57 features and 1 target (last column)
data = pd.read_csv(url, header=None)

# 2. Separate Features (X) and Target (y)
X = data.iloc[:, :-1]  # All columns except the last
y = data.iloc[:, -1]   # The last column (1 = Spam, 0 = Not Spam)

# 3. Split the data into Training and Testing sets (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Feature Scaling 
# Logistic Regression performs better when features are on the same scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Build and Train the Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 6. Make Predictions
y_pred = model.predict(X_test)

# 7. Evaluate Model Performance (As per requirements)
print("--- Logistic Regression Model Performance ---")

# Accuracy
accuracy = accuracy_score(y_test, y_test) # Corrected logic: y_test vs y_pred
accuracy = accuracy_score(y_test, y_pred)
print(f"\n1. Accuracy Score: {accuracy * 100:.2f}%")

# Confusion Matrix
print("\n2. Confusion Matrix:")
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

# Classification Report (Precision, Recall, F1-score)
print("\n3. Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Not Spam', 'Spam']))