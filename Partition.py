# Data from the confusion matrix
TP = 22
TN = 60
FP = 10
FN = 8

# Total samples
total = TP + TN + FP + FN

# (i) Accuracy: (TP + TN) / Total
accuracy = (TP + TN) / total

# (ii) Recall (Sensitivity): TP / (TP + FN)
recall = TP / (TP + FN)

# (iii) Precision: TP / (TP + FP)
precision = TP / (TP + FP)

# (iv) F1-Score: 2 * (Precision * Recall) / (Precision + Recall)
f1_score = 2 * (precision * recall) / (precision + recall)

# Display Results
print(f"--- Classification Metrics ---")
print(f"Accuracy:  {accuracy:.2f}")
print(f"Recall:    {recall:.2f}")
print(f"Precision: {precision:.2f}")
print(f"F1-Score:  {f1_score:.2f}")