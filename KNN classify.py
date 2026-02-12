import numpy as np
import matplotlib.pyplot as plt

# Dataset from image
prices = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]
num_bins = 3

# i. Equal Frequency (Equi-depth) Partitioning
def equal_frequency(data, k):
    n = len(data)
    depth = n // k
    return [data[i * depth : (i + 1) * depth] for i in range(k)]

# ii. Equal Width Partitioning
def equal_width(data, k):
    low, high = min(data), max(data)
    width = (high - low) / k
    bins = [[] for _ in range(k)]
    for x in data:
        idx = int((x - low) / width)
        if idx == k: idx -= 1 # Include max value in last bin
        bins[idx].append(x)
    return bins, width

# Execution
freq_bins = equal_frequency(prices, num_bins)
width_bins, w = equal_width(prices, num_bins)

print(f"Equal Frequency Bins: {freq_bins}")
print(f"Equal Width Bins (Width={w:.1f}): {width_bins}")