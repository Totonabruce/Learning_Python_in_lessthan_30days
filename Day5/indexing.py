fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # first fruit
print(first_fruit)
last_fruit = fruits[-1]
print(last_fruit)
last_fruit1 = fruits[-2]
print(last_fruit1)

# last index
fruits = ['banana', 'orange', 'mango', 'lemon']
last_index = len(fruits) -1
print (last_index)
first_fruit = fruits[-4]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

lst = ['item','item2','item3', 'item4', 'item5', 'item 6']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']