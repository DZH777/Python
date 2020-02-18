# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)
# # re-declaring the variable works
f = "abc"
print(f)
g = "abs"
print(g)
# # ERROR: variables of different types cannot be combined

#print("string" + 123)
print("string " + str(123))

# Global vs. local variables in functions
def someFunction():
    global g
    g = "qwe"
    f = "def"
    print("f in someFunction: " + f)
    print("g in someFunction: " + g)    

print("f before: " + f)
print("g before: " + g)
someFunction()
print("f after: " + f)
print("g after: " + g)

del g
print("g after del: " + g)
