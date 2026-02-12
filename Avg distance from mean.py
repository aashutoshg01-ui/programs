# Group Frequency Table and Skewness Calculation

import math

# Given data
age_groups = [(2,4), (4,6), (6,8), (8,10)]
frequency = [16, 13, 7, 5]

# Step 1: Calculate Mid Values
mid_values = [(a+b)/2 for a,b in age_groups]

# Step 2: Calculate fx
fx = [mid_values[i] * frequency[i] for i in range(len(frequency))]

# Step 3: Mean Calculation
N = sum(frequency)
mean = sum(fx) / N

# Step 4: Standard Deviation Calculation
variance = sum([frequency[i] * (mid_values[i] - mean)**2 for i in range(len(frequency))]) / N
std_dev = math.sqrt(variance)

# Step 5: Median Calculation
cf = [sum(frequency[:i+1]) for i in range(len(frequency))]
N2 = N / 2

for i in range(len(cf)):
    if cf[i] >= N2:
        median_class_index = i
        break

L = age_groups[median_class_index][0]
f = frequency[median_class_index]
cf_prev = cf[median_class_index - 1] if median_class_index > 0 else 0
h = age_groups[0][1] - age_groups[0][0]

median = L + ((N2 - cf_prev) / f) * h

# Step 6: Skewness Calculation
skewness = 3 * (mean - median) / std_dev

# Display Table
print("\nGroup Frequency Table\n")
print("Age Group\tMid Value\tFrequency\tf*x")
for i in range(len(age_groups)):
    print(f"{age_groups[i]}\t\t{mid_values[i]}\t\t{frequency[i]}\t\t{fx[i]}")

print("\nTotal Frequency:", N)
print("Mean =", round(mean, 2))
print("Median =", round(median, 2))
print("Standard Deviation =", round(std_dev, 2))
print("Skewness =", round(skewness, 2))

# Differences Between Stratified & Cluster Sampling
print("\nDifferences Between Stratified and Cluster Sampling:\n")

print("Stratified Sampling:")
print("1. Population divided into homogeneous strata.")
print("2. Samples taken from each group.\n")

print("Cluster Sampling:")
print("1. Population divided into heterogeneous clusters.")
print("2. Only few clusters are selected.")
