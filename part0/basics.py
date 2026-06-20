#!/usr/bin/env python3
import time

def hero_name():
    name = input("Let us know how the abyss should call you: ")
    time.sleep(1)
    print(f"Thats quite bad, wouldnt have wanted my mama to call me {name}")
    return name

def hero_class():
    while(1):
        print("Now, you have the choose from 1 to 4 how you will fight:")
        time.sleep(1)
        print("1: As a Warrior, fighting for goth chicks")
        time.sleep(1)
        print("2: As a Mage, virgin until your last breath")
        time.sleep(1)
        print("3: As a Rogue, lost in Texas")
        time.sleep(1)
        print("4: As a Cleric, protector of faith")
        
        try:
            choice = int(input("Class: "))
                
            if choice == 1:
                da_class = "Warrior"
                time.sleep(1)
                print("May the goths be with you, Warrior")
                return da_class
            
            if choice == 2:
                da_class = "Mage"
                time.sleep(1)
                print("Losing your virginity would mean you lost something. But you never lose, Mage.")
                return da_class
            
            if choice == 3:
                da_class = "Rogue"
                time.sleep(1)
                print("Next step Vegas? Lots of money there, Rogue")
                return da_class
            
            if choice == 4:
                da_class = "Cleric"
                time.sleep(1)
                print("Who the hell wants to chose those bald bustards")
                return da_class
        except ValueError:
            print("Bro cant read numbers from 1 to 4")
            continue

def health(da_class):

    if da_class == "Warrior":
        health = 100
    if da_class == "Mage":
        health = 75
    if da_class == "Rogue":
        health = 80
    if da_class == "Cleric":
        health = 90
    
    return health

def the_status(name, classe, health):
    print(f"Welcome {name}, the {classe} with {health} HP!")

def greetings():
    print("Welcome in the shadows, will you survive?")


if __name__ == "__main__":
    greetings()
    time.sleep(1)
    name = hero_name()
    time.sleep(1)
    classe = hero_class()
    thehealth = health(classe)
    time.sleep(1)
    the_status(name, classe, thehealth)