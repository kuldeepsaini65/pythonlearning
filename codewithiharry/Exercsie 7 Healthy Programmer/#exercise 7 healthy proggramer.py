from pygame import mixer
from time import time
from datetime import datetime

print()
print("**************************")
print("Programme is Running ")
print("Minimize it And Do Not Close This Programme until PC ShutDown")
print("**************************")
print()


def musicplay(file, stopcmd):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input("To Stop This Alarm Music \nType - STOP:- ").lower()
        if a == stopcmd:
            mixer.music.stop()
            break


def log(msg):
    with open("Programmer.txt", "a") as wtr:
        wtr.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eye = time()
    init_physical = time()
    watersec = 35 * 60
    eyesec = 50 * 60
    physicalsec = 80 * 60

    while True:
        if time() - init_water > watersec:
            print("\n+++++++Water Drinking Time+++++++++ ")
            musicplay("water.mp3", "stop")
            init_water = time()
            log("Water drunk at ")

        elif time() - init_eye > eyesec:
            print("\n******Eyes Exercise Time*******")
            musicplay("eye.mp3", "stop")
            init_eye = time()
            log("Eyes Rest at ")

        elif time() - init_physical > physicalsec:
            print("\n----Physical Exercise Time----")
            musicplay("physical.mp3", "stop")
            init_physical = time()
            log("Physical Exercise Done at ")
