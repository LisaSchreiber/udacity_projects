import time
import random
# import emojis


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("Welcome!")
    role = ["an emperor", "a knight", "an outlaw"]
    # print_pause(emoji.emojize(':raised_hands:'))
    print_pause("You live in a mystic and ancient world and you"
                " are " + random.choice(role) + ".")
    print_pause("You find yourself wandering around, carrying a small knife.")
    print_pause("The knife makes you feel safe, but who knows, if it actually"
                " has the power to defend you?")
    print_pause("While you wander around, you notice a cave,"
                " a house and a hill.\n")


def cave(weapons):
    print_pause("You peek into the cave and enter carefully.")
    # print_pause(emoji.emojize(':black_medium_small_square:'))
    if 'sword' in weapons:
        print_pause("You already got everything that you could"
                    " find in the cave.")
        print_pause("There is nothing more to do here."
                    " Go outside and defend your empire.")
    else:
        print_pause("You see something. What might it be?")
        print_pause("Ohh! This is amazing.")
        print_pause("You found a shining sword and take it with you.")
        print_pause("This seems more reliable than your knife and might"
                    " proof worthy in the future.")
        weapons.append("sword")
    print_pause("You go back outside.")
    explore(weapons)


def hill(weapons):
    print_pause("You decided to check out the hill.")
    print_pause("However, first you need to hike.")
    # print_pause(emoji.emojize(':mount_fuji:'))
    print_pause("When you reach the top of the hill, you see:")
    if 'gold' in weapons:
        print_pause("Nothing. Apperantly there is nothing more to get here.")
        print_pause("This was a lot of energy for nothing.")
    else:
        print_pause("A shining stone! What is this? Wow!")
        print_pause("This is gold!")
        print_pause("You go and collect it. You find a carving saying:")
        print_pause("'Take care of this treasure.")
        print_pause("It helps to fight evil creatures.'")
        weapons.append("gold")
    print_pause("You decide to go down and continue to follow your calling.\n")
    explore(weapons)


def house(weapons):
    print_pause("Oh, you chose to enter the house. What happens now?")
    # print_pause(emoji.emojize(':house:'))
    print_pause("You already had a funny feeling to enter,"
                " but now you see why:")
    monster = ["dragon", "troll", "zombie"]
    print_pause("There is a " + random.choice(monster) + "!\n")
    strategy = input("Do you fight (enter '1') or flight (enter '2')?\n")
    if '2' == strategy:
        print_pause("You run and esacpe.\n")
        explore(weapons)
    elif '1' == strategy:
        if 'sword' in weapons and 'gold' in weapons:
            print_pause("You fight. The gold protects you and you can"
                        " use your sword to fight.")
            print_pause("Congratulations!! You won and protect your empire!\n")
            # print_pause(emoji.emojize(':confetti_ball:'))
        else:
            print_pause("Oh no! You lost.")
            (" You need to collect better weapons next time.\n")
            # print_pause(emoji.emojize(':sob:'))
        play_again()
    else:
        print_pause("This is no valid choice. Please enter '1' or '2'.")
        house(weapons)


def play_again():
    play = input("Would you like to play again?"
                 " Enter 'yes' to play, otherwise enter 'no'.\n").lower()
    if 'yes' == play:
        play_game()
    elif 'no' == play:
        print_pause("Thank you. Good Bye!")
    else:
        print_pause("I cannot understand. Please try again.\n")
        play_again()


def explore(weapons):
    option = input("Where yould you like to go now?"
                   " Enter 'house', 'hill' or 'cave'?\n").lower()
    if option == 'cave':
        cave(weapons)
    elif option == 'hill':
        hill(weapons)
    elif option == 'house':
        house(weapons)
    else:
        print_pause("You cannot go there.\n")
        explore(weapons)


def play_game():
    weapons = []
    intro()
    explore(weapons)


play_game()
