# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:14:59 2020

@author: annorm
"""
import hw5_util
"""Using hw5_util print the gradual and steepest path from the start location
to the global maximum or local maximium"""


def get_nbrs(r,c):
        if (r>0 and c>0) and ( r<len(grid)-1 and c<len(grid[r])-1 ):
            neighbors = [ (r-1, c) , (r+1, c) , (r, c-1) , (r, c+1) ]
            return(neighbors)

        elif (r==0 and c>0) and ( r<len(grid)-1 and c<len(grid[r])-1 ):
            neighbors = [ (r, c-1) ,(r, c+1) , (r+1, c) ]
            return(neighbors)

        elif (r>0 and c>0) and ( r==len(grid)-1 and c<len(grid[r])-1 ):
            neighbors = [ (r-1, c) , (r, c-1) , (r, c+1) ]
            return(neighbors)

        elif (r>0 and c==0) and ( r<len(grid)-1 and c<len(grid[r])-1 ):
            neighbors = [ (r-1, c) , (r+1, c) , (r, c+1) ]
            return(neighbors)

        elif (r>0 and c>0) and ( r<len(grid)-1 and c==len(grid[r])-1 ):
            neighbors = [ (r-1, c) , (r, c-1) , (r+1, c) ]
            return(neighbors)

        elif (r>0 and c>0) and ( r==len(grid)-1 and c==len(grid[r])-1 ):
            neighbors = [ (r-1, c) , (r, c-1) ]
            return(neighbors)

        elif (r==0 and c==0) and ( r<len(grid)-1 and c<len(grid[r])-1 ):
            neighbors = [ (r+1, c) , (r, c+1) ]
            return(neighbors)

        elif (r==0 and c>0) and ( r<len(grid)-1 and c==len(grid[r])-1 ):
            neighbors = [ (r+1, c) , (r, c-1) ]
            return(neighbors)

        elif (r>0 and c==0) and ( r==len(grid)-1 and c<len(grid[r])-1 ):
            neighbors = [ (r-1, c) , (r, c+1) ]
            return(neighbors)




stop = False
while not stop:
    n = int (input("Enter a grid index less than or equal to 3 (0 to end): ") )

    if n <= hw5_util.num_grids():
        print(n)
        grid = hw5_util.get_grid(n)
        stop = True

        max_step = int( input("Enter the maximum step height: ") )
        print(max_step)


        choice = input("Should the path grid be printed (Y or N): ")
        print(choice)
        choice = choice.upper()
        print("Grid has", len(grid), "rows and", len(grid[0]), "columns")


        #FINDING THE GLOBAL MAXIMUM AND STORING THE LOCATION FOR LATER USE
        high=[]
        i=0
        while i < len(grid):
            high.append( max(grid[i]) )
            i += 1

        x=0
        while x < len(grid):
            y=0
            while y < len(grid[x]):
                if max(high) == grid[x][y]:
                    max_x = x
                    max_y = y
                    print("global max:", "(" + str(x) + "," , str(y) + ")", max(high))
                y += 1
            x += 1

        print("===")


        #FINDING THE LOCAL MAXIMUM AND STORING THE LOCATION FOR LATER USE
        r = 0
        while r < len(grid):
            c = 0
            while c < len(grid[r]):
                if (r>0 and c>0) and ( r<len(grid)-1 and c<len(grid[r])-1 ):
                    if grid[r][c] < max(high) and grid[r][c] > grid[r-1][c] and grid[r][c] > grid[r+1][c]\
                        and grid[r][c] > grid[r][c-1] and grid[r][c] > grid[r][c+1]:
                            local_x = r
                            local_y = c
                            local_max = grid[r][c]

                elif (r==0 and c>0) and ( r<len(grid)-1 and c<len(grid[r])-1 ):
                    if grid[r][c] > max(high) and grid[r][c] > grid[r][c-1] and grid[r][c] > grid[r][c+1]\
                        and grid[r][c] > grid[r+1][c]:
                            local_x = r
                            local_y = c
                            local_max = grid[r][c]

                elif (r>0 and c>0) and ( r==len(grid)-1 and c<len(grid[r])-1 ):
                    if grid[r][c] < max(high) and grid[r][c] > grid[r-1][c] and grid[r][c] > grid[r][c-1]\
                        and grid[r][c] > grid[r][c+1]:
                            local_x = r
                            local_y = c
                            local_max = grid[r][c]

                elif (r>0 and c==0) and ( r<len(grid)-1 and c<len(grid[r])-1 ):
                    if grid[r][c] < max(high) and grid[r][c] > grid[r-1][c] and grid[r][c] > grid[r+1][c]\
                        and grid[r][c] > grid[r][c+1]:
                            local_x = r
                            local_y = c
                            local_max = grid[r][c]

                elif (r>0 and c>0) and ( r<len(grid)-1 and c==len(grid[r])-1 ):
                    if grid[r][c] < max(high) and grid[r][c] > grid[r-1][c] and grid[r][c] > grid[r][c-1]\
                        and grid[r][c] > grid[r+1][c]:
                            local_x = r
                            local_y = c
                            local_max = grid[r][c]

                elif (r>0 and c>0) and ( r==len(grid)-1 and c==len(grid[r])-1 ):
                    if grid[r][c] < max(high) and grid[r][c] > grid[r-1][c] and grid[r][c] > grid[r][c-1]:
                        local_x = r
                        local_y = c
                        local_max = grid[r][c]

                elif (r==0 and c==0) and ( r<len(grid)-1 and c<len(grid[r])-1 ):
                    if grid[r][c] < max(high) and grid[r][c] > grid[r+1][c] and grid[r][c] > grid[r][c+1]:
                        local_x = r
                        local_y = c
                        local_max = grid[r][c]

                elif (r==0 and c>0) and ( r<len(grid)-1 and c==len(grid[r])-1 ):
                    if grid[r][c] < max(high) and grid[r][c] > grid[r+1][c] and grid[r][c] > grid[r][c-1]:
                        local_x = r
                        local_y = c
                        local_max = grid[r][c]

                elif (r>0 and c==0) and ( r==len(grid)-1 and c<len(grid[r])-1 ):
                    if grid[r][c] < max(high) and grid[r][c] > grid[r-1][c] and grid[r][c+1]:
                        local_x = r
                        local_y = c
                        local_max = grid[r][c]
                c += 1
            r += 1

        #FINDING THE STEEPEST PATH FROM THE START LOCATION
        start_loc = hw5_util.get_start_locations(n)
        z = 0
        path = []
        while z < len(start_loc):
            pee=0
            print("steepest path")
            (row, column) = start_loc[z]
            path.append(start_loc[z])
            pee+=1
            if pee < 5:
                print( '(' + str(row) + ', '  + str(column) + ')', end = " " )
            if pee == 5:
                print( '(' + str(row) + ', '  + str(column) + ') ')
                pee=0
            neighbors = get_nbrs(row, column)

            #AFTER FIND THE NEIGHBORS OF THE START LOCATION FINDS WHICH HEIGHT DIFFERENCE IS LESS THAT THE MAXIMUM STEP AND STORES THEM INTO OPTIONS
            s = 0
            options = []
            while s < len(neighbors):
                if grid[neighbors[s][0]][neighbors[s][1]] - grid[row][column] > 0 and max_step >= grid[neighbors[s][0]][neighbors[s][1]] - grid[row][column]:
                    options.append(neighbors[s])
                s += 1

            #GOES THROUGH OPTIONS AND CHECKS WHICH DIFFERENCE IS GREATER AND USES THAT AS THE NEW START LOCATION AND ADDS IT TO THE PATH
            t = 0
            if len(options) > 0 and len(options)!=1:
                while t < len(options)-1:
                    if grid[options[t+1][0]][options[t+1][1]] > grid[options[t][0]][options[t][1]]:
                        (row, column) = (options[t+1][0],options[t+1][1])
                        path.append(options[t+1])
                    else:
                        (row, column) = (options[t][0],options[t][1])
                        path.append( (options[t]) )

                    t += 1
            if len(options) == 1:
                path.append(options[0])
                (row, column) = options[0][0], options[0][1]


            #REPEAT OF THE PREVIOUS LOOP USING THE NEW START LOCATION AND CONTINUES UNTIL IT REACHES THE GLOBAL OR LOCAL MAX
            end_found = False
            while not end_found:
                pee+=1
                if pee < 5:
                    print( '(' + str(row) + ', '  + str(column) + ')', end = " " )
                if pee == 5:
                    print( '(' + str(row) + ', '  + str(column) + ') ')
                    pee=0
                neighbors = get_nbrs(row, column)
                s = 0
                options = []
                while s < len(neighbors):
                    if grid[neighbors[s][0]][neighbors[s][1]] - grid[row][column] > 0 and max_step >= grid[neighbors[s][0]][neighbors[s][1]] - grid[row][column]:
                        options.append(neighbors[s])
                    s += 1

                t = 0
                if len(options) > 0:
                    while t < len(options)-1:
                        if grid[options[t+1][0]][options[t+1][1]] > grid[options[t][0]][options[t][1]]:
                            (row, column) = (options[t+1][0],options[t+1][1])
                            path.append(options[t+1])
                        else:
                            (row, column) = (options[t][0],options[t][1])
                            path.append( (options[t]) )
                        t += 1

                if len(options) == 1:
                    path.append(options[0])
                    (row, column) = (options[0][0], options[0][1])
                elif len(options)==0:
                    end_found = True
                    print("\nno maximum")
                    print("...")

                if grid[path[-1][0]][path[-1][1]] == grid[max_x][max_y]:
                    end_found = True
                    print( '(' + str(row) + ', '  + str(column) + ') ')
                    print("global maximum")
                    print("...")

                elif grid[path[-1][0]][path[-1][1]] == grid[local_x][local_y]:
                    end_found = True
                    print( '(' + str(row) + ', '  + str(column) + ') ')
                    print("local maximum")
                    print("...")





        #SAME AS THE PREVIOUS LOOP JUST USES THE LOWER DIFFERENCE TO MOVE TO THE GLOBAL MAX

            print("most gradual path")
            peepee=0
            (row, column) = start_loc[z]
            path.append(start_loc[z])

            peepee+=1
            if peepee < 5:
                print( '(' + str(row) + ', '  + str(column) + ')', end = " " )
            if peepee == 5:
                print( '(' + str(row) + ', '  + str(column) + ') ')
                peepee=0

            neighbors = get_nbrs(row, column)
            s = 0
            options = []
            while s < len(neighbors):
                if grid[neighbors[s][0]][neighbors[s][1]] - grid[row][column] > 0 and max_step >= grid[neighbors[s][0]][neighbors[s][1]] - grid[row][column]:
                    options.append(neighbors[s])
                s += 1

            t = 0
            if len(options) > 0 and len(options)!=1:
                while t < len(options)-1:
                    if grid[options[t+1][0]][options[t+1][1]] < grid[options[t][0]][options[t][1]]:
                        (row, column) = (options[t+1][0],options[t+1][1])
                        path.append(options[t+1])
                    else:
                        (row, column) = (options[t][0],options[t][1])
                        path.append( (options[t]) )

                    t += 1
            if len(options) == 1:
                path.append(options[0])
                (row, column) = options[0][0], options[0][1]

            end_found = False
            while not end_found:
                peepee+=1
                if peepee < 5:
                    print( '(' + str(row) + ', '  + str(column) + ')', end = " " )
                if peepee == 5:
                    print( '(' + str(row) + ', '  + str(column) + ') ')
                    peepee=0

                neighbors = get_nbrs(row, column)
                s = 0
                options = []
                while s < len(neighbors):
                    if grid[neighbors[s][0]][neighbors[s][1]] - grid[row][column] > 0 and max_step >= grid[neighbors[s][0]][neighbors[s][1]] - grid[row][column]:
                        options.append(neighbors[s])
                    s += 1

                t = 0
                if len(options) > 0:
                    while t < len(options)-1:
                        if grid[options[t+1][0]][options[t+1][1]] < grid[options[t][0]][options[t][1]]:
                            (row, column) = (options[t+1][0],options[t+1][1])
                            path.append(options[t+1])
                        else:
                            (row, column) = (options[t][0],options[t][1])
                            path.append( (options[t]) )
                        t += 1

                if len(options) == 1:
                    path.append(options[0])
                    (row, column) = (options[0][0], options[0][1])

                elif len(options)==0:
                    end_found = True
                    print("\nno maximum")
                    print("===")

                if grid[path[-1][0]][path[-1][1]] == grid[max_x][max_y]:
                    end_found = True
                    print( '(' + str(row) + ', '  + str(column) + ') ')
                    print("global maximum")
                    print("===")

                elif grid[path[-1][0]][path[-1][1]] == grid[local_x][local_y]:
                    end_found = True
                    print( '(' + str(row) + ', '  + str(column) + ') ')
                    print("local maximum")
                    print("===")


            z += 1

        if choice == "Y":
           print("Path grid")
           path_row = 0
           while path_row < len(grid):
               path_column = 0

               while path_column < len(grid[path_row]):
                   path.count( (path_row, path_column) )

                   if path_column == 0:
                       if path.count( (path_row, path_column) ) == 0:
                           print(" ", ".", end = "  ")
                       elif path.count( (path_row, path_column) ) > 0:
                           print(" ", path.count( (path_row, path_column) ), end = "  ")
                   elif path_column > 0 and path_column != len(grid[path_row])-1:
                       if path.count((path_row, path_column)) == 0:
                           print(".", end = "  ")
                       elif path.count( (path_row, path_column) ) > 0:
                           print(path.count( (path_row, path_column) ), end = "  ")

                   elif path_column == len(grid[path_row])-1:
                       if path.count((path_row, path_column)) == 0:
                           print(".")
                       elif path.count( (path_row, path_column) ) > 0:
                           print(path.count( (path_row, path_column) ) )

                   path_column += 1
               path_row += 1
