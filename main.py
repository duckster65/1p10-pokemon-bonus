import time
import random
import csv
import math
from Pokemon_class import Pokemon

team = []

def skewed_random_number(min_value=1, max_value=100):

    skewed_float = random.random() ** 2

    skewed_int = round(skewed_float * (max_value - min_value) + min_value)

    return skewed_int

def retreive_pokemon(target_pokemon, level, index):
    csv_file = 'pokemon.csv'
    with open(csv_file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)

        line_num = 1

        if index == 999:
            for row in csv_reader:
                if row[1] == target_pokemon:
                    #HP = 0.020 * math.sqrt(level) * int(row[5])

                    EV = 0

                    for i in range(5):
                        EV += int(row[6 + i])

                    HP = math.floor(0.01 * (2 * int(row[5]) + 6 + math.floor(0.25 * EV)) * level) + level + 10

                    stats = [int(row[6]), int(row[7]), int(row[10])]

                    temp_pokemon = Pokemon(target_pokemon, row[2], HP, stats)
                    return temp_pokemon
                
                line_num += 1
        
        else:
            iteration = 0
            for row in csv_reader:
                if iteration == index:
                    EV = 0
                    for i in range(5):
                        EV += int(row[6+i])
                    
                    HP = math.floor(0.01 * (2 * int(row[5]) + 6 + math.floor(0.25 * EV)) * level) + level + 10

                    stats = [int(row[6]), int(row[7]), int(row[10])]

                    temp_pokemon = Pokemon(row[1], row[2], HP, stats)
                    return temp_pokemon
                
                iteration += 1

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
        alive = 0
         #Check how many pokemon on the players team are alive
        for i in range(len(team)):
            if int(team[i].HP) > 0:
                alive += 1

        if alive > 0:
            print("\nYou have chosen to fight Brock!")
            leaders_team.append(retreive_pokemon("Geodude", 12, 999))
            leaders_team.append(retreive_pokemon("Onix", 14, 999))

            leader_pokemon_num = len(leaders_team)

            leader_pokemon = leaders_team[random.randint(0, leader_pokemon_num - 1)]

            current_pokemon = None

            while True: 
                print("\n")
                for i in range(len(team)):
                    pokemon = team[i]
                    print((str((i+1))+ "."), pokemon.name, str(pokemon.HP), "HP")

                choice = int(input("Which pokemon would you like to send out first?: "))
                
                try:
                    current_pokemon = team[choice - 1]
                    break

                except Exception as e:
                    continue

            leader_alive = len(leaders_team)


            while True:

                choice = input("\nWould you like to send out a new pokemon or attack (1 or 2): ")

                if choice == "1":

                    while True:
                        for i in range(len(team)):
                            pokemon = team[i]
                            print((str((i+1))+ "."), pokemon.name, str(pokemon.HP), "HP")
                        choice = int(input("\n\nWhich pokemon would you like to send out?: "))
                        try: 
                            if team[(choice - 1)].HP > 0:
                                current_pokemon = team[(choice - 1)]
                                break
                        except Exception as e:
                            print(e)
                            continue
                else:
                    ##Player turn
                    player_attack = current_pokemon.stats[0]/2

                    print("All pokemon have one attack, tackle, determined by the attack stat of the pokemon")
                    time.sleep(1)
                    print("\nYou use tackle doing", player_attack, "damage to", leader_pokemon.name)
                   
                    if leader_pokemon.HP - player_attack <= 0:
                        print("You knocked out the opponent's pokemon!")
                        leader_pokemon.HP = 0
                        leader_alive = leader_alive - 1

                        if leader_alive == 0:
                            print("You won!")
                            break

                        else:
                            new_pokemon = leaders_team[random.randint(0, leader_pokemon_num - 1)]
                            while new_pokemon == leader_pokemon or new_pokemon.HP == 0:
                                new_pokemon = leaders_team[random.randint(0, leader_pokemon_num - 1)]
                            
                            leader_pokemon = new_pokemon

                        continue

                    else:
                        leader_pokemon.HP = leader_pokemon.HP - player_attack
                        print(leader_pokemon.name, "has", leader_pokemon.HP, "HP remaining")
                    
                    ##Opponent Turn

                    if leader_pokemon.HP < (leader_pokemon.maxHP * 0.2) and (len(leaders_team) - leader_alive) > 1:
                        random_number = random.choice([1, 2])

                        if random_number == 1:

                            new_pokemon = leaders_team[random.randint(0, leader_pokemon_num - 1)]
                            while new_pokemon == leader_pokemon or new_pokemon.HP == 0:
                                new_pokemon = leaders_team[random.randint(0, leader_pokemon_num - 1)]
                            
                            leader_pokemon = new_pokemon
                            continue
                    

                    opponent_attack = leader_pokemon.stats[0]/2

                    print("\nThe gym leader uses tackle doing", opponent_attack, "damage to", current_pokemon.name)
                    if current_pokemon.HP - opponent_attack <= 0:
                        print("Your pokemon was knocked out")
                        current_pokemon.HP = 0
                        alive -= 1
                        if alive == 0:
                            print("You lost, you have no remaning pokemon")
                            break
                        while True:
                            print("\nSelect a new pokemon to send out: ")
                            for i in range(len(team)):
                                pokemon = team[i]
                                print((str((i+1))+ "."), pokemon.name, str(pokemon.HP), "HP")
                            choice = int(input("\n\nWhich pokemon would you like to send out?: "))
                            try: 
                                if team[(choice - 1)].HP > 0:
                                    current_pokemon = team[(choice - 1)]
                                    break
                            except Exception as e:
                                continue

                        continue

                    else:
                        current_pokemon.HP = current_pokemon.HP - opponent_attack
                        print(current_pokemon.name, "has", current_pokemon.HP, "HP remaining")



                    

        else:
            print("You have no pokemon alive!")


            print("test")

def check_pokemon():
    print("Here is your current team: ")
    for i in range(len(team)):
        pokemon = team[i]
        print((str((i+1))+ "."), pokemon.name, str(pokemon.HP), "HP")
    
    choice = input("Would you like to revive your team? (y or n): ")
    if choice == "y":
        for pokemon in team:
            pokemon.HP = pokemon.maxHP

def wild_pokemon():
    global team
    pokemon_found = [["Grass", "Bug", "Normal", "Ground", "Fighting"], ["Dragon", "Water", "Ice"], ["Normal", "Fire", "Ground", "Dark", "Rock", "Dark", "Flying"]]
    region = input("Select a region to find pokemon in: \n1. Grassland\n2. Sea\n3. Mountains")

    pokemon_index = random.randint(1, 801)
    print("index is", pokemon_index)
    level = skewed_random_number()
    pokemon = retreive_pokemon("", level, pokemon_index)

    time.sleep(1)

    print("You encounter a wild", pokemon.name, "at level", level)

    choice = input("Would you like to try to catch it? (y or n)")
    if choice == "y":
        random_number = random.choice([1, 2])

        if random_number == 1:
            print("\nCongratulations you caught", pokemon.name, "it has been added to your team!")
            team.append(pokemon)
        else:
            print("\nThe pokemon got away...")
        
        time.sleep(1)

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
        pokemon = retreive_pokemon("Charmander", 5, 999)
        team.append(pokemon)
    
    elif choice == "2":
        print("You selected Bulbasaur!")
        pokemon = retreive_pokemon("Bulbasaur", 5, 999)
        team.append(pokemon)

    elif choice == "3":
        print("You selected Squirtle!")
        pokemon = retreive_pokemon("Squirtle", 5, 999)
        team.append(pokemon)

    print("\nYou are now ready to set off on your journey!")
    print("You set off into the woods around the town!")
    
    time.sleep(1)    

    while True:

        while True:
            print("What would you like to do now?")
            choice = input("\n\n1. Fight a gym leader\n2. Catch new pokemon\n3. Check your team and revive them\n4. Exit the game\n")

            if choice == "1":
                gym_battle()
            if choice == "2":
                wild_pokemon()
            if choice == "3":
                check_pokemon()
            if choice == "4":
                exit()


main()