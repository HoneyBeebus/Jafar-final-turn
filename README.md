# Calculating the maximum amount on the final turn
Jafar and Aladdin are playing checkers. Jafar has one pawn left and is about to make his final move. Construct a function Solution(B) that calculates the maximum amount of moves possible on the final turn. The board will be of size NxN where N is any integer between (1,30)

## Assumptions
Checkers can only move in the vertical diagonal direction, i.e. up and to the left or up and to the right. In order for a checker to move, there must be an opponent's checker in the respective tile. Additionally, there must be a free space in the same diagonal adjacent to them.
Consider a standard X Y plot. If our checker is located at (2,2), then in order for a move to occur an opponents checker must be at either (3,3) or (1,3) and if that is the case there needs to be a free tile at (4,4) for the tile at (3,3) OR a free tile at (0,4) for the tile at (1,3)

## Structure of Solution
First, a simple function searches through the two diemensional array "B" and finds Jafar's pawn which is represented by an "O". The position of Jafar's pawn is recorded in a dictionary as two entries "xCoord" and "yCoord"
Next, a recursive function "findMaxMove" is called. To start, the function checks to see if Jafar's pawn is in the two topmost rows. If so, the function returns 0. After checking to see if Jafar's pawn is at the top, the function then checks to see if Jafar's pawn is located on either the extreme left or right of the board. By "extreme left or right" I mean the last two columns on either the left or right side. This is useful because there is only one valid direction for moves if the pawn is located in the extremes and we can utilize this information to save time by not checking in the directions unpermitted by these location.
If the pawn is not located on any extremes, the function assess to see if a valid move is available. If so, the move is made, xCoord and yCoord are adjusted to reflect the new location, and maxMove is incremented by one. 
Finally, the function calls itself again passing in the updated dictionary and maxMove. This process repeats untill there is not a valid move to be made.

## Test Cases
Test cases are as follows:

A. 5x5 board with no movement possible, expected value is 0
B. 5x5 board with one move available, expected value = 1
C. 5x5 board with Jafar in the vertical extremes, expected value = 0
D. 5x5 board with Jafar in the leftmost column and no valid move, expected value = 0
E. 5x5 board with Jafar in the leftmost column and a single valid move, expected value = 1
F. 5x5 board with Jafar in the rightmost column and a single valid move, expected v alue = 1
G. 5x5 board with Jafar starting in prime position for maximum amount of moves on a 5x5 board, expected value = 2
H. 2x2 board with no valid moves available, expected value = 0
I. 1x1 board with no valid moves available, expected value = 0
J. 10x10 board, larger board, one move available, expected value = 1
K. 3x3 board, minimum sized board for at least one valid move, expected value = 1

## Running
Compile with python3 interpreter of choice. By default test cases are commented out. To run test cases, uncomment testCases() at the bottom of the file. 

:)
