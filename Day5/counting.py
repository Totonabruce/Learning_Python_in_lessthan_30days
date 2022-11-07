fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence

fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]

fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]

print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
print(sorted(fruits, reverse=True))
#fruits = sorted(fruits,reverse=True)
#print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
