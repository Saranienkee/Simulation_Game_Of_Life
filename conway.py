"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import CheckFigures
import datetime

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N,M):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*M, p=[0.2, 0.8]).reshape(N, M)

def gridReadFile(N, M, gridFile):
    M = int(M)
    N = int(N)
    grid = np.zeros(N*M).reshape(N,M)
    for coordenada in gridFile:
        if (coordenada[0] < N and coordenada[1] < M):
            grid[coordenada[0], coordenada[1]] = ON

    print(grid)
    print(N)
    print(M)
    return grid



def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, N,M):

    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    vecinos=0
    for i in range(N):
        for j in range(M):

            if i > 0:
                if grid[i - 1, j]==ON:
                    vecinos += 1
            if i < N - 1:
                if grid[i + 1, j]==ON:
                    vecinos += 1
            if j > 0:
                if grid[i, j - 1]==ON:
                    vecinos += 1
            if j < M - 1:
                if grid[i, j + 1]==ON:
                    vecinos += 1
            if i > 0 and j > 0:
                if grid[i - 1, j - 1]==ON:
                    vecinos += 1
            if i > 0 and j < M - 1:
                if grid[i - 1, j + 1]==ON:
                    vecinos += 1
            if i < N - 1 and j > 0:
                if grid[i + 1, j - 1]==ON:
                    vecinos += 1
            if i < N - 1 and j < M - 1:
                if grid[i + 1, j + 1]==ON:
                    vecinos += 1


            if grid[i,j]==ON:
                if vecinos==2 or vecinos==3:
                    newGrid[i,j]=ON
                if vecinos<2 or vecinos>3:
                    newGrid[i, j] = OFF

            if grid[i,j]==OFF:
                if vecinos==3:
                    newGrid[i,j]=ON

            vecinos=0

    figure_count = CheckFigures.CountFigures(grid,N,M)


    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]

    return img,






# main() function
def main():

    grid = np.array([])  # declara array 2d vacio
    gridFile=[]

    readFiles = int(input("Do you want to read a file? 0 for no and 1 for yes "))
    #while True:
        #if not(readFiles == 0 and readFiles == 1):
            #readFiles = int(input("Do you want to read a file? 0 for no and 1 for yes "))
            #break
    outputs = open('Outputs_Simulation.txt', 'w')
    outputs.write("")

    if readFiles==1:

        f = open('read3.txt', 'r')
        for i, line in enumerate(f.readlines()):
            if i == 0:
                lineArray=line.split()
                N=int(lineArray[0])
                M =int(lineArray[1])

            if i == 1:
                print("no")

            else:
                lineCoordinates=line.split()
                lineCoordinates[0] = int(lineCoordinates[0])
                lineCoordinates[1] = int(lineCoordinates[1])
                gridFile.append(lineCoordinates)


        f.close()
        grid=gridReadFile(N,M,gridFile)




    if readFiles == 0:
        nInput = input("Number of Rows: ")
        mInput=input("Number of Columns: ")
        # Command line args are in sys.argv[1], sys.argv[2] ..
        # sys.argv[0] is the script name itself and can be ignored
        # parse arguments
        parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
        # TODO: add arguments

        # set grid size
        N = int(nInput) #tamaño de la simulacion
        M = int(mInput)
        grid = randomGrid(N, M)



    dateSimulation = datetime.datetime.now()
    outputs.write(f"Simulation at {dateSimulation}\n")
    outputs.write(f"Universe size {N} X {M}\n")

    # set animation update interval
    updateInterval = 500 #tiempo en ms que toma entre frame

    # declare grid

    # populate grid with random on/off - more off than on



    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(N*M).reshape(N, M)
    #addGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')



    # hace que la animacion ocurra
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, M,),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()



# call main
if __name__ == '__main__':
    main()