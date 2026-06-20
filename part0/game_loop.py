#!/usr/bin/env python3

rooms = [
    {
        "id": 0,
        "description": "Well seems like a good stinky room, lots of dripping liquid",
        "exits": {"east": 1},
    },
    {
        "id": 1,
        "description": "Cant see shi here, i dont have a lamp either",
        "exits": {"west": 0, "east": 2},
    },
    {
        "id": 2,
        "description": "I think i landed in the toilets, fml",
        "exits": {"west": 1, "north": 3},
    },
    {
        "id": 3,
        "description": "Its freezing here goddamnit, who forgot to close the fridge?",
        "exits": {"south": 2, "east": 4},
    },
]
current_room_index = 0


def game_loop():
    running = True
    current_room_index = 0

    while running:
        current_room = rooms[current_room_index]
        print("\n" + current_room["description"])
        print(f"Exits: {', '.join(current_room['exits'])}")
        print("[M] Move   [Q] Quit")

        choice = input(">").strip().lower()

        if choice == "q":
            print("You coward, farewell")
            running = False
        elif choice == "m":
            direction = input("Where to? (north, south, west, east)\n> ")
            if direction in current_room["exits"]:
                current_room_index = current_room["exits"][direction]
                print(f"You move {direction}")
            else:
                print(f"There is no exit to the {direction}.")
        else:
            print("Cant even chose correctly between directions...")


if __name__ == "__main__":
    game_loop()