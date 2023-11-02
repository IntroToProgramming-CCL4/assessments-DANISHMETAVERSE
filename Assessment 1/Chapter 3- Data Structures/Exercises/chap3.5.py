invited_list = ['Kanye West', 'Michael Jackson', 'Bobby Wardell Sandimanie III']

for invited in invited_list:
    print(f"Dear {invited}, I cordially invite you to dinner at my house, Warm regards.")

# person who couldnt make it 
print(f"Unfortunately, {invited_list[1]} has a busy schedule and cant make it.")

# replacement person
invited_list[1] = 'Renoah Bernardino'

# second set of invitation message 
print("                             - Updated Invitations -                               ")
for invited in invited_list:
    print(f"Dear {invited}, I cordially invite you to dinner at my house, Warm regards.")