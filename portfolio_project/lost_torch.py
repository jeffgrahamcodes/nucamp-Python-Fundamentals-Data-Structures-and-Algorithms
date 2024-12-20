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


class Room:
    def __init__(self, description, items=None, exits=None):
        self.description = description
        self.items = items if items else []
        self.exits = exits if exits else {}

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_exit(self, direction):
        return self.exits.get(direction)


rooms = {
    "Entrance Hall": Room(
        description="You stand in a dimly lit hall. The floor is dusty and a single torch flickers on the wall. There's a door to the north.",
        items=[],
        exits={"north": "Treasure Room"}
    ),
    "Treasure Room": Room(
        description="The room is small and cramped. A chest rests in the corner. A faint glow comes from inside it.",
        items=["treasure"],
        exits={
            "south": "Entrance Hall",
            "east": "Exit"
        }
    ),
    "Exit": Room(
        description="A narrow corridor leads to a heavy wooden door. Beyond it, you see daylight. This must be the way out!",
        items=[],
        exits={"west": "Treasure Room"}
    )
}

player = Player('Entrance Hall')


def move_player(direction):
    current_room = rooms[player.current_room]
    new_room_name = current_room.get_exit(direction)

    if not new_room_name:
        print('Cannot go that way\n')
        return False

    # Check if trying to enter exit room without treasure
    if new_room_name == "Exit" and not player.has_item('treasure'):
        print("The exit is locked! You need the treasure to leave.\n")
        return False

    player.move(new_room_name)

    if player.current_room == 'Exit':
        print(rooms[player.current_room].description)
        return True

    print(f'You enter the {player.current_room}\n')
    return False


def show_room_description():
    print(rooms[player.current_room].description + '\n')


def show_inventory():
    if player.inventory:
        print("You have the following item(s):")
        for i in player.inventory:
            print(i)
        print()
    else:
        print("Your inventory is empty.\n")


def show_room_items():
    current_room = rooms[player.current_room]
    if current_room.items:
        print('You see the following item(s) in the room:')
        for item in current_room.items:
            print(item)
        print()
    else:
        print('The room is empty.\n')


def pick_up_item():
    current_room = rooms[player.current_room]
    if current_room.items:
        item = current_room.items.pop()
        player.pick_up_item(item)
        print(f'You pick up the {item} and add it to your inventory.\n')
    else:
        print('There is nothing to pick up here.\n')


def reset_game():
    # Reset player position and inventory
    player.current_room = 'Entrance Hall'
    player.inventory = []
    # Reset the treasure in the Treasure Room if you want a fresh start
    rooms["Treasure Room"].items = ["treasure"]


while True:
    # Initialize reached_exit for each loop iteration
    reached_exit = False

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
        reached_exit = move_player('north')
    elif option == 'S':
        reached_exit = move_player('south')
    elif option == 'E':
        reached_exit = move_player('east')
    elif option == 'W':
        reached_exit = move_player('west')
    else:
        print("Invalid choice. Please try again.\n")
        continue

    # Check if the player reached the exit and has the treasure
    if reached_exit:
        choice = input(
            "You have escaped with the treasure! Play again? (Y/N): ").upper().strip()
        if choice == 'Y':
            reset_game()
        else:
            print("Thanks for playing!")
            break
