fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
print(fruits)
print(len(fruits))
print('mango' in fruits) # checking mango in set of fruits
fruits.add('citrus') # Add citrus to the list of the fruits
fruits.add('avocado') # Add avocado to the list
print(fruits)
vegetables = {'spinach', 'Kales', 'cabbage','brocolli'}
fruits.update(vegetables)
print(fruits)
fruits.remove('Kales')
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)
del fruits
print(fruits)