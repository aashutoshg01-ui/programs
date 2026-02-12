values = [0, 1, 2, 3, 4, 5]
freq = [27, 96, 58, 54, 18, 7]

N = sum(freq)
mean = sum(v * f for v, f in zip(values, freq)) / N

cum_freq = []
total = 0
for f in freq:
    total += f
    cum_freq.append(total)

mid = N / 2

median = None
for i, cf in enumerate(cum_freq):
    if cf >= mid:
        median = values[i]
        break

mode = values[freq.index(max(freq))]

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
