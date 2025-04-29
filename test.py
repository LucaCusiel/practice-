import random
import time
import sys
import os

balance = 100

def delayed_text(s):   #Taken from https://www.youtube.com/watch?v=2h8e0tXHfk0 and edited to fit with my code and make it easier to use
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()    
        time.sleep(0.05)



try:
    betamount = int(input("Enter your bet: "))
except ValueError:
    print("Please enter a valid bet\n")
if betamount > balance:
        delayed_text("Not Enough Balance, You Poor. Please lower your bet\n") #Will keep repeating until user gives a bet that is within their balance
        time. sleep(1)
elif betamount < 1:    
        delayed_text("Please enter a valid bet\n")
        time. sleep(1)