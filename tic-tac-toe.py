# Scenario
# Your task is to write a simple program which pretends to play tic-tac-toe with the user. 
# To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

# the computer (i.e., your program) should play the game using 'X's;
# the user (e.g., you) should play the game using 'O's;
# the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
# all the squares are numbered row by row starting with 1 (see the example session below for reference)
# the user inputs their move by entering the number of the square they choose − the number must be valid,
# i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field
# which is already occupied;
# the program checks if the game is over − there are four possible verdicts: the game should continue, 
# the game ends with a tie, you win, or the computer wins;
# the computer responds with its move and the check is repeated;
# don't implement any form of artificial intelligence − a random field choice made by the computer is good 
# enough for the game.
# The example session with the program may look as follows:

# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 1
# +-------+-------+-------+
# |       |       |       |
# |   O   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 8
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 4
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 7
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# You won!

# Requirements
# Implement the following features:

# the board should be stored as a three-element list, while each element is another three-element list 
# (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:

# board[row][column]


# each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number 
# (such a square is considered free)
# the board's appearance should be exactly the same as the one presented in the example.
# implement the functions defined for you in the editor.

# Drawing a random integer number can be done by utilizing a Python function called randrange(). 
# The example program below shows how to use it (the program prints ten random numbers from 0 to 8).

# Note: the from-import instruction provides access to the randrange function defined within an external 
# Python module callled random.

# from random import randrange

# for i in range(10):
#     print(randrange(8))

from multiprocessing.dummy import freeze_support
from random import randrange
from turtle import st


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print("+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+")
    
    print(("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|\n") * 1, end="")
    print(("|" + " " * 3 + board[0] + " " * 3 + "|" + " " * 3 + board[1] + " " * 3 + "|" + " " * 3 + board[2] + " " * 3 + "|\n") * 1, end="")
    print(("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|\n") * 1, end="")
    
    print("+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+")
    print(("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|\n") * 1, end="")
    print(("|" + " " * 3 + board[3] + " " * 3 + "|" + " " * 3 + board[4] + " " * 3 + "|" + " " * 3 + board[5] + " " * 3 + "|\n") * 1, end="")
    print(("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|\n") * 1, end="")
    
    print("+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+")
    print(("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|\n") * 1, end="")
    print(("|" + " " * 3 + board[6] + " " * 3 + "|" + " " * 3 + board[7] + " " * 3 + "|" + " " * 3 + board[8] + " " * 3 + "|\n") * 1, end="")
    print(("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|\n") * 1, end="")
    
    print("+" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "+")
    
def enter_move():
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    new_move = int(input("Enter your move: "))
    if new_move >= 1 and new_move <= 9 and status_game[new_move -1 ] != "x" and status_game[new_move - 1] != "0":
        status_game[new_move - 1] = "0"
        display_board(status_game)
    else:
        print("Play not allowed")
        enter_move()

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = 9
    for i in range (9): 
        if board[i]=='x' or board[i]=='0':
            free_squares -= 1
    return free_squares

def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0]=='0' and board[1]=='0' and board[2]=='0':
        print('You win!')  
        return False
    elif board[2]=='0' and board[5]=='0' and board[8]=='0':
        print('You win!')  
        return False
    elif board[6]=='0' and board[7]=='0' and board[8]=='0':
        print('You win!')  
        return False
    elif board[0]=='0' and board[3]=='0' and board[6]=='0':
        print('You win!')  
        return False
    
    elif board[0]=='x' and board[1]=='x' and board[2]=='x':
        print('Computer win!')
        return False
    elif board[2]=='x' and board[5]=='x' and board[8]=='x':
        print('Computer win!')
        return False
    elif board[6]=='x' and board[7]=='x' and board[8]=='x':
        print('Computer win!')
        return False
    elif board[0]=='x' and board[3]=='x' and board[6]=='x':
        print('Computer win!')
        return False
    elif board[1]=='x' and board[4]=='x' and board[7]=='x':
        print('Computer win!')
        return False
    elif board[3]=='x' and board[4]=='x' and board[5]=='x':
        print('Computer win!')
        return False
    elif board[0]=='x' and board[4]=='x' and board[8]=='x':
        print('Computer win!')
        return False
    elif board[2]=='x' and board[4]=='x' and board[6]=='x':
        print('Computer win!')
        return False
    
    elif make_list_of_free_fields(status_game) == 0:
        print('Tied game!')
        return False
        
    else:
        return True

def draw_move(board):
    # The function draws the computer's move and updates the board.
    ramdom = True
    iteration = 0
    while ramdom:
        move_ramdom = randrange(0,9)
        if board[move_ramdom -1 ]=='x' or board[move_ramdom - 1]=='0':
            move_ramdom = randrange(0,9)
        else:
            status_game[move_ramdom - 1] = 'x'
            ramdom = False
    print('Computer move:' ,move_ramdom)
    display_board(board)
    
global status_game
status_game = ["1","2","3","4","x","6","7","8","9"] 

display_board(status_game)
while victory_for(status_game):
    victory_for(status_game)
    enter_move()
    draw_move(status_game)