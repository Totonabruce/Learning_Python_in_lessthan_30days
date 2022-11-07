banana = {
        'county':'Narok',
        'type': 'Easy_ripe',
        'soil': 'loamy',
        'temperature': 22-32,
        'years_of_maturity':2.5,
        'color_changed': False,
        'alternative_soil' : ['fertile_clay', 'sand','murram'],
        'other_countries':{
            'One':'Uganda',
            'Two':'Tanzania'
        }
        }
print(banana)
print(len(banana))

print(banana.get('county'))
print(banana.get('other_countries'))
print(banana.get('alternative_soil'))

banana['cost_per_kg'] = 'Ksh 50'
banana['alternative_soil'].append('Red_clay')
print(banana)

print(('soil') in banana) # True
print(('kenya' in banana))

print(banana.items())
print(banana.clear())
del banana
