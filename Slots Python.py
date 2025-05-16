import random
import time
import sys
import os
from PIL import Image
import winsound
import cv2
import pygame
import moviepy as mp

pygame.mixer.init()


balance = 200
symbols = ["💎","7️⃣","🔔","💗","🍓","🍒","🍋","🍇",]
winnings = 0 
jackpot = 650
newjackpot = 250
payouts = {
    "💎": {"2": 2},
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


def delayed_text(s):   #https://www.youtube.com/watch?v=2h8e0tXHfk0  edited to fit with my code and make it easier to use
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()    
        time.sleep(0.05)



def symbolwait(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()    
        time.sleep(0.5)



delayed_text("Welcome to 🎰Slots🎰\n")
time. sleep(0.5)
delayed_text(f'Current balance: ${balance}\n')
delayed_text("To win the jackpot you will need to get 3 💎 in a whole row\n")
delayed_text("Every time you bet it will take half of what you bet and put it into the jackpot pool\n")

while True:

    while True:
        delayed_text(f"The jackpot is currently ${jackpot}\n")
        try:
            betamount = int(input("Enter your bet: "))

            if betamount > balance:
                    delayed_text("Not Enough Balance, You Poor. Please lower your bet\n") #Will keep repeating until user gives a bet that is within their balance
                    time. sleep(1)

            elif betamount < 0:    
                    delayed_text("Please enter a valid bet\n")
                    time. sleep(1)

            elif betamount < 10:    
                    delayed_text("Please input a bet above 10$\n")
                    time. sleep(1)
                
                
            else:
                break

        except ValueError:
            delayed_text("Please enter a valid bet\n")


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
            balance = + balance + jackpot #jackpot WOULD NOT MESS WITH THIS AREA, PAIN IN THE ASS TO TRY DO IT ANY OTHER WAY OR TRY CHANGE ONE LITTLE THING     
            delayed_text("💎JACKPOT!!!💎 You hit 3 diamonds!\n")
            jackpot = newjackpot  # Reset jackpot to 250$
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

        balance = balance + winnings 
        balance = balance - betamount
        jackpot = jackpot + (balance / 2)

    else:
        winnings = 0
        delayed_text("No matches. You win nothing this time.\n")
        balance = balance - betamount
        jackpot = jackpot + (balance / 2)
        
        
    if balance <= 0:
    
        video_path = "LossVideo.mp4"
        if os.path.exists(video_path):
            video_clip = mp.VideoFileClip(video_path)
            audio_path = "LossVideo_audio.wav"
            video_clip.audio.write_audiofile(audio_path, codec='pcm_s16le')
            
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            
            cap = cv2.VideoCapture(video_path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_time = 1 / fps
            
            start_time = time.time()
            
            cv2.namedWindow("Loss Video", cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("Loss Video", cv2.WND_PROP_TOPMOST, 1)  # Bring the window to the front
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                elapsed_time = time.time() - start_time
                
                if elapsed_time >= frame_time * 0.98:
                    cv2.imshow('Loss Video', frame)
                    start_time = time.time()
                    time.sleep(frame_time * 0.88)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
            cap.release()
            cv2.destroyAllWindows()

            delayed_text("You are now poor and owe the cartel money")
        exit()

    else:
        delayed_text(f"Your balance is now ${balance}\n")
        print()

        # Only accept "yes" or "no" and repeats after wrong asnwer
        while True:
            play_again = input("Spin again? (yes/no): ").strip().lower()
            if play_again in ["yes", "no", "y", "n"]:
                break
            else:
                print("Please type 'yes' or 'no'")

        if play_again == "no":
            im = Image.open(r"KeepGoing.jpg")
            im.show()
            break
            

            
            #FIX PAYOUTS, if slots 1-2 match it does not displaying winning but slot 2-3 do (FIXED)
