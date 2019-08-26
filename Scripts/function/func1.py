import copy

a = [1, 2, 3, 7]
b = a[:]
print(a)
print(b)
a[1] = 10
print(a)
print(b)


test2 = [[None, None, None], [None, None, None], [None, None, None]]
print(test2)

temp1 = test2[:]
temp1[1][1] = 'J'

temp2 = copy.deepcopy(test2)
temp2[1][2] = 'X'

print("temp1 " + str(temp1))
print("test2 " + str(test2))
print("temp2 " + str(temp2))

