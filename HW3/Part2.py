# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:03:20 2020

@author: annorm
"""
#PIKACHU SIMULATION

#USER INPUTS
turns = int( input("How many turns? => ") )
print(turns)
name = input("What is the name of your pikachu? => ")
print(name)
meet = int( input("How often do we see a Pokemon (turns)? => ") )
print(meet)

width = 75
height = 75
position = (width, height)



#SIMULATION FUNCTION
def move_pokemon(width, height, meet):

   print(" ")
   print("Starting simulation,", "turn 0", name, "at ("+ str(width) + "," , str(height) + ")"  )

   #SIMULATION WHILE LOOP
   i = 1
   N = -1
   E = 1
   W = -1
   S = 1
   total = meet
   Record = []

   if turns == 0:
                print(name, "ends up at (" + str(width) + "," , str(height) + ")" + "," , "Record:", Record )

    #WHICH WAY TO MOVE
   while i<= turns:
        direction = input("What direction does {} walk? => ".format(name))
        print(direction)
        direction = direction.upper()

        if direction == "N":
            width = width + (5*N)

        elif direction == "S":
            width = width + (5*S)

        elif direction == "W":
            height = height + (5*W)

        elif direction == "E":
            height = height + (5*E)


        if height < 0:
            height = 0
        elif  150 < height:
            height = 150
        elif width < 0:
            width = 0
        elif 150 < width:
            width = 150


        #MEETING ANOTHER POKEMON
        if i == total:
            print("Turn", str(i) + ",", name, "at (" + str(width) + ",", str(height) + ")" )
            kind = input("What type of pokemon do you meet (W)ater, (G)round? => ")
            print(kind)
            kind = kind.upper()

            #MEETING A WATER TYPE
            if kind == "W":
                Record.append("Win")
                if direction == "N":
                    width = width + N
                elif direction == "S":
                    width = width + S
                elif direction == "W":
                    height = height + W
                elif direction == "E":
                    height = height + E

                if (0 <= height and height <= 150) and (0 <= width and width <= 150):
                    print(name, "wins and moves to (" + str(width) + ",", str(height) + ")" )
                elif height < 0:
                    height = 0
                    print(name, "wins and moves to (" + str(width) + ",", str(height) + ")" )
                elif  150 < height:
                    height = 150
                    print(name, "wins and moves to (" + str(width) + ",", str(height) + ")" )
                elif width < 0:
                    width = 0
                    print(name, "wins and moves to (" + str(width) + ",", str(height) + ")" )
                elif 150 < width:
                    width = 150


            #MEETING A GROUND TYPE
            elif kind == "G":
                Record.append("Lose")
                if direction == "N":
                    width = width + (S*10)
                elif direction == "S":
                    width = width + (N*10)
                elif direction == "W":
                    height = height + (E*10)
                elif direction == "E":
                    height = height + (W*10)

                if (0 <= height and height <= 150) and (0 <= width and width <= 150):
                    print(name, "runs away to (" + str(width) + ",", str(height) + ")")
                elif height < 0:
                    height = 0
                    print(name, "runs away to (" + str(width) + ",", str(height) + ")" )
                elif  150 < height:
                    height = 150
                    print(name, "runs away to (" + str(width) + ",", str(height) + ")" )
                elif width<0:
                    width = 0
                    print(name, "runs away to (" + str(width) + ",", str(height) + ")" )
                elif 150 < width:
                    width = 150

            else:
                Record.append("No Pokemon")

            total += meet


        #FINAL TURN AND RESULTS
        if i == turns:
                if (0 <= height and height <= 150) and (0 <= width and width <= 150):
                    print(name, "ends up at", "(" + str(width) + ",", str(height) + ")" + ",", "Record:", Record )

        i += 1


move_pokemon(width, height, meet)
