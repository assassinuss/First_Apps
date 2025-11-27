import os
import time
from pathlib import Path

def star():
    print("Loading Screen: Star")
    for i in range(100):
        for j in range(5):
            for k in range(5):
                print(" " * (4 - j) + "*" * (2 * j + 1))
                time.sleep(0.1)


def point():
    pass

def xmas():
    pass

def zap():
    pass

def load(selection):
    script_folder = Path(__file__).parent
    filename = script_folder / f"{selection}.txt"

    content = filename.read_text(encoding="utf8")
    frames = [f.strip() for f in content.split("motherfucker") if f.strip()]

    for _ in range(10):
        for frame in frames:
            os.system('cls')
            print(frame)
            time.sleep(0.75)

def menu():
    selection = 0
    options = [1, 2, 3, 4]
    while selection not in options:
        os.system('cls')
        selection= int(input("Select which loading screen to display:\n1. Star Loading Screen\n2. Points Loading Screen\n3. Xmas Loading Screen\n4.There is too much ASCII porn!!\n"))
    
    os.system('cls')
    print ("oki doki, you selected option ", selection)
    time.sleep(3)

    load(selection)
    


menu()