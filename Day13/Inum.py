# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 3rd Squares
cube = [i * i * i for i in range(6)]
print(cube) 

# It is also possible to make a list of tuples
numbers = [(i, i * i, i*i*i) for i in range(11)]
print(numbers) 

