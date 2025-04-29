import random
import time
import sys
import os

balance = 100
symbols = ["💎","7️⃣","🔔","💗","🍓","🍒","🍋","🍇",]

payouts = {
    "💎": {"2": 1.5, "3": 20},
    "7️⃣": {"2": 1.5, "3": 5},
    "🔔": {"2": 1.5, "3": 3},
    "💗": {"2": 1.5, "3": 2.5},
    "🍓": {"2": 1.45, "3": 1.75},
    "🍒": {"2": 1.35, "3": 1.65},
    "🍋": {"2": 1.2, "3": 1.5},
    "🍇": {"2": 1.2, "3": 1.5},
}


firstwheel = None
secondwheel = None
thridwheel = None


def delayed_text(s):   #Taken from https://www.youtube.com/watch?v=2h8e0tXHfk0 and edited to fit with my code and make it easier to use
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()    
        time.sleep(0.0)



def symbolwait(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()    
        time.sleep(0.5)



delayed_text("Welcome to 🎰Slots🎰\n")
time. sleep(0.5)
delayed_text(f'your balance is currently: ${balance}\n')
delayed_text("To win the jackpot you will need to get 3 diamonds in a whole row\n")
delayed_text("The jackpot is currently $350\n")
delayed_text("Every time you bet it will take half of what you bet and put it into the jackpot pool\n")

while True:
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
    else:
        break

balance = balance - betamount
delayed_text(f"Rolling Slots With A Bet Of ${betamount}\n")
delayed_text(f"Balance: ${balance}\n")

random_items = random.sample(symbols, 3)
time. sleep(0.5)
symbolwait(random_items)