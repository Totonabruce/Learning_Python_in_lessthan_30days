fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
print(fruits[0:4]) # prints all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
print(fruits[0:]) # Prints all the lsit. No stoppag included
orange_and_mango = fruits[1:3] # it does not include the first index
print(fruits[1:3]) # tems in index 1 to 4 only
orange_mango_lemon = fruits[1:]
print(fruits[1:]) # print items from the second on the list
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
print(fruits[::2]) # skip and item