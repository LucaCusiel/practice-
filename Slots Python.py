import random
import time

balance = 100
symbols = ["💎","7️⃣","🔔","💗","🍓","🍒","🍋","🍇",]

firstwheel = None
secondwheel = None
thridwheel = None


print("Welcome to 🎰Slots🎰")
time. sleep(0.5)
print(f'your balance is currently: ${balance}')
print("To win the jackpot you will need to get 3 diamonds in a whole row")
print("The jackpot is currently $350")
print("Every time you bet it will tae half of what you bet and put it into the jackpot pool")

while True:
    betamount = int(input("How much do you wanna bet: "))
    if betamount > balance:
        print("Not Enough Balance, You Poor. Please lower your bet") #Will keep repeating until user gives a bet that is within their balance
        time. sleep(1)
    elif betamount < 1:    
        print("Please enter a valid bet")
        time. sleep(1)
    else:
        break

print("Test")