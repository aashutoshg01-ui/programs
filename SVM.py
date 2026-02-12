# 1- Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2- Load MNIST Dataset
print("Loading MNIST dataset...")

mnist = fetch_openml('mnist_784', version=1)

X, y = mnist.data, mnist.target

# Convert labels to integers
y = y.astype(int)

print("Dataset Loaded Successfully")
print("Total samples:", X.shape[0])

# 3- Preprocess the Data
# Normalize features
X = X / 255.0

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# 4- Train the SVM Model
print("Training SVM Model...")

# Using subset for faster execution (very important)
svm_model = SVC(kernel='linear', C=1.0)

svm_model.fit(X_train[:10000], y_train[:10000])

print("Training Completed")

# 5- Prediction
y_pred = svm_model.predict(X_test[:2000])

# 6- Model Evaluation
accuracy = accuracy_score(y_test[:2000], y_pred)
print("\nAccuracy:", accuracy * 100, "%")

cm = confusion_matrix(y_test[:2000], y_pred)
print("\nConfusion Matrix:\n", cm)

print("\nClassification Report:\n", classification_report(y_test[:2000], y_pred))

# 7- Visualization
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# 8- Show Sample Prediction
plt.imshow(X_test.iloc[0].values.reshape(28,28), cmap='gray')
plt.title(f"Predicted: {y_pred[0]}  Actual: {y_test.iloc[0]}")
plt.axis('off')
plt.show()
