#a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
toppings= input('What topping would you like to add:')
while toppings != 'quit':
    print ('I will add', toppings, 'to your pizza!') #print a message saying you add the 
    toppings = input ('would you like to add more?:')
else:
    print ('Thank you, have a great day.')
