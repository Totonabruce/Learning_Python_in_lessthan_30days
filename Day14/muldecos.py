# Applying multiple decorators
''' These decorator functions are higher order function that takes functions as parameters '''
def uppercase_decorator (function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# 2nd decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_decorator = func.spliited()
        return splitted_decorator
    return wrapper
@split_string_decorator
@uppercase_decorator # Order which deco is important

def greeting ():
    return 'welcome to python for cyber security'
print(greeting)
 

