import random
import time

balance = 100

print(f'Balance: ${balance}')


while True:
    bet = int(input("How much do you wanna bet: "))
    if bet > balance:
        print("Not Enough Balance, You Poor. Please lower your bet") #Will keep repeating until user gives a bet that is within their balance
        time. sleep(1)
    else:
        break

print("Test")