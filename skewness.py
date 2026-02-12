classes = [(2, 4), (4, 6), (6, 8), (8, 10)]
freq = [3, 4, 2, 1]

mid = [(c[0] + c[1]) / 2 for c in classes]
n = sum(freq)
sum_fx = sum(f * x for f, x in zip(freq, mid))
mean = sum_fx / n

sum_f_x2 = sum(f * (x - mean) ** 2 for f, x in zip(freq, mid))
sd = (sum_f_x2 / n) ** 0.5

sum_f_x3 = sum(f * (x - mean) ** 3 for f, x in zip(freq, mid))
skewness = (sum_f_x3 / ((n - 1) * (sd ** 3)))

sum_f_x4 = sum(f * (x - mean) ** 4 for f, x in zip(freq, mid))
kurtosis = (sum_f_x4 / ((n - 1) * (sd ** 4)))

print("Mean =", round(mean, 2))
print("Standard Deviation =", round(sd, 2))
print("Skewness =", round(skewness, 2))
print("Kurtosis =", round(kurtosis, 2))
