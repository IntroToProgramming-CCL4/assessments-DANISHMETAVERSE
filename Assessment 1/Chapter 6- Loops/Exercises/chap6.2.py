#ask users their age
while True:
    age = int(input('Enter age:')) 
    if age <=3:
        print("Tickets are free!") #If a person is under the age of 3, the ticket is free
    elif age >=3 and age <=12:
        print("Tickets are 10$!") #they are between 3 and 12, the ticket is $10
    elif age >12:
        print("Tickets are 15$!") #and if they are over age 12, the ticket is $15.
