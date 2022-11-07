try:
    name = input('Name')
    Dob = input('DOB')
    age = 2022 - int(Dob)
    print(f'You are {name} and your age is {age}.')
except Exception as e:
    print (e)