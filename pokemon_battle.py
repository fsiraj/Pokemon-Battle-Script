import time
import sys
import random


def print_pause(string):
    print(string)
    sys.stdout.flush()
    time.sleep(1)


def intro():
    rockTypePokemons = ["Geodude", "Onyx", "Rhyperior", "Groudon", "Regirock"]
    global enemy
    enemy = random.choice(rockTypePokemons)

    print_pause(f"You find yourself facing a wild {enemy}.")
    if enemy == "Groudon":
        print_pause("Groudon is a legendary pokemon.")
        print_pause("You run away for your life.")
        gameover()
    print_pause("You can choose Charmander or Squirtle.")


def pokemon_choice():
    choice = input("Enter 1 to choose Charmander.\n"
                   "Enter 2 to choose Squirtle.\n")
    choices = ['1', '2']
    while choice not in choices:
        choice = input("Invalid input, choose 1 or 2 ")
    return choice


def charmander():
    move = input("To use Blaze press 1.\nTo use Firestorm press 2.\n")
    if move == "1":
        print_pause("You used Blaze.")
        print_pause("It wasn't effective.")
    elif move == "2":
        print_pause("You used Firestorm.")
        print_pause("It wasn't effective.")
    else:
        print_pause("That's not an option. Please choose again.")
        charmander()


def squirtle():
    move = input("To use Hydrojet press 1.\nTo use Tsunaami press 2.\n")
    if move == "1":
        print_pause("You used Hydrojet")
        print_pause("It was super effective!")
    elif move == "2":
        print_pause("You used Tsunaami.")
        print_pause("It was super effective!")
    else:
        print_pause("That's not an option. Please choose again.")
        squirtle()


def foe():
    rocktypeMoves = ["Rock Smash", "Rock Blast", "Stealth Rock", "Accelerock"]
    print_pause(f"{enemy} used {random.choice(rocktypeMoves)}.")


def battle():
    global pokemon
    pokemon = pokemon_choice()
    if pokemon == "1":
        print_pause("You've picked Charmander!")
        charmander()
        foe()
        print_pause("It was super effective.")
        print_pause("Charmander fainted.")
        print_pause("You run away.")
        gameover()

    elif pokemon == "2":
        print_pause("You've picked Squirtle!")
        squirtle()
        print_pause("You win!")
        gameover()

    else:
        print_pause("That isn't a choice")
        battle()


def gameover():
    replay = input("Play again? Y/N\n")
    if replay.lower() == "y":
        pokemonBattle()
    elif replay.lower() == "n":
        sys.exit()
    else:
        print_pause("Not a choice.")
        gameover()


def pokemonBattle():
    intro()
    battle()


pokemonBattle()
