import random
def guess_number_game_comp():
    print("Welcome to guess number game ")
    y=random.randint(1,10)
    print("enter a number from  1-10")
    attempts=0
    while True:
        u=int(input("enter a number "))
      
        attempts+=1
        try:
            if u==y:
                print(f"guess is correct in {attempts} ")
                break
            else:
                print("invalid number , please try again")
        except ValueError:
            print("your input is invalid")
        
guess_number_game_comp()
        
        
 