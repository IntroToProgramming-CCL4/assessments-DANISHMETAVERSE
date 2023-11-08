#print a message saying the deli has run out of pastrami
print ("Pastrami is out of stock")
sandwich_orders = ['Swap sandwich','club sandwtich', 'plain sandwich', 'rueben sandwich', 'bánh mì', 'pastrami', 'pastrami', 'pastrami' ] 
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami') #then use a while loop to remove all
finished_sandwiches =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("\nI made your",current_sandwich)
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich , " is done\n")





