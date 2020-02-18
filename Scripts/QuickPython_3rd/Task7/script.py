counter = {}
max = 0
with open("moby_01_clean.txt") as infile:
    for line in infile:
        counter[line.strip()] = counter.get(line.strip(), 0) + 1 # считаем количество
        if counter[line.strip()] > max:
            max = counter[line.strip()]
    for word in counter:
        if counter[word] == 1:
            print("Min count (1): " + word)
    for word in counter:
        if counter[word] == max:
            print("Max count (" + str(max) + "): " + word)
