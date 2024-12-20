class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, new_room):
        self.current_room = new_room

    def pick_up_item(self, item):
        self.inventory.append(item)

    def has_item(self, item):
        return item in self.inventory


rooms = {
    "Entrance Hall": {
        "description": "You stand in a dimly lit hall. The floor is dusty and a single torch flickers on the wall. There's a door to the north.",
        "items": [],
        "exits": {
            "north": "Treasure Room"
        }
    },
    "Treasure Room": {
        "description": "The room is small and cramped. A chest rests in the corner. A faint glow comes from inside it.",
        "items": ["treasure"],
        "exits": {
            "south": "Entrance Hall",
            "east": "Exit"
        }
    },
    "Exit": {
        "description": "A narrow corridor leads to a heavy wooden door. Beyond it, you see daylight. This must be the way out!",
        "items": [],
        "exits": {
            "west": "Treasure Room"
        }
    }
}

player = Player('Entrance Hall')


def move_player(direction):
    current = player.current_room
    if direction not in rooms[current]['exits']:
        print('Cannot go that way\n')
        return

    new_room = rooms[current]['exits'][direction]

    # Check if the new room is the Exit and if the player has the treasure
    if new_room == "Exit" and not player.has_item('treasure'):
        print("The exit is locked! You need the treasure to leave.\n")
        return

    player.move(new_room)

    # If the player reaches the Exit, show its description and end the game loop
    if player.current_room == 'Exit':
        print(rooms[player.current_room]['description'])
        # Potentially break out of the loop or return a flag to end game
        return

    print(f'You enter the {player.current_room}\n')


def show_room_description():
    print(rooms[player.current_room]['description'] + '\n')


def show_inventory():
    if player.inventory:
        print("You have the following items:")
        for i in player.inventory:
            print(i)
        print()
    else:
        print("Your inventory is empty.\n")


def show_room_items():
    if rooms[player.current_room]['items']:
        print('You see the following item(s) in the room:')
        for item in rooms[player.current_room]['items']:
            print(item)
        print()
    else:
        print('The room is empty.\n')


def pick_up_item():
    if rooms[player.current_room]['items']:
        item = rooms[player.current_room]['items'].pop()
        player.pick_up_item(item)
        print(f'You pick up the {item} and add it to your inventory.\n')
    else:
        print('There is nothing to pick up here.\n')


while True:
    # Display options
    print("1) Get room description")
    print("2) Check Inventory")
    print("3) Check Room")
    print("4) Pickup Item")
    print("N) Move North")
    print("S) Move South")
    print("E) Move East")
    print("W) Move West")

    option = input("What would you like to do? ").upper().strip()
    print()

    if option == "1":
        show_room_description()
    elif option == "2":
        show_inventory()
    elif option == "3":
        show_room_items()
    elif option == "4":
        pick_up_item()
    elif option == 'N':
        move_player('north')
    elif option == 'S':
        move_player('south')
    elif option == 'E':
        move_player('east')
    elif option == 'W':
        move_player('west')
    else:
        print("Invalid choice. Please try again.\n")
