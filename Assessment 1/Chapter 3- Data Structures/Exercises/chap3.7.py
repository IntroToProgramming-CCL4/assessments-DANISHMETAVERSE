places= ['GREAT PYRAMID OF GIZA','LIGHTHOUSE OF ALEXANDRIA.','HANGING GARDENS','STATUE OF ZEUS','TEMPLE OF ARTEMIS', 'MAUSOLEUM AT HALICARNASSUS', 'COLOSSUS OF RHODES']
print ("Original:", places) #Print your list in its original order

print ("Alphabetical:", sorted(places))

print ("Original 2:", places)#Show that your list is still in its original order by printing it.

print ("Reverse alphabetical:", sorted(places, reverse=True))

print ("Original 3:", places)#Show that your list is still in its original order by printing it again.

places.reverse()#change order of list

print ('Reversed:', places)

places.reverse()#change order of list again. 

print ('Original after reversing:', places)

places.sort() #alphabetical order.

print ('Alphabetical order with Sort():', places)

places.sort(reverse=True) #reverse alphabetical order.

print ('Reverse alphabetical with Sort():', places)