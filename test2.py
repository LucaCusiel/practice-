import random
import time
import sys
import os

balance = 100
symbols = ["💎","7️⃣","🔔","💗","🍓","🍒","🍋","🍇",]
winnings = 0 
jackpot = 350
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


# Spin the slot (allows repeats of the symbol)
random_items = random.choices(symbols, k=3)

print("*******")
for item in random_items:
    print(item, end=" ", flush=True)
    time.sleep(0.5)
print("\n*******")



if random_items[0] == random_items[1] == random_items[2]:
    match_symbol = random_items[0]
    if match_symbol == "💎":
        winnings = 350 #jackpot
        delayed_text("💎JACKPOT!!!💎 You hit 3 diamonds!\n")
    else:
            multiplier = payouts[match_symbol]["3"]
            winnings = int(betamount * multiplier)
            delayed_text(f"3x {match_symbol}! You win ${winnings}!\n")
elif (random_items[0] == random_items[1] or 
      random_items[0] == random_items[2] or 
      random_items[1] == random_items[2]):

    if random_items[0] == random_items[1] or random_items[0] == random_items[2]:
        match_symbol = random_items[0]
    else:
        match_symbol = random_items[1]

    multiplier = payouts[match_symbol]["2"]
    winnings = int(betamount * multiplier)
    delayed_text(f"2x {match_symbol}! You win ${winnings}!\n")

else:
    winnings = 0
    delayed_text("No matches. You win nothing this time.\n")



    
    #FIX PAYOUTS, if slots 1-2 match it does not displaying winning but slot 2-3 do (FIXED)
