import time
cart = []
money = int(input('Insert Money: '))
print('Current Balance: $', money)

# MENU OF ITEMS BELOW
brand = {'A1': ['Banana\t', '1.0'], 'B1': ['Apple\t', '1.3'], 'C1': ['kiwi\t', '2.0'], 'D1': ['Avocado', '3.2'],
         'E1': ['Mango\t', '2.3'], 'F1': ['Pineapple', '1.4'], 'G1': ['Strawberry', '1.1']}

print('|--------------------Please Select A Fruit----------------------|')
for key, value in brand.items():
    print('| Code:', key, '\tFruit: ', value[0], '\tPrice/Kg: $', value[1], ' \t|')
print('#################################################################')

price1 = 0  # Initialize price1 outside the loop

while True:
    brand1 = input('Select Code:')
    brand1 = brand1.upper()

    while brand1 not in brand:
        print('Invalid Code')
        brand1 = input("Please enter a valid code or [Q] to quit:")
        if brand1.upper() == 'Q':
            print("Thank you, have a great day!")
            print("Please get your remaining balance of", money, "$ from the 'change box!'")
            exit()

    for key, value in brand.items():
        if brand1 == key:
            print('You have selected:', value[0], 'it will cost you: $', value[1], 'per kg')
            price = int(input('How many kilograms? : '))
            price1 += price * float(value[1])  # Update price1 with the new purchase
            print("That would be $", price1)

            while True:
                action = input("[S] to shop more, [Q] to Proceed to checkout: ").upper()

                if action == 'S':
                    brand1 = input('Select Code:')
                    brand1 = brand1.upper()

                    while brand1 not in brand:
                        print('Invalid Code')
                        brand1 = input("Please enter a valid code or [Q] to quit:")
                        if brand1.upper() == 'Q':
                            print("Thank you, have a great day!")
                            print("Please get your remaining balance of $", money, "from the 'change box!'")
                            exit()

                    for key, value in brand.items():
                        if brand1 == key:
                            print('You have selected:', value[0], 'it will cost you: $', value[1], 'per kg')
                            price = int(input('How many kilograms? : '))
                            price1 += price * float(value[1])  # Update price1 with the new purchase
                            print("That would be $", price1)

                elif action == 'Q':
                    if money - price1 < 0:
                        print("Insufficient funds! Please add more money or remove items from the cart.")
                        continue  # Continue the loop to allow user to add more money or remove items
                    else:
                        print('Thank you, have a great day!')
                        money -= price1
                        print("Please get your remaining balance of $", money, "from the change box!")

                        # Display Receipt
                        print("\n--------------------RECEIPT----------------------")
                        for item in cart:
                            print(f"{item[0]} - {item[1]} kg - ${item[2]}")
                        print(f"               -{time.strftime('%D:%M:%Y')}               ")
                        print("Total: $", price1, )
                        print("Remaining Balance: $", money, "                     ")
                        print("-------------------------------------------------")

                        exit()
