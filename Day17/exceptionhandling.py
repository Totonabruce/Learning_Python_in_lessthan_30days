try:
    name = input('Enter your name')
    year_of_birth = input('Year of birth')
    age = 2022 - int(year_of_birth)
    print(f'You are {name}. And your age {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('I usually run with the try block')   
finally:
    print('I alway run.') 