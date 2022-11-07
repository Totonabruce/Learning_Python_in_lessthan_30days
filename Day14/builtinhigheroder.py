# Built in highr order functions functions
import numbers


numbers = [0,1,2,3,4,5,6,7,8,9] # Iterable
def square (x): # square function
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))
# Introducing lambda function
numbers_squared = map (lambda x : x ** 2, numbers)
print(list(numbers_squared))
