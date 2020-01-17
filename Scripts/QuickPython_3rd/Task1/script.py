temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))
print("Max: " + str(max(temperatures)))
print("Min: " + str(min(temperatures)))
print("Avg: " + str(round(sum(temperatures)/len(temperatures),2)))
temperatures.sort()
print("Median: " + str(temperatures[round(len(temperatures)/2)]))
x = set(temperatures)
print("Unique: " + str(len(x)))
