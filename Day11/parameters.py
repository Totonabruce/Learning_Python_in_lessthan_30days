
from cmath import pi


def greeetings (name):
    message = name + " , I am enjoying python programming"
    return message

print(greeetings('Totona'))

def add_ten (num):
        ten = 10
        return num + ten
print(add_ten(150))

def square_number(x):
    return x * x
print (square_number(2))

def area_of_a_circle(r):
    pi = 3.14
    area = pi * r **2
    return area
print(area_of_a_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050  
  
