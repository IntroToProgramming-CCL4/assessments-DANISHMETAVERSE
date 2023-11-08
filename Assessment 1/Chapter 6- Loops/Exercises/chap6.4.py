#Make a list called sandwich_orders and fill it with the names of various sandwiches.
sandwich_orders = ['Swap sandwich','club sandwtich', 'plain sandwich', 'rueben sandwich', 'bánh mì'] 
finished_sandwiches =[]#make an empty list called finished_sandwiches.

while sandwich_orders:
    current_sandwich = sandwich_orders.pop() 
    print("\nI made you a",current_sandwich)#this prints out that you make the sandwich
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich , " is done\n") #prints out that sandwich orders are done
    