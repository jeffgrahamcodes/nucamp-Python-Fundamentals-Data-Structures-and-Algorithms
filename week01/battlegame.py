# Declare three variables with the following names:
# wizard, elf, human
# As you do, set each of their values to a String with their display name, which is their name with the first letter capitalized.
# Example: wizard = "Wizard"
wizard = "Wizard"
elf = "Elf"
human = "Human"

while True:
        # Declare three variables, set to Integer values that indicate the hp of each character.
    # The hp of a wizard is 70
    # The hp of an elf is 100
    # The hp of a human is 150
    # Example: wizard_hp = 70
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150

    # Declare three more variables having Integer values that indicate the damage of each character.
    # The damage of a Wizard is 150
    # The damage of an Elf is 100
    # The damage of a Human is 20
    # Example: wizard_damage = 150
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20

    # Also declare two variables that set the hp and damage for the Dragon - 300 hp and 50 damage.
    # Example: dragon_hp = 300
    dragon_hp = 300
    dragon_damage = 50

    # Show the player a list of options to choose from, using the print() function.
    # Use the input() function to prompt the user with the String: "Choose your character: ".
    # Assign the value returned from the input function to a variable named character.
    # print("1) Wizard")
    # print("2) Elf")
    # print("3) Human")
    # character = input("Choose your character: ")

    # Wrap all the code you created in Task 2 in an infinite while loop that uses the True condition.
    # Inside the while loop, write a sequence of three if statements to handle the three options.
    # In the body for each if statement:

    # Declare a variable named character and set its value.
    # Then, declare two variables named my_hp and my_damage.

    # character = wizard
    # my_hp = wizard_hp
    # my_damage = wizard_damage

    # End the body for each of these if statements with a break statement.
    # Print "Unknown character" if the input is not 1, 2, or 3.
    # ***in bonus work, something(s) have to be rest***
    while True:
        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        option = input("Choose your character: ")
        
        if option == "1":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if option == "2":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if option == "3":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        # Please improve messages if needed
        print("Unknown character")

    print(f"You have chosen the character: {character}")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_damage}\n")


    # Begin a second infinite while loop, using the True condition.
    # Reduce the value of dragon_hp by the value of my_damage:

    # dragon_hp = dragon_hp - my_damage

    # Printing Battle Progress:  Use print statements to show battle progress.

    # print("The", character, "damaged the Dragon!")

    # Handling Dragon's Turn:  Decrease the value of the character's hitpoints (my_hp) by the value of dragon_damage.  Use a print statement to update battle progress.
    # Finishing the Battle: If the dragon's or character's hitpoints are zero or below, print "The Dragon has lost the battle" or "The ", character, "has lost the battle" and break out of the loop.
    while True:
        dragon_hp = dragon_hp - my_damage
        print(f"The {character} damaged the Dragon!")
        print(f"The Dragon's hit points are now: {dragon_hp}\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle!")
            break

        print(f"The Dragon strikes back at the {character}")
        my_hp = my_hp - dragon_damage
        print(f"The {character}'s hit points are now: {my_hp}\n  ")
        if my_hp <= 0:
            print(f"The {character} has lost the battle!")
            break


    play_again = input("Play again? type y for yes or n for no: ")

    while play_again.lower() != 'y' and play_again.lower() != 'n':
        play_again = input("Play again? type y for yes or n for no: ")
    
    if play_again.lower() == "y":
        print("Once more unto the breach, dear friends, once more!\n")
    if play_again.lower() == "n":
        print("The greatest victory is that which requires no battle.\n")
        break






