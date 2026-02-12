freq = [5, 3, 15, 40, 17, 12, 7, 1]
total_players = 100

less_than_65_95 = sum(freq[0:3])
percentage_a = (less_than_65_95 / total_players) * 100

between_61_95_65_95 = sum(freq[1:3])
percentage_b = (between_61_95_65_95 / total_players) * 100

between_61_95_71_95 = sum(freq[1:6])

print("a) Percentage less than 65.95 =", percentage_a, "%")
print("b) Percentage between 61.95 and 65.95 =", percentage_b, "%")
print("c) Number of players between 61.95 and 71.95 =", between_61_95_71_95)
