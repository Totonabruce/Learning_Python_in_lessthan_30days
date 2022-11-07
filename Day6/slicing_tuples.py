# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
print(all_items)
all_items = tpl[0:]         # all items
print(all_items)
middle_two_items = tpl[1:3]  # does not include item at index 3
print(middle_two_items)


fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
print(all_fruits)
all_fruits= fruits[0:]      # all items
print(all_fruits)
orange_mango = fruits[1:3]  # doesn't include item at index 3
print(orange_mango)
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)