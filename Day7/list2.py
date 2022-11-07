fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana','citrus','avocado']
fruits = set(fruits) # {'banana', 'orange', 'mango', 'lemon','orange', 'banana','citrus','avocado'}
print(fruits)
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
cereals = {'maize','wheat','rice','millet','beans'}
fruits.update(cereals)
print(fruits)