import random
def user():
    print("Welcome to guess number game")
    y=random.randint(1,6)
    print("Guess a number between 1-6")
    attempt=0
    
    while True:
       try: 
        u=int(input("Enter a guess number between 1 to 6"))
        attempt+=1
        y=random.randint(1,6)
        print(f"my guess is {u}")
        if 1<=u<=6:
         if u==y:
            print(f"Congratulations , Your guess is correct in {attempt} attempt")
            break
         else:
            print("Guess is not correct, please try again")
        else:
           print("enter a guess number with in the range given numbers")
        print(f"User guess is {y}")
       except ValueError:
        print("Enter a valid integer")     

user()