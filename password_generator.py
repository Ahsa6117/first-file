import random
import string
def password_generator():
    length=int(input("enter a length of password which you want to generate"))
    ch=string.ascii_letters+string.ascii_lowercase+string.digits+string.whitespace+string.ascii_uppercase
    pas=''.join(random.choice(ch) for i in range(length))
    print(pas)
password_generator()