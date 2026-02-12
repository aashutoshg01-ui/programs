import numpy as np

# Given grouped data
classes = [(0,9),(10,19),(20,29),(30,39),(40,49),(50,59),(60,69),(70,79),(80,89)]
frequency = np.array([20,21,23,16,11,10,7,3,1])

# Step 1: Midpoints
midpoints = np.array([(a+b)/2 for a,b in classes])

# Step 2: Mean Calculation
fx = midpoints * frequency
N = frequency.sum()

mean = fx.sum() / N

print("Estimated Mean =", round(mean,2))

# Step 3: Median Calculation
cf = np.cumsum(frequency)
n2 = N/2

median_class_index = np.where(cf >= n2)[0][0]

L = classes[median_class_index][0] - 0.5
f = frequency[median_class_index]
cf_prev = cf[median_class_index - 1]
h = classes[0][1] - classes[0][0] + 1

median = L + ((n2 - cf_prev)/f) * h

print("Estimated Median =", round(median,2))

# Step 4: Mode Calculation
modal_class_index = np.argmax(frequency)

L = classes[modal_class_index][0] - 0.5
fm = frequency[modal_class_index]
fm1 = frequency[modal_class_index - 1]
fm2 = frequency[modal_class_index + 1]

mode = L + ((fm - fm1) / ((fm - fm1) + (fm - fm2))) * h

print("Estimated Mode =", round(mode,2))
