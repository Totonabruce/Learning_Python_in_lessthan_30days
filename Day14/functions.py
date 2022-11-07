# Functions as parameters
def sum_numbers(nums): # normal function
    return sum(nums) # abusing the inbuilt function

def higher_order_functions(f, lst): # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_functions(sum_numbers, [1,2,3,4,5,6,7])
print(result)

# Function as a return value
def square (x): # square function
    return x**2
def cube (x): # cube function
    return x ** 3
def absolute (x): # Absolute function
    if x >=0:
     return x
    else:
        return - (x)
    
def higher_order_function(type): # A higher order function returning a fxn
    if type == 'square':
       return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3))
result = higher_order_function('absolute')
print(result(-3))



