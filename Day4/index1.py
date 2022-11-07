# working with indexes

first_name = 'Totona'
last_name = 'Bruce'
age = 289
job = 'teacher'
country = 'KENYA'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314



challenge = 'thirty days of python'
sub_string = 'py'
print(challenge.index(sub_string))  # 15
print(challenge.index(sub_string, 10)) # 15

challenge = 'thirty days of python'
sub_string = 'py'
print(challenge.rindex(sub_string))  # 15
print(challenge.rindex(sub_string, 10)) # 15

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # true
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed