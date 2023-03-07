import numpy as np
n=0
# _____________________________________________________________________________________________________________________________Mascaras
# _____________________________________________________________________ Block
matrix = [
    [0, 0, 0, 0],
    [0, 255, 255, 0],
    [0, 255, 255, 0],
    [0, 0, 0, 0],
]
Block = np.array(matrix)
#_____________________________________________________________________ Beehive
matrix = [
    [0, 0, 0, 0, 0,0],
    [0, 0, 255, 255, 0,0],
    [0, 255, 0, 0, 255,0],
    [0, 0, 255, 255, 0,0],
    [0, 0, 0, 0, 0,0],
]
Beehive = np.array(matrix)
Beehive1 = np.rot90(matrix)
# _____________________________________________________________________ Loaf
matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 255, 255, 0, 0],
    [0, 255, 0, 0, 255, 0],
    [0, 0, 255, 0, 255, 0],
    [0, 0, 0, 255, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
Loaf = np.array(matrix)
Loaf1 = np.rot90(matrix)
Loaf2 = np.rot90(matrix, k=2)
Loaf3 = np.rot90(matrix, k=3)

# _____________________________________________________________________ Boat
matrix = [
    [0, 0, 0, 0, 0],
    [0, 255, 255, 0, 0],
    [0, 255, 0, 255, 0],
    [0, 0, 255, 0, 0],
    [0, 0, 0, 0, 0],
]
Boat = np.array(matrix)
Boat1 = np.rot90(matrix)
Boat2 = np.rot90(matrix, k=2)
Boat3 = np.rot90(matrix, k=3)
# _____________________________________________________________________ Tub
matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 255, 0, 0],
    [0, 255, 0, 255, 0],
    [0, 0, 255, 0, 0],
    [0, 0, 0, 0, 0],
]
Tub = np.array(matrix)
# _____________________________________________________________________ Blinkers
matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 255, 0, 0],
    [0, 0, 255, 0, 0],
    [0, 0, 255, 0, 0],
    [0, 0, 0, 0, 0],

]
BlinckerV = np.array(matrix)

matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 255, 255, 255, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],

]
BlinckerH = np.array(matrix)
# _____________________________________________________________________ Toads
matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 255, 0, 0],
    [0, 255, 0, 0, 255, 0],
    [0, 255, 0, 0, 255, 0],
    [0, 0, 255, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
Toad1 = np.array(matrix)
Toad11 = np.rot90(matrix)
Toad12 = np.rot90(matrix, k=2)
Toad13 = np.rot90(matrix, k=3)

matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 255, 255, 255, 0],
    [0, 255, 255, 255, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
Toad2 = np.array(matrix)
Toad21 = np.rot90(matrix)
Toad22 = np.rot90(matrix, k=2)
Toad23 = np.rot90(matrix, k=3)
# _____________________________________________________________________ Beacons
matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 255, 255, 0, 0, 0],
    [0, 255, 255, 0, 0, 0],
    [0, 0, 0, 255, 255, 0],
    [0, 0, 0, 255, 255, 0],
    [0, 0, 0, 0, 0, 0],
]
Beacon1 = np.array(matrix)
Beacon11 = np.rot90(matrix)
Beacon12 = np.rot90(matrix, k=2)
Beacon13 = np.rot90(matrix, k=3)

matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 255, 255, 0, 0, 0],
    [0, 255, 0, 0, 0, 0],
    [0, 0, 0, 0, 255, 0],
    [0, 0, 0, 255, 255, 0],
    [0, 0, 0, 0, 0, 0],
]
Beacon2 = np.array(matrix)
Beacon21 = np.rot90(matrix)
Beacon22 = np.rot90(matrix, k=2)
Beacon23 = np.rot90(matrix, k=3)
# _____________________________________________________________________ Gliders
matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 255, 0, 0],
    [0, 0, 0, 255, 0],
    [0, 255, 255, 255, 0],
    [0, 0, 0, 0, 0],
]
Glider1 = np.array(matrix)
Glider11 = np.rot90(matrix)
Glider12 = np.rot90(matrix, k=2)
Glider13 = np.rot90(matrix, k=3)
matrix = [
    [0, 0, 0, 0, 0],
    [0, 255, 0, 255, 0],
    [0, 0, 255, 255, 0],
    [0, 0, 255, 0, 0],
    [0, 0, 0, 0, 0],
]
Glider2 = np.array(matrix)
Glider21 = np.rot90(matrix)
Glider22 = np.rot90(matrix, k=2)
Glider23 = np.rot90(matrix, k=3)
matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 255, 0],
    [0, 255, 0, 255, 0],
    [0, 0, 255, 255, 0],
    [0, 0, 0, 0, 0],
]
Glider3 = np.array(matrix)
Glider31 = np.rot90(matrix)
Glider32 = np.rot90(matrix, k=2)
Glider33 = np.rot90(matrix, k=3)
matrix = [
    [0, 0, 0, 0, 0],
    [0, 255, 0, 0, 0],
    [0, 0, 255, 255, 0],
    [0, 255, 255, 0, 0],
    [0, 0, 0, 0, 0],
]
Glider4 = np.array(matrix)
Glider41 = np.rot90(matrix)
Glider42 = np.rot90(matrix, k=2)
Glider43 = np.rot90(matrix, k=3)

# _____________________________________________________________________ Light-weight spaceship
matrix = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 255, 0, 0, 255, 0, 0],
    [0, 0, 0, 0, 0, 255, 0],
    [0, 255, 0, 0, 0, 255, 0],
    [0, 0, 255, 255, 255, 255, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
LWS1 = np.array(matrix)
LWS11 = np.rot90(matrix)
LWS12 = np.rot90(matrix, k=2)
LWS13 = np.rot90(matrix, k=3)

matrix = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 255, 255, 0, 0],
    [0, 255, 255, 0, 255, 255, 0],
    [0, 255, 255, 255, 255, 0, 0],
    [0, 0, 255, 255, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
LWS2 = np.array(matrix)
LWS21 = np.rot90(matrix)
LWS22 = np.rot90(matrix, k=2)
LWS23 = np.rot90(matrix, k=3)

matrix = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 255, 255, 0, 0, 0],
    [0, 255, 255, 255, 255, 0, 0],
    [0, 255, 255, 0, 255, 255, 0],
    [0, 0, 0, 255, 255, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
LWS3 = np.array(matrix)
LWS31 = np.rot90(matrix)
LWS32 = np.rot90(matrix, k=2)
LWS33 = np.rot90(matrix, k=3)

matrix = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 255, 255, 255, 255, 0],
    [0, 255, 0, 0, 0, 255, 0],
    [0, 0, 0, 0, 0, 255, 0],
    [0, 255, 0, 0, 255, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

LWS4 = np.array(matrix)
LWS41 = np.rot90(matrix)
LWS42 = np.rot90(matrix,k=2)
LWS43 = np.rot90(matrix,k=3)

def CountFigures(grid,N,M):
    global n
    n +=1

    newGrid = np.zeros((N+2)*(M+2)).reshape((N+2),(M+2))

    for i in range(1,N+1):
        for j in range(1,M+1):
            newGrid[i,j]=grid[i-1,j-1]

    #_____________________________________________________________________________________________________________________________Count Figures

    percentblocks=0
    percentbeehives=0
    percentloafs=0
    percentboats=0
    percenttubs=0
    percentblinkers=0
    percenttoads=0
    percentbeacons=0
    percentgliders=0
    percentLWSs=0
    blocks=0
    beehives=0
    loafs= 0
    boats= 0
    tubs= 0
    blinkers= 0
    toads= 0
    beacons= 0
    gliders= 0
    LWSs= 0
    Total=0


    for i in range(N):
        for j in range(M):

            # _____________________________________________________________________ Block
            section = newGrid[i:i + 4, j:j + 4]
            if np.array_equal(section, Block ):
                blocks+=1
            # _____________________________________________________________________ Beehive
            section = newGrid[i:i + 5, j:j + 6]
            if np.array_equal(section, Beehive ):
                beehives += 1
            if np.array_equal(section, Beehive1 ):
                beehives += 1
            # _____________________________________________________________________ Loaf
            if np.array_equal(section, Loaf ):
                loafs += 1
            if np.array_equal(section, Loaf1 ):
                loafs += 1
            if np.array_equal(section, Loaf2 ):
                loafs += 1
            if np.array_equal(section, Loaf3 ):
                loafs += 1
            # _____________________________________________________________________ Boat
            section = newGrid[i:i + 5, j:j + 5]
            if np.array_equal(section, Boat ):
                boats += 1
            if np.array_equal(section, Boat1 ):
                boats += 1
            if np.array_equal(section, Boat2 ):
                boats += 1
            if np.array_equal(section, Boat3 ):
                boats += 1
            # _____________________________________________________________________ Tub
            if np.array_equal(section, Tub ):
                tubs += 1
            # _____________________________________________________________________ Blinkers
            if np.array_equal(section, BlinckerV ):
                blinkers += 1
            if np.array_equal(section, BlinckerH):
                blinkers += 1
            # _____________________________________________________________________ Toads
            section = newGrid[i:i + 6, j:j + 6]
            if np.array_equal(section, Toad1 ):
                toads += 1
            if np.array_equal(section, Toad11):
                toads += 1
            if np.array_equal(section, Toad12):
                toads += 1
            if np.array_equal(section, Toad13):
                toads += 1
            if np.array_equal(section, Toad2):
                toads += 1
            if np.array_equal(section, Toad21):
                toads += 1
            if np.array_equal(section, Toad22):
                toads += 1
            if np.array_equal(section, Toad23):
                toads += 1
            # _____________________________________________________________________ Beacons
            if np.array_equal(section, Beacon1):
                beacons += 1
            if np.array_equal(section, Beacon11):
                beacons += 1
            if np.array_equal(section, Beacon12):
                beacons += 1
            if np.array_equal(section, Beacon13):
                beacons += 1
            if np.array_equal(section, Beacon2):
                beacons += 1
            if np.array_equal(section, Beacon21):
                beacons += 1
            if np.array_equal(section, Beacon22):
                beacons += 1
            if np.array_equal(section, Beacon23):
                beacons += 1
            # _____________________________________________________________________ Gliders
            section = newGrid[i:i + 5, j:j + 5]
            if np.array_equal(section, Glider1):
                gliders += 1
            if np.array_equal(section, Glider11):
                gliders += 1
            if np.array_equal(section, Glider12):
                gliders += 1
            if np.array_equal(section, Glider13):
                beacons += 1
            if np.array_equal(section, Glider2):
                gliders += 1
            if np.array_equal(section, Glider21):
                gliders += 1
            if np.array_equal(section, Glider22):
                gliders += 1
            if np.array_equal(section, Glider23):
                gliders += 1
            if np.array_equal(section, Glider3):
                gliders += 1
            if np.array_equal(section, Glider31):
                gliders += 1
            if np.array_equal(section, Glider32):
                gliders += 1
            if np.array_equal(section, Glider33):
                gliders += 1
            if np.array_equal(section, Glider4):
                gliders += 1
            if np.array_equal(section, Glider41):
                gliders += 1
            if np.array_equal(section, Glider42):
                gliders += 1
            if np.array_equal(section, Glider43):
                gliders += 1
            # _____________________________________________________________________ Light-weight spaceship
            section = newGrid[i:i + 5, j:j + 5]
            if np.array_equal(section, LWS1):
                LWSs += 1
            if np.array_equal(section, LWS11):
                LWSs += 1
            if np.array_equal(section, LWS12):
                LWSs += 1
            if np.array_equal(section, LWS13):
                LWSs += 1
            if np.array_equal(section, LWS2):
                LWSs += 1
            if np.array_equal(section, LWS21):
                LWSs += 1
            if np.array_equal(section, LWS22):
                LWSs += 1
            if np.array_equal(section, LWS23):
                LWSs += 1
            if np.array_equal(section, LWS3):
                LWSs += 1
            if np.array_equal(section, LWS31):
                LWSs += 1
            if np.array_equal(section, LWS32):
                LWSs += 1
            if np.array_equal(section, LWS33):
                LWSs += 1
            if np.array_equal(section, LWS4):
                LWSs += 1
            if np.array_equal(section, LWS41):
                LWSs += 1
            if np.array_equal(section, LWS42):
                LWSs += 1
            if np.array_equal(section, LWS43):
                LWSs += 1

    Total=blocks+beehives+loafs+boats+tubs+blinkers+toads+beacons+gliders+LWSs

    if Total>0:
        percentblocks=(blocks*100)/Total
        percentbeehives=(beehives*100)/Total
        percentloafs=(loafs*100)/Total
        percentboats=(boats*100)/Total
        percenttubs=(tubs*100)/Total
        percentblinkers=(blinkers*100)/Total
        percenttoads=(toads*100)/Total
        percentbeacons=(beacons*100)/Total
        percentgliders=(gliders*100)/Total
        percentLWSs=(LWSs*100)/Total



    print("")
    print("")
    print(f"Iteration: {n}")
    print("____________________________________________")
    print("|                |   Count   |   Percent   |")
    print("____________________________________________")
    print(f"|        Block   |      {blocks}     |      {int(percentblocks)}     |")
    print(f"|      Beehive   |      {beehives}     |      {int(percentbeehives)}     |")
    print(f"|         Loaf   |      {loafs}     |      {int(percentloafs)}     |")
    print(f"|         Boat   |      {boats}     |      {int(percentboats)}     |")
    print(f"|          Tub   |      {tubs}     |      {int(percenttubs)}     |")
    print(f"|      Blinker   |      {blinkers}     |      {int(percentblinkers)}     |")
    print(f"|         Toad   |      {toads}     |      {int(percenttoads)}     |")
    print(f"|       Beacon   |      {beacons}     |      {int(percentbeacons)}     |")
    print(f"|       Glider   |      {gliders}     |      {int(percentgliders)}     |")
    print(f"|    spaceship   |      {LWSs}     |      {int(percentLWSs)}     |")
    print("____________________________________________")
    print(f"|        Total   |      {Total}     |              |")

    with open("Outputs_Simulation.txt", "a") as file:
        file.write("\n")
        file.write("\n")
        file.write(f"Iteration: {n}\n")
        file.write("____________________________________________\n")
        file.write("|                |   Count   |   Percent   |\n")
        file.write("____________________________________________\n")
        file.write(f"|        Block   |      {blocks}     |      {int(percentblocks)}     |\n")
        file.write(f"|      Beehive   |      {beehives}     |      {int(percentbeehives)}     |\n")
        file.write(f"|         Loaf   |      {loafs}     |      {int(percentloafs)}     |\n")
        file.write(f"|         Boat   |      {boats}     |      {int(percentboats)}     |\n")
        file.write(f"|          Tub   |      {tubs}     |      {int(percenttubs)}     |\n")
        file.write(f"|      Blinker   |      {blinkers}     |      {int(percentblinkers)}     |\n")
        file.write(f"|         Toad   |      {toads}     |      {int(percenttoads)}     |\n")
        file.write(f"|       Beacon   |      {beacons}     |      {int(percentbeacons)}     |\n")
        file.write(f"|       Glider   |      {gliders}     |      {int(percentgliders)}     |\n")
        file.write(f"|    spaceship   |      {LWSs}     |      {int(percentLWSs)}     |\n")
        file.write("____________________________________________\n")
        file.write(f"|        Total   |      {Total}     |              |\n")