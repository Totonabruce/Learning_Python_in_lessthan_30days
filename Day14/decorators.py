# Normal function
from distutils.archive_util import make_archive


def greeting():
    return 'Hello Python Programming'
def upper_case_deco (function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = upper_case_deco(greeting)
print(g) # Greeting in upper case


# Same function but with a decorator
''' This decorator function is a higher function that takes a function as a decorator '''
def upper_case_deco(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@upper_case_deco
def greeting ():
    return 'hello python programming'
print(greeting())




    
