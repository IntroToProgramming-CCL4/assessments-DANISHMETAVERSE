invited_list = ['Kanye West', 'Michael Jackson', 'Bobby Wardell Sandimanie III']
for invited in invited_list:
    print ('I am delighted to inform that you are invited to dinner,', invited)

print (invited_list[0], 'Cant make it to dinner')
print ('Not coming:', invited_list[0])
invited_list.remove ('Kanye West')

print('NEWLIST')
invited_list.insert (0, 'Vladimir Putin')

invited_list = ['Vladimir Putin', 'Michael Jackson', 'Bobby Wardell Sandimanie III']
for invited in invited_list:
    print ('I am delighted to inform that you are invited to dinner,', invited)

print ('Im really sorry i can only invite 2 people for dinner')
poppedguest = invited_list.pop(0)
print ('Im sorry but you dont fit', poppedguest, 'maybe next time.')

for poppedguest in invited_list:
    print ('I am delighted to inform that you are still invited to dinner,', poppedguest)

del invited_list [0]
del invited_list [0]
print ('Remaining guests:',invited_list)
