from optparse import Values


lecturer = {
    'first_name':'Totona',
    'last_name':'Lonyeiye',
    'age':27,
    'country':'Kenya',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
     
    }
print(lecturer)
print(len(lecturer))
print(lecturer['first_name']) # Totona
print(lecturer['country'])    # Kenya
print(lecturer['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(lecturer['skills'][0])  # JavaScript
print(lecturer['address']['street']) # Space street
print(lecturer['address']['zipcode'])       # zipcode

lecturer['job_title'] = 'Instructor'
lecturer['skills'].append('HTML')
print(lecturer)

lecturer['first_name'] = 'Saningo'
lecturer['age'] = 21
print(lecturer)

lecturer.pop('country')
lecturer.popitem()
del lecturer['first_name']
print(lecturer)

# copying a dictionary
lecturer_copy = lecturer.copy()
print(lecturer_copy)

keys = lecturer.keys()
print(keys)
values = lecturer.values()
print(values)

    