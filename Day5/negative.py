fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
print(fruits[-4:])
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
print(fruits[-3:-1])
print(fruits[:-1])
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
print(fruits[-3:])
print(fruits[-2:])
print(fruits[-1:])
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']