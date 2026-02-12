data = [78, 82, 85, 90, 92, 94, 95, 100, 110, 120, 150]

data.sort()

def median(lst):
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]

n = len(data)
mid = n // 2

if n % 2 == 0:
    lower_half = data[:mid]
    upper_half = data[mid:]
else:
    lower_half = data[:mid]        
    upper_half = data[mid+1:]      
    
Q1 = median(lower_half)
Q3 = median(upper_half)

IQR = Q3 - Q1

lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR

outliers = [x for x in data if x < lower_fence or x > upper_fence]

print("Data:", data)
print("Q1 =", Q1)
print("Q3 =", Q3)
print("IQR =", IQR)
print("Lower Fence =", lower_fence)
print("Upper Fence =", upper_fence)
print("Outliers =", outliers)
