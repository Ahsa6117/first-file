import random
import string
def PIN_generator():
    length=int(input("enter a length of password which you want to generate"))
    ch=string.digits
    pas=''.join(random.choice(ch) for i in range(length))
    print(pas)
PIN_generator()