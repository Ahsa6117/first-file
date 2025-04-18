
print("Welcome to the Mad Libs Game!")
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
food = input("Enter a type of food: ")
s = f"""
One day, {name} went to {place}. 
There, they saw a {adjective} {animal} that was trying to {verb}.
Surprised, {name} decided to offer it some {food}, and they became best friends!
"""
print("Here is your Mad Libs story:")
print(s)