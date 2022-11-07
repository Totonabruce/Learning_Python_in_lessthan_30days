tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
fruits = list(fruits)

print('orange' in fruits) # True
print('apple' in fruits) # False
print('banana' in fruits)
fruits = tuple(fruits)
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment