names = {}
name = input("What is the first name? ")
name = name
age = input("What is the first age? ")
age = int(age)
names[name] = age
name = input("What is the second name? ")
name = name
age = input("What is the second age? ")
age = int(age)
names[name] = age
name = input("What is the third name? ")
name = name
age = input("What is the third age? ")
age = int(age)
names[name] = age
name = input("Whose age show? ")
name = name
if name in names:
    print("His age is " + str(names[name]) + ".")
else:
    print("Unknown name.")
