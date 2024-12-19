class Player:
    def __init__(self, start_room):
        # The room where the player begins the game
        self.current_room = start_room
        # A list to hold items the player picks up
        self.inventory = []

    def move(self, new_room):
        # Update the player’s current room
        self.current_room = new_room

    def pick_up_item(self, item):
        # Add an item to the player’s inventory
        self.inventory.append(item)

    def has_item(self, item):
        # Check if the player has a certain item
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

while True:
    print("1) Get room description")
    print("2) Check Inventory")
    print("3) Check Room")
    print("4) Pickup Item")
    print("N) Move North")
    print("S) Move South")
    print("E) Move East")
    print("W) Move West")
    option = input("What would do want to do: ")

    if option == "1":
        print(rooms[player.current_room]['description'])
    if option == "2":
        if player.inventory:
            print(len(player.inventory))
        else:
            print("empty")
    if option == "3":
        if rooms[player.current_room]['items']:
            print('There are items')
        else:
            print('room empty')
    if option == 'N':
        if 'north' in rooms[player.current_room]['exits']:
            print(rooms[player.current_room]['exits']['north'])
        else:
            print('Cannot go that way')
    if option == 'S':
        if 'south' in rooms[player.current_room]['exits']:
            print(rooms[player.current_room]['exits']['north'])
        else:
            print('Cannot go that way')
    if option == 'E':
        if 'east' in rooms[player.current_room]['exits']:
            print(rooms[player.current_room]['exits']['east'])
        else:
            print('Cannot go that way')
    if option == 'W':
        if 'west' in rooms[player.current_room]['exits']:
            print(rooms[player.current_room]['exits']['west'])
        else:
            print('Cannot go that way')
