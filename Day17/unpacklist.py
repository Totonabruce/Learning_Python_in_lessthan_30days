from ast import arg
import numbers


def sumof5nums (a,b,c,d,e):
    return a+b+c+d+e
lst = [1,2,3,4,5]
print(sumof5nums(*lst))


numbers = range (2,7)
print(list(numbers))
args = [2,7]
numbers = range(*args)
print(numbers)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print (fin, sw, nor, rest)

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)