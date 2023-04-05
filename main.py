import time
import random
import csv
import math
from Pokemon_class import Pokemon

team = []

def retreive_pokemon(target_pokemon, level):
    csv_file = 'pokemon.csv'
    with open(csv_file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)

        line_num = 1

        for row in csv_reader:
            if row[1] == target_pokemon:
                #HP = 0.020 * math.sqrt(level) * int(row[5])

                EV = 0

                for i in range(5):
                    EV += int(row[6 + i])

                HP = math.floor(0.01 * (2 * int(row[5]) + 6 + math.floor(0.25 * EV)) * level) + level + 10

                temp_pokemon = Pokemon(target_pokemon, row[2], HP)
                return temp_pokemon
            
            line_num += 1

def main():

#Possibly add saved games...

    print("Welcome to the pokemon game!")
    choice = input("\nIf you would like to start at the beginning of the game type 1, \nif you would like to start at a specifc stage, type 2: ")
    if choice == "1":
        start()
    elif choice == "2":
        print("To skip into the game select a pokemon roster to use by entering their names and level")
        while True:
            name = input("What pokemon would you like on your team?: ")
            level = input("what level is the pokemon?: ")

def gym_battle():
    global team
    leaders_team = []
    choice = input("Which gym leader do you want to fight:\n1. Brock\n")
    if choice == "1":
        print("\nYou have chosen to fight Brock!")
        leaders_team.append(retreive_pokemon("Geodude", 12))
        leaders_team.append(retreive_pokemon("Onix", 14))

        current_pokemon = ""

        while True: 
            print("\n")
            for i in range(len(team)):
                pokemon = team[i]
                print((str((i+1))+ "."), pokemon.name, str(pokemon.HP), "HP")

            choice = input("Which pokemon would you like to send out first?: ")
            
            try:
                current_pokemon = team[int(choice)]
                break

            except Exception as e:
                continue

        while alive > 0:
            print("test")

def start():
    global team
    time.sleep(1)
    print("\nWelcome to the Kanto region where you will encounter wild pokemon!")
    time.sleep(1)
    print("\nYou start your journey in Pallet Town!")
    time.sleep(1)
    print("\nYou may begin by selecting your starter pokemon:")
    print("1. Charmander (Fire Type)")
    print("2. Bulbasaur (Grass Type)")
    print("3. Squirtle (Water)")
    choice = input("Which one would you like to choose (1-3)\n")
    if choice == "1":
        print("You selected Charmander!")
        pokemon = retreive_pokemon("Charmander", 5)
        team.append(pokemon)
    
    elif choice == "2":
        print("You selected Bulbasaur!")
        pokemon = retreive_pokemon("Bulbasaur", 5)
        team.append(pokemon)

    elif choice == "3":
        print("You selected Squirtle!")
        pokemon = retreive_pokemon("Squirtle", 5)
        team.append(pokemon)

    print("\nYou are now ready to set off on your journey!")
    print("You set off into the woods around the town!")
    
    time.sleep(1)    

    while True:
        print("What would you like to do now?")
        choice = input("\n\n1. Fight a gym leader\n2. Catch new pokemon\n3. Exit the game")

        if choice == "1":
            gym_battle()
        
        if choice == "2":
            wild_pokemon()
        if choice == "3":
            exit()


main()