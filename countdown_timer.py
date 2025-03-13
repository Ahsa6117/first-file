import time
def ti(seconds):
    while seconds>0:
        time.sleep(1)
        print(seconds)
        seconds=seconds-1
    print("Times up")
try:
 i=int(input("Entet a time where to start"))
 if i<0:
    print("Incorrect , enter a positive integer")
 else:
  ti(i)
except ValueError:
   print("enter the valid integer")