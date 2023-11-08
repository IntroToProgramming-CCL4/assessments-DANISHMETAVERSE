# several dictionaries in a list called pets
pets = [
    {"animal": "Dog", "owner": "Danish"}, 
    {"animal": "Cat", "owner": "Bins"},
    {"animal": "Camel", "owner": "Dobi"}, 
    {"animal": "Cow", "owner": "Janel"},]

# 
for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner's Name: {pet['owner']}")
    print()