#
# Example file for working with functions
#

# define a basic function
def func1():
    print("This is func1")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def func3(x):
    return x*x*x
# function with default value for an argument
def func4(num, x = 1):
    result = 1
    for i in range(x):
        result = result * num
    return result
#function with variable number of arguments
def func5(*args):
    result = 0
    for x in args:
        result = result + x
    return result

func1()
print(func1())
print(func1)
func2(10,20)
print(func2(10,20))
print(func2)
func3(5)
print(func3(5))
print(func3)
func4(2)
print(func4(2))
print(func4)
func4(2,3)
print(func4(2,3))
print(func4)
func4(x = 2,num = 3)
print(func4(x = 2,num = 3))
print(func4)
func5(1,2,3,4,5)
print(func5(1,2,3,4,5))
print(func5)
