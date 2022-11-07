fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
does_exist = 'lemon' in fruits
print(does_exist)  #True

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
fruits.append('Sandara')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
fruits.insert(0, 'Machungwa')
print(fruits)
fruits.insert(1, 'Maembe')
print(fruits)

fruits.remove('Maembe')
fruits.remove('lemon')
fruits.remove('Machungwa')

fruits.pop(0)
print(fruits)     
fruits.pop(1)
print(fruits)
fruits.pop(2)
print(fruits)
