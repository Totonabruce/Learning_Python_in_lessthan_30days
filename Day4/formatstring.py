# string only

from cmath import pi


fname = 'Bruce'
lname = 'Totona'
language = 'Python'
format_string = 'I am %s %s. I teach %s. ' %(fname, lname, language)
print (format_string)

# string and numbers
radius = 7
pi = 3.14
area = pi * radius **2
format = 'The area of a circle with radius %d is: %.2f.' % (radius, area)
print (format)

# fixed list - tuple
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
format_string = 'The following are python libraries: %s' %(python_libraries)
print (format_string)

# working with python3
first_name = 'Bruno'
last_name = 'Tots'
language = 'Python'
format_string = 'I am {} {}. I teach {}.' .format(first_name, last_name, language)
print(format_string)

a = 5
b= 3

print('{} + {} = {}' .format(a , b, a + b))
print('{} - {} = {}' .format(a, b, a - b))
print('{} * {} = {}' .format(a, b, a * b))
print('{} / {} = {:.2f}' .format(a,b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)