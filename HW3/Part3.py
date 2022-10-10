# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:07:50 2020

@author: annorm
"""
import math



"""A FUNCTION THAT DETERMINES THE NEXT POPULATION OF BEARS, BERRIES,
AND TOURIST BASED OFF THE CURRENT POPULATIO"""



def find_next(bears, berries, tourists):
    if bears < 0:
        bears1 = 0
    else:
        bears1 = bears

    if berries < 0:
        berries1 = 0
    else:
        berries1 = berries

    if tourists < 0:
        tourists1 = 0
    else:
        tourists1 = tourists

    bears_pop.append(bears)
    berries_pop.append(berries)
    tourists_pop.append(tourists)

    print("Year"+ y_space + "Bears" + b_space + "Berry" + b_space + "Tourists" + " " *( 10-len("Tourists") ) )
    print("1" + space + str(bears1) + " " * ( 10-len(str(bears1) ) ) + "{:.1f}".format(berries1) + " " * (10-len(str( "{:.1f}".format(berries1) ) ) ) + str(tourists1) + " " *(10-len(str(tourists1) ) ) )


    #LOOP THAT FINDS AND PRINTS ALL THREE POPULATIONS
    i = 2
    while i <= 10:
        bears_next = int( berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1) )
        berries_next = float( (berries*1.5) - (bears+1)*(berries/14) - \
            (math.log(1+tourists,10)*0.05) )
        tourists_next = int( 20000*(bears_next-10)+100000 )



    #MAKING NEGATIVES = 0
        if bears_next > 0:
            bears = bears_next
        else:
            bears = 0

        if berries_next>0:
            berries = berries_next
        else:
            berries = 0

        if bears_next < 4 or bears_next > 15:
            tourists_next = 0
        elif bears_next > 10:
            tourists_next=tourists_next
        elif bears_next <= 10:
            tourists_next = 10000*bears



        if tourists_next > 0:
            tourists = tourists_next
        else:
            tourists = 0


        berries_pop.append(berries)
        tourists_pop.append(tourists)
        bears_pop.append(bears)



        print(str(i) + " " * ( 10-len(str(i)) ) + str(bears) + " " * ( 10-len( str(bears) ) ) + "{:.1f}".format(berries) +  " "*( 10-len(str("{:.1f}".format(berries)) ) ) + str(tourists) + " " * (10-len(str(tourists))) )

        if i == 10:
            print("")
            print("Min:" + y_space + str( min(bears_pop) ) + " " * ( 10-len( str( min(bears_pop) ) ) ) + str( "{:.1f}".format(min(berries_pop)) ) + " " * ( 10-len(str( "{:.1f}".format(min(berries_pop)) ) ) ) + str( min(tourists_pop) ) + " " * (10-len(str( min(tourists_pop) ))))
            print("Max:" + y_space + str( max(bears_pop) ) + " " * ( 10-len( str( max(bears_pop) ) ) ) + str( "{:.1f}".format(max(berries_pop)) ) + " " * ( 10-len(str( "{:.1f}".format(max(berries_pop)) ) ) ) + str( max(tourists_pop) ) + " " * (10-len(str( max(tourists_pop) ))))

        i += 1


if __name__ == "__main__":
    bears = int( input("Number of bears => ") )
    print(bears)

    berries = ( input("Size of berry area => ") )
    print(berries)
    berries = float(berries)

#DETERMINE THE AMOUNT OF TOURIST
    tourists = int( 20000*(bears-10)+100000 )

    if bears < 4 or bears > 15:
        tourists = 0
    elif bears <= 10:
        tourists = 10000*bears
        tourists1 =tourists
#CALCULATING SPACES
y_space = " " * 6
b_space = " " * 5
space = " " *9

#LIST TO STORE THE VALUES FOR MIN AND MAX
bears_pop = []
tourists_pop = []
berries_pop = []


find_next(bears, berries, tourists)
