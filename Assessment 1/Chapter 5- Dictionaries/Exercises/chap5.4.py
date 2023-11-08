
rivers = {'Nile River': 'Egypt', 'Niger River': 'Africa', 'Mississippi River': 'USA'}
for key, value in rivers.items():
    print ('\nThe', key, 'runs through', value) 
#Use a loop to print a sentence about each river.
 for key in rivers.keys():
    print ('\nRiver name -', key)
#Use a loop to print the name of each river included in the dictionary.
for value in rivers.values():
    print (f'\nlocation -', value)
#se a loop to print the name of each country included in the dictionary.
