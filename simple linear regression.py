# Average Distance Between Data Values and Mean

# Given data
data = [12, 23, 31, 15, 26, 24, 16, 23]

# Step 1: Calculate Mean
mean = sum(data) / len(data)

# Step 2: Calculate Absolute Distances
distances = [abs(x - mean) for x in data]

# Step 3: Calculate Average Distance
avg_distance = sum(distances) / len(distances)

# Display results
print("Data values:", data)
print("Mean:", round(mean, 2))
print("Absolute distances:", [round(d,2) for d in distances])
print("Average distance from mean:", round(avg_distance, 2))
