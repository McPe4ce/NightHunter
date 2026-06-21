#!/usr/bin/env python3
import random
import time


print("========NIGHTHUNTER========")
time.sleep(1)
print("Welcome in the shadows, will you survive?")
time.sleep(1)


while(1):
    name = input("Let us know how the abyss should call you: ")
    time.sleep(1)
    print(f"Thats quite bad, wouldnt have wanted my mama to call me {name}")
    time.sleep(1)

    classes = {"1": "As a Warrior, fighting for goth chicks",
                "2": "As a Mage, virgin until your last breath",
                "3": "As a Rogue, lost in Texas",
                "4": "As a Cleric, protector of faith"
                }
    print("Pick your Class:")
    for key, value in classes.items():
        print(f"[{key}]: {value}")
        time.sleep(1)
    
    try:
        choice = int(input("Class: "))
            
        if choice == 1:
            da_class = "Warrior"
            time.sleep(1)
            print("May the goths be with you, Warrior")
        
        if choice == 2:
            da_class = "Mage"
            time.sleep(1)
            print("Losing your virginity would mean you lost something. But you never lose, Mage.")
        
        if choice == 3:
            da_class = "Rogue"
            time.sleep(1)
            print("Next step Vegas? Lots of money there, Rogue")
        
        if choice == 4:
            da_class = "Cleric"
            time.sleep(1)
            print("Who the hell wants to chose those bald bustards")
        
        if choice not in range(1,5):
            print("What cant read numbers from 1 to 4")
            continue
    except ValueError:
        print("Bro cant read numbers from 1 to 4")
        continue
    
    base_health = {"Warrior": 100, "Mage": 70, "Rogue": 80, "Cleric": 90}

    hero = {
            "name": name,
            "class": da_class,
            "health": base_health[da_class],
            "max_health": base_health[da_class],
            "gold": 0,
        }
    print(f"\n{hero['name']} the {hero['class'].capitalize()} enters the dungeon...\n")
    break


rooms = [
    {
        "id": 0,
        "description": "Well seems like a good stinky room, lots of dripping liquid",
        "exits": {"east": 1},
        "monster": None,
    },
    {
        "id": 1,
        "description": "Cant see shi here, i dont have a lamp either",
        "exits": {"west": 0, "east": 2},
        "monster": {"name": "Goblin", "health": 15, "attack": 3, "gold": 5},
    },
    {
        "id": 2,
        "description": "I think i landed in the toilets, fml",
        "exits": {"west": 1, "north": 3},
        "monster": {"name": "Goblin ", "health": 15, "attack": 5, "gold": 5},
    },
    {
        "id": 3,
        "description": "Its freezing here goddamnit, who forgot to close the fridge?",
        "exits": {"south": 2, "east": 4},
        "monster": {"name": "Goblin", "health": 15, "attack": 7, "gold": 5},
    },
]

def show_room(room, hero):
    print("\n" + "=" * 40)
    print(room["description"])
    if room["monster"]:
        m = room["monster"]
        print(f"  Monster: {m['name']}  HP: {m['health']}")
    exits = list(room["exits"].keys())
    print(f"  Exits: {', '.join(exits)}")
    print(f"  {hero['name']}: {hero['health']}/{hero['max_health']} HP  |  Gold: {hero['gold']}")
    print("=" * 40)


def attack(hero, monster):
    base_damage = {"Warrior": 10, "Mage": 12, "Rogue": 9, "Cleric": 7}
    damage = base_damage[hero["class"]] + random.randint(-2, 3)
    damage = max(1, damage)
    monster["health"] -= damage
    print(f"\nYou hit the {monster['name']} for {damage} damage!", end=" ")

    if monster["health"] <= 0:
        print(f"The {monster['name']} is defeated!")
        hero["gold"] += monster["gold"]
        print(f"You earn {monster['gold']} gold. Total: {hero['gold']}")
        return True   # monster dead

    print(f"({monster['health']} HP remaining)")

    # counter-attack
    counter = max(1, monster["attack"] + random.randint(-1, 2))
    hero["health"] -= counter
    print(f"The {monster['name']} strikes back for {counter} damage! ({hero['health']} HP remaining)")
    return False  # monster still alive


current_room_index = 0
running = True

while running and hero["health"] > 0:
    room = rooms[current_room_index]
    show_room(room, hero)

    # build action menu dynamically
    actions = ["[M] Move", "[Q] Quit"]
    if room["monster"]:
        actions.insert(0, "[A] Attack")
    print("  " + "   ".join(actions))

    choice = input("> ").strip().lower()

    if choice == "q":
        print("\nYou retreat from the dungeon.")
        running = False

    elif choice == "a":
        if room["monster"]:
            defeated = attack(hero, room["monster"])
            if defeated:
                room["monster"] = None   # clear the room
        else:
            print("There is nothing to attack here.")

    elif choice == "m":
        if room["monster"]:
            print("You can't run past the monster! Defeat it first.")
        else:
            direction = input("Direction: ").strip().lower()
            if direction in room["exits"]:
                current_room_index = room["exits"][direction]
            else:
                print(f"No exit to the {direction}.")

    else:
        print("Unknown command.")

if hero["health"] <= 0:
    print(f"\n{hero['name']} has fallen. Game over.")
else:
    print(f"\n{hero['name']} escapes with {hero['gold']} gold. Well played.")