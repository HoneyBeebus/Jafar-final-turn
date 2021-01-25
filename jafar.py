###################################################################
#______                          _                  __            #
#| ___ \                        | |                / _|           #
#| |_/ / __ ___  _ __   ___ _ __| |_ _   _    ___ | |_            #
#|  __/ '__/ _ \| '_ \ / _ \ '__| __| | | |  / _ \|  _|           #
#| |  | | | (_) | |_) |  __/ |  | |_| |_| | | (_) | |             #
#\_|  |_|  \___/| .__/ \___|_|   \__|\__, |  \___/|_|             #
#               | |                   __/ |                       #
#               |_|                  |___/                        #
# _____     _   _                         _    _ _     _ _        #
#/  __ \   | | | |                       | |  | | |   (_) |       #
#| /  \/   | |_| | ___ _ __  _ __ _   _  | |  | | |__  _| |_ ___  #
#| |       |  _  |/ _ \ '_ \| '__| | | | | |/\| | '_ \| | __/ _ \ #
#| \__/\_  | | | |  __/ | | | |  | |_| | \  /\  / | | | | ||  __/ #
# \____(_) \_| |_/\___|_| |_|_|   \__, |  \/  \/|_| |_|_|\__\___| #
#                                  __/ |                          #
#                                 |___/                           #
###################################################################

#Function used to find the x and y coordinates of Jafar's pawn
def findJafar(B):
    jafar = dict()
    jafar['xCoord'] = 0
    jafar['yCoord'] = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j] == "O":
                jafar['yCoord'] = i
                jafar['xCoord'] = j
    return jafar    


#Recursive algorithm that calculates the number of max moves Jafar can perform on his last turn
def calcMaxMove(B, jafar, maxMove):
    
    #BASE CASE
    #If Jafar's pawn is in the top, or second from the top row. There are no valid moves.
    if (jafar['yCoord'] <= 1):
        return (maxMove)
    
    #If Jafar's pawn is not in the topmost rows, there may be valid moves
    else:
        #If Jafar's pawn is in the leftmost column OR the second from the leftmost column, we only have to check the tile up and to the right
        if (jafar['xCoord'] <= 1):
            #If the tile up and to the right has one of Alladin's pieces
            if (B[jafar['xCoord'] + 1][jafar['yCoord'] - 1] == "X"):
                #If the tile up and to the right of Alladin's piece is free
                if (B[jafar['yCoord'] - 2][jafar['xCoord'] + 2] != "X"):
                    #Make the move!
                    jafar['xCoord'] += 2
                    jafar['yCoord'] -= 2
                    #Increment the maxMove counter
                    maxMove += 1
                    #Recursive call, checks if there are any more valid moves in the new position
                    maxMove = calcMaxMove(B, jafar, maxMove)
                    #After recursive call, return maxMove
                    return (maxMove)
                #If the tile up and to the right of Alladin's piece is occupied
                else:
                    return(maxMove)
            #If the tile up and to the right is empty
            else:
                return (maxMove)
        
        
        #If Jafar's pawn is in the rightmost column OR the second from the rightmost column, we only have to check the tile up and to the left
        elif (jafar['xCoord'] >= (len(B) - 2)):
            #If the tile up and to the left has one of Alladin's pieces
            if (B[jafar['yCoord'] - 1][jafar['xCoord'] - 1] == "X"):
                #If the tile up and to the left of Alladin's piece is free
                if (B[jafar['yCoord'] - 2][jafar['xCoord'] - 2] != "X"):
                    #Make the move!
                    jafar['xCoord'] -= 2
                    jafar['yCoord'] -= 2
                    #Increment the maxMove counter
                    maxMove += 1
                    #Recursive call, checks if there are any more valid moves in the new position
                    maxMove = calcMaxMove(B, jafar, maxMove)
                    #After recursive call, return maxMove
                    return (maxMove)
                #If the tile up and to the left of Alladin's piece is occupied
                else:
                    return(maxMove)
            #If the tile up and to the left is empty
            else:
                return (maxMove)
        
        
        #Jafar's pawn is not on the extremes of the board
        else:
            #If the tile up and to the right has one of Alladin's pieces
            if (B[jafar['xCoord'] + 1][jafar['yCoord'] - 1] == "X"):
                #If the tile up and to the right of Alladin's piece is free
                if (B[jafar['xCoord'] + 2][jafar['yCoord'] - 2] != "X"):
                    #Make the move!
                    jafar['xCoord'] += 2
                    jafar['yCoord'] -= 2
                    #Increment the maxMove counter
                    maxMove += 1
                    #Recursive call, checks if there are any more valid moves in the new position
                    maxMove = calcMaxMove(B, jafar, maxMove)
                    #After recursive call, return maxMove
                    return (maxMove)
                #If the tile up and to the right of Alladin's piece is occupied
                else:
                    return(maxMove)
            #If the tile up and to the left has one of Alladin's pieces
            elif (B[jafar['yCoord'] - 1][jafar['xCoord'] - 1] == "X"):
                #If the tile up and to the left of Alladin's piece is free
                if (B[jafar['yCoord'] - 2][jafar['xCoord'] - 2] != "X"):
                    #Make the move!
                    jafar['xCoord'] -= 2
                    jafar['yCoord'] -= 2
                    #Increment the maxMove counter
                    maxMove += 1
                    #Recursive call, checks if there are any more valid moves in the new position
                    maxMove = calcMaxMove(B, jafar, maxMove)
                    #After recursive call, return maxMove
                    return (maxMove)
                #If the tile up and to the left of Alladin's piece is occupied
                else:
                    return(maxMove)
            #If the tile up and to the left is empty
            else:
                return (maxMove)


#Driving function
def solution(B):
    # write your code in Python 3.6
    #Find jafar's pawn and record the x and y coordinates
    jafar = findJafar(B)
    #Initialize a variable to keep track of maximum moves. Default value is 0
    maxMove = 0
    #Calculate maxMove
    maxMove = calcMaxMove(B, jafar, maxMove)
    return maxMove





##################################################
# _____         _     _____                      #
#|_   _|       | |   /  __ \                     #
#  | | ___  ___| |_  | /  \/ __ _ ___  ___  ___  #
#  | |/ _ \/ __| __| | |    / _` / __|/ _ \/ __| #
#  | |  __/\__ \ |_  | \__/\ (_| \__ \  __/\__ \ #
#  \_/\___||___/\__|  \____/\__,_|___/\___||___/ #
##################################################                                             


#Function used for testing
def testCases ():
    print("")
    print("")
    print("RUNNING/////")
    print("")
    print("------------------")
    #Temporary variable to hold results of solution for each test. Compared to expected value to determine pass or fail
    temp = 0

    #Variables to keep track of number of failed and passed tests
    numPass = 0
    numFail = 0
    
    #5x5 board with no movement, expected value = 0
    A = ['...X.', '.X...', '.O...', '...X.', '.....']
    temp = solution(A)
    if (temp == 0):
        print("Test A: PASSED")
        numPass += 1
    else:
        print("Test A: FAILED!")
        numFail += 1


    #5x5 board with one move availble, expected value = 1
    B = ['.X...', '.X...', '..O..', '...X.', '.....']
    temp = solution(B)
    if (temp == 1):
        print("Test B: PASSED")
        numPass += 1
    else:
        print("Test B: FAILED!")
        numFail += 1


    #5x5 board with Jafar in the vertical extremes, expected value = 0
    C = ['.X...', '..O..', '..X..', '...X.', '.....']
    temp = solution(C)
    if (temp == 0):
        print("Test C: PASSED")
        numPass += 1
    else:
        print("Test C: FAILED!")
        numFail += 1


    #5x5 board with Jafar in leftmost column and no valid move, expected value = 0
    D = ['..X..', '.X...', 'O....', '...X.', '.....']
    temp = solution(D)
    if (temp == 0):
        print("Test D: PASSED")
        numPass += 1
    else:
        print("Test D: FAILED!")
        numFail += 1


    #5x5 board with Jafar in leftmost column and a valid move, expected value = 1
    E = ['...X.', '.X...', 'O....', '...X.', '.....']
    temp = solution(E)
    if (temp == 1):
        print("Test E: PASSED")
        numPass += 1
    else:
        print("Test E: FAILED!")
        numFail += 1


    #5x5 board with Jafar in rightmost column and a valid move, expected value = 1
    F = ['.X...', '...X.', '....O', '...X.', '.....']
    temp = solution(F)
    if (temp == 1):
        print("Test F: PASSED")
        numPass += 1
    else:
        print("Test F: FAILED!")
        numFail += 1


    #5x5 board with Jafar starting in prime position for max moves on a 5x5 board, expected value = 2
    G = ['.X...', '...X.', '....X', '.X...', 'O....']
    temp = solution(G)
    if (temp == 2):
        print("Test G: PASSED")
        numPass += 1
    else:
        print("Test G: FAILED!")
        numFail += 1


    #2x2 board, no valid moves should be allowed, expected value = 0
    H = ['.X','O.']
    temp = solution(H)
    if (temp == 0):
        print("Test H: PASSED")
        numPass += 1
    else:
        print("Test H: FAILED!")
        numFail += 1


    #1x1 board, no valid moves should be allowed, expected value = 0
    I = ['O']
    temp = solution(I)
    if (temp == 0):
        print("Test I: PASSED")
        numPass += 1
    else:
        print("Test I: FAILED!")
        numFail += 1


    #10x10 board, large board. expected value = 1
    J = ['..........', '..........', '..X.......', '..........', '..X.......', '..........', '..X.......', '..........', '..X.......', '...O......']
    temp = solution(J)
    if (temp == 1):
        print("Test J: PASSED")
        numPass += 1
    else:
        print("Test J: FAILED!")
        numFail += 1

    #3x3 board, minimum board size needed for a valid move, expected value = 1
    K = ['...', '.X.', 'O..']
    temp = solution(K)
    if (temp == 1):
        print("Test K: PASSED")
        numPass += 1
    else:
        print("Test K: FAILED!")
        numFail += 1

    print("------------------")
    print("")
    print("Total PASSED: ", numPass)
    print("Total FAILED: ", numFail)

#Uncomment to run test cases
#testCases()