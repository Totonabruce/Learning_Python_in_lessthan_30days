fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
print(vegetables)
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

del vegetables
print (fruits)
del fruits 
print (fruits) # Name fruits is not defined. The tuple is empty.