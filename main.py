#!/usr/bin/env python3
import pyautogui
from time import sleep
from random import seed, randint

def get_message(i):
    m = {
        1: "Physik ist super",
        3: "Allgemeine Relativitaetstheorie for the win",
        4: "May mass times acceleration be with you",
        5: "Bloodbath",
        6: "gd",
        7: "Das Haus des Verderbens",
        8: "Trink mal weniger Monster",
        9: "Karl von Chlodwig",
        10: "Mach mal weniger Sport!",
        11: "Auf nach Troscharad!",
        12: "Was ist hier los",
        13: "Moin",
        14: "Du stinkst",
        15: "Tallinn, die Hauptstadt von Estland",
        16: "Visit GD Quant",
    }
    return m[i] if i in m else "Pytob stinkt wie ein verrottender Schildkroeten-Kadaver"

def spam(elements, num, pause):
    for x in range(num + 1):
        for e in elements:
            pyautogui.typewrite(e)
            pyautogui.press("enter")
            sleep(pause)

def random_spam(num, pause):
    for x in range(num + 1):
        for e in get_message(randint(1, 20)):
            pyautogui.typewrite(e)
            pyautogui.press("enter")
            sleep(pause)

seed()

print('Satz (1) / Buchstaben (2)')

spamtype = input()[0]

if spamtype not in '12sbSB':
    print('Please enter a proper spam mode.')
    exit(1)

print("Vorhandener (1) / Eigener (2) Text")
texttype = input()[0]

while texttype not in '12veVE':
    print('Please don\'t enter stupid shit.')
    texttype = input()[0]

if texttype in '2eE':
    print("Gebe deinen Text ein:")
    s = str(input())

print("Sleep time in seconds.")
g = -1
while g < 0:
    print("Es geht nicht schneller als 0:")
    try:
        g = float(input())
    except:
        print("Please enter a valid float.")
        pass

print("Lege die Anzahl des zu versendenden Textes ein")
anz = -1
while anz < 0:
    print("Es geht nicht weniger als 0:")
    try:
        anz = int(input())
    except:
        print("Muss eine ganze Zahl sein")
        pass

# Warten
print("Sie haben 15 Sekunden zeit, den Chat auszuwählen...")
sleep(15)

# Spam
if texttype in '2eE':
    random_spam(anz, g)
else:
    spam([s] if spamtype in '1sS' else s, anz, g)
