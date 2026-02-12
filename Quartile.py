data = [46, 69, 32, 60, 52, 41]

n = len(data)

mean = sum(data) / n

deviations = [(x - mean) for x in data]
sq_deviations = [(x - mean)**2 for x in data]

sum_sq_dev = sum(sq_deviations)

sample_variance = sum_sq_dev / (n - 1)

print("Data:", data)
print("Mean:", mean)
print("Deviations:", deviations)
print("Squared Deviations:", sq_deviations)
print("Sum of Squared Deviations:", sum_sq_dev)
print("Sample Variance:", sample_variance)
