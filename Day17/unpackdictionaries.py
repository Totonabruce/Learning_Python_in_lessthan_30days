def unpacking_person_infor(name, country, city, age):
    return f'{name} lives in {city}, {country}. He is {age} years old'
dct = {'name': 'Totona', 'country':'Kenya','city':'Nairobi','age':28}
print(unpacking_person_infor(**dct))