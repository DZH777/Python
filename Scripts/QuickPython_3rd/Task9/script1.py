def decorate(func):
    def wrapper_func(*args):
        print("<html>" +  func(*args) + "</html>")
    return wrapper_func

def myfunction(parameter):
    print(parameter)

@decorate
def myfunction(parameter):
    return parameter

myfunction("hello")
