from PIL import Image

answer = input("Do you want to keep gambling: ")

if answer == "yes":
    print("Horay")
else:
    im = Image.open(r"KeepGoing.jpg")
    im.show()
    