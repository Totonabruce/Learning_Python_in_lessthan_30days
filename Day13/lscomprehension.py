# One way
from random import random
from re import A, M
import string
from zlib import Z_BLOCK


language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

# Generating numbers
numbers = [i for i in range(21)]  # to generate numbers from 0 to 20
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10..20]

# random numbers
import random
print(string.ascii_lowercase)