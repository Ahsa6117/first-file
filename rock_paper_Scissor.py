import random
print("Welcome in rock Paper scissor ")
r={1:"Rock",2:"Paper",3:"Scissor"}

comp=random.choice([r[1],r[3]])
print("my choice is ",comp)

user=int(input("Enter your choice \n1: Rock \n2: Paper \n3: Scissor"))
if user==1:
    user=r[1]
elif user==2:
    user=r[2]
elif user==3:
    user=r[3]
else:
   print("Wrong input")
print("User choice is :",user)  
result=" " 
if (user==comp) :
   result=="draw"
elif (user==r[1]and comp==r[2]  ) or (comp==r[1] and user==r[2]):
   result=r[2]
elif (user==r[2] and comp==r[3]) or (comp==r[2] and user==r[3]):
    result=r[3]
elif (user==r[1] and comp==r[3]) or (comp==r[1] and user ==r[3]):
    result=r[1]
print(f"{user} vs {comp}")
if result=="DRAW":
    print("its a tie")
elif result==user:
    print("User wins")
else:
    print("Computer wins")