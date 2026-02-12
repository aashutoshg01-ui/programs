import numpy as np

# Dataset from the image
data = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]
num_bins = 3

def equal_frequency(data, k):
    # Sort data (already sorted in this case)
    data = sorted(data)
    n = len(data)
    # Calculate items per bin
    bin_size = n // k
    bins = [data[i * bin_size : (i + 1) * bin_size] for i in range(k)]
    return bins

def equal_width(data, k):
    # Width = (max - min) / k
    low, high = min(data), max(data)
    width = (high - low) / k
    
    bins = [[] for _ in range(k)]
    for x in data:
        # Determine index, ensuring the max value stays in the last bin
        idx = int((x - low) / width)
        if idx == k:
            idx -= 1
        bins[idx].append(x)
    
    bin_ranges = [(low + i*width, low + (i+1)*width) for i in range(k)]
    return bins, bin_ranges

# --- Calculations ---
freq_bins = equal_frequency(data, num_bins)
width_bins, ranges = equal_width(data, num_bins)

# --- Output ---
print("i. Equal Frequency Partitioning (4 items per bin):")
for i, b in enumerate(freq_bins):
    print(f"   Bin {i+1}: {b}")

print("\nii. Equal Width Partitioning:")
print(f"   (Range: {min(data)} to {max(data)}, Width: {(max(data)-min(data))/3:.2f})")
for i, b in enumerate(width_bins):
    print(f"   Bin {i+1} {np.round(ranges[i], 2)}: {b}")