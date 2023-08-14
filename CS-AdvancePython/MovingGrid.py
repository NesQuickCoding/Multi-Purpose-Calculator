# -*- coding: utf-8 -*-
"""
Grid Movement
"""
from pprint import pprint


def title():
    print("==========================================================")
    print("\t\t\tPokemon Py Version")
    print("==========================================================")
    print("My name is Professor Broke!")
    print("This is the world of Pokemon")
    print("Pokemon are pocket monsters you catch, train, and battle")
    print("But most of all... Pokemon are Friends!")
    print("Before we start, I will need to ask you a few questions:")

def player_creation():
    name = input("Please enter your name trainer!\nName: ")
    gender = input("Please enter your gender trainer\nGender: ")
    nature = input("How would you describe yourself with one word?\nNature: ")
    mysterybox_choice = input("Now I would like you to a pick a Mystery box from 1 to 4\nChoice: ")
    print("Awesome here is what's inside the Mystery Box:")
    # Show content of mystery box
    instructions()
    
# Create Player class with inputs
def instructions():
    print("Alright Trainer!")
    print("I am transporting you to the world of Pokemon")
    print("This region is called Noob Town")
    print("You Player have a mark called 'M' in the map")
    print("Enemy Players have a mark called 'C' in the map")
    print("Wild Pokemon have a mark called 'P' in the map")
    print("Trees are marked with '#' in the map")
    ready_input = input("Are you ready? Enter (y for Yes and n for No)\nChoice:")
    
    if(ready_input == 'y'):
        print("Alright let's begin!")
        print("Zoooooooom!")
        # activate sequence here 
        pass_through_grid([5,5], grid)
    else:
        print("Okay, here's the instructions again!")
        # return to instructions 
        instructions()
    

# # = Tree
# M = Player
# C = CPU
# P = Pokemon

# Movement 
# n for North
# s for South
# e for East
# w for West

grid = [['#', 'O', 'O', 'P', 'O', 'O', 'O', 'O', 'O', '#'],
 ['#', 'O', 'O', 'O', 'O', '#', '#', '#', '#', '#'],
 ['#', 'O', '#', 'O', 'O', 'O', '#', '#', '#', '#'],
 ['#', '#', 'O', 'O', 'O', 'O', 'O', '#', 'C', '#'],
 ['#', 'O', 'P', '#', 'O', 'O', 'O', 'O', '#', '#'],
 ['#', 'O', 'O', 'O', '#', 'M', 'O', '#', '#', '#'],
 ['#', '#', '#', '#', 'O', 'O', 'O', 'O', 'O', '#'],
 ['#', 'O', 'C', 'O', 'O', 'O', 'O', 'C', 'O', '#'],
 ['#', '#', '#', '#', 'O', 'O', 'O', 'O', 'O', '#'],
 ['#', '#', '#', 'O', 'O', 'O', 'P', 'O', 'O', '#']]


player_position = [0,0]

#my_grid[player_position[0]][player_position[1]] = 'X'


def battle_mode_cpu():
    print("Entering Trainer Battle Mode")
    pass

def battle_mode_poke():
    print("Entering Pokemon Battle Mode")
    
    


def pass_through_grid(current_player_position, grid):
    x = [-1,1,0,0]
    y = [0,0,-1,1]

    grid[current_player_position[0]][current_player_position[1]] = 'M'

    pprint(grid)

    while True:
        direction = input('Which direction do you want to move to?\nEnter n,w,e,s for direction: ')

        if direction == 'n':
            potential_new_position = [current_player_position[0] + x[0], current_player_position[1] + y[0]]
            
            #print(grid[potential_new_position[0]][potential_new_position[1]])

            # check the bounds
            if potential_new_position[0] < 0 or potential_new_position[0] > len(grid):
                print("Can't move this way")
                print("Enter different position")
                
            if grid[potential_new_position[0]][potential_new_position[1]] == '#':
                print("TREE!!!")
                print("Enter different position")
                
            if grid[potential_new_position[0]][potential_new_position[1]] == 'C':
                print("ENEMY TRAINER!")
                print("LET'S GO!")
                # Player battles with trainer here
                
            if grid[potential_new_position[0]][potential_new_position[1]] == 'P':
                print("WILD POKEMON!!")
                print("GO!")
                # player battles with pokemon here
            
            else:
            
                grid[current_player_position[0]][current_player_position[1]] = 'O'

                # change the position
                grid[potential_new_position[0]][potential_new_position[1]] = 'M'

                current_player_position = potential_new_position

        elif direction == 's':
            potential_new_position = [current_player_position[0] + x[1], current_player_position[1] + y[1]]

            # check the bounds
            if potential_new_position[0] < 0 or potential_new_position[0] > len(grid):
                print("Can't move this way")
                print("Enter different position")
                
            if grid[potential_new_position[0]][potential_new_position[1]] == '#':
                print("TREE!!!")
                print("Enter different position")
                
            if grid[potential_new_position[0]][potential_new_position[1]] == 'C':
                print("ENEMY TRAINER!")
                print("LET'S GO!")
                # Player battles with trainer here
                
            if grid[potential_new_position[0]][potential_new_position[1]] == 'P':
                print("WILD POKEMON!!")
                print("GO!")
                # player battles with pokemon here
                    
            else:
                grid[current_player_position[0]][current_player_position[1]] = 'O'

                # change the position
                grid[potential_new_position[0]][potential_new_position[1]] = 'M'

                current_player_position = potential_new_position

        elif direction == 'w':
            potential_new_position = [current_player_position[0] + x[2], current_player_position[1] + y[2]]

            # check the bounds
            if potential_new_position[1] < 0 or potential_new_position[1] > len(grid[0]):
                print("Can't move this way")
                print("Enter different position")
            
            if grid[potential_new_position[0]][potential_new_position[1]] == '#':
                print("TREE!!!")
                print("Enter different position")
                
            if grid[potential_new_position[0]][potential_new_position[1]] == 'C':
                print("ENEMY TRAINER!")
                print("LET'S GO!")
                
            if grid[potential_new_position[0]][potential_new_position[1]] == 'P':
                print("WILD POKEMON!!")
                print("GO!")
                    

                    
            else:
                grid[current_player_position[0]][current_player_position[1]] = 'O'

                # change the position
                grid[potential_new_position[0]][potential_new_position[1]] = 'M'

                current_player_position = potential_new_position

        elif direction == 'e':
            potential_new_position = [current_player_position[0] + x[3], current_player_position[1] + y[3]]

            # check the bounds
            if potential_new_position[1] < 0 or potential_new_position[1] > len(grid[0]):
                print("Can't move this way")
                print("Enter different position")
                
            if grid[potential_new_position[0]][potential_new_position[1]] == '#':
                print("TREE!!!")
                print("Enter different position")
                
            if grid[potential_new_position[0]][potential_new_position[1]] == 'C':
                print("ENEMY TRAINER!")
                print("LET'S GO!")
                # Player battles with trainer here
                
            if grid[potential_new_position[0]][potential_new_position[1]] == 'P':
                print("WILD POKEMON!!")
                print("GO!")
                # player battles with pokemon here
                    

                    
            else:
                grid[current_player_position[0]][current_player_position[1]] = 'O'

                # change the position
                grid[potential_new_position[0]][potential_new_position[1]] = 'M'

                current_player_position = potential_new_position


        elif direction == 'exit':
            print("==========================================================")
            print("\t\tGoodbye Trainer! Please Play Again!")
            print("==========================================================")
            break


        # Finally we print the grid
        pprint(grid)

    return None


def start():
    title()
    player_creation()
    
start()