rivers = {'Nile River': 'Egypt', 'Niger River': 'Africa', 'Mississippi River': 'USA'}
for key, value in rivers.items():
    print ('\nThe', key, 'runs through', value)
for key in rivers.keys():
    print ('\nRiver name -', key)
for value in rivers.values():
    print (f'\nlocation -', value)