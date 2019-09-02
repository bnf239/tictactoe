import math
import turtle
import time
import random

# This list represents the board. It's a list
# of nine strings, each of which is either
# "X", "O", "_", representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.
global the_board
the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]
indexes = [[-300,100,-300,300],[-100,100,-100,300],[100,100,100,300]
           ,[-300,-100,-300,100],[-100,-100,-100,100],[100,-100,100,100],
           [-300,-300,-300,-100],[-100,-300,-100,-100],[100,-300,100,-100]]
indexes2 = [[-300,-100,100,300],[-100,100,100,300],[100,300,100,300],
            [-300,-100,-100,100],[-100,100,-100,100],[100,300,-100,100],
            [-300,-100,-300,-100],[-100,100,-300,-100],[100,300,-300,-100]]
def draw_board(board):
    """
    signature: list(str) -> NoneType
    Given the current state of the game, draws
    the board on the screen, including the
    lines and the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.clear()
    turtle.color('black')
    turtle.penup()
    turtle.goto(-100,300)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(100,300)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(-300,100)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(-300,-100)
    turtle.pendown()
    turtle.forward(600)
    for i in range(len(board)):
        if board[i] == 'X':
            turtle.color('green')
            turtle.penup()
            turtle.goto(indexes[i][0],indexes[i][1])
            turtle.left(45)
            turtle.pendown()
            turtle.forward(math.sqrt(80000))
            turtle.penup()
            turtle.goto(indexes[i][2],indexes[i][3])
            turtle.left(-90)
            turtle.pendown()
            turtle.forward(math.sqrt(80000))
            turtle.left(45)
        elif board[i]== "O":
            turtle.color('red')
            turtle.penup()
            turtle.goto(indexes[i][0]+100,indexes[i][1])
            turtle.pendown()
            turtle.circle(100, 360) 
    turtle.update()
    

def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    Given a list representing the state of the board
    and an x,y screen coordinate pair indicating where
    the user clicked, update the board
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool indicated if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """
    print("user clicked at "+str(x)+","+str(y))
    for i in range(len(board)):
        if indexes2[i][0]<=x<= indexes2[i][1] and indexes2[i][2]<=y<=indexes2[i][3]:
            if board[i]=="_":
                board[i]='O'
                return True
            elif board[i]=="X":
                return False
            

def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    if board[0]== board[1] and board[0]==board[2]:
        if board[0]=="X":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("Computer Won! You Lost :(", True,"center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        elif board[0]=="O":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("YOU WON!!!!:)",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        else:
            return False
            
    elif board[0]==board[4] and board[0]==board[8]:
        if board[0]=="X":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("Computer Won! You Lost :(",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        elif board[0]=="O":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("YOU WON!!!!:)",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        else:
            return False
    elif board[2]==board[5]and board[2]==board[8]:
        if board[2]=="X":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("Computer Won! You Lost :(", True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        elif board[2]=="O":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("YOU WON!!!!:)",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        else:
            return False
    elif board[2]==board[4]and board[2]==board[6]:
        if board[2]=="X":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("Computer Won! You Lost :(",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        elif board[2]=="O":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("YOU WON!!!!:)",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
    elif board[3]==board[4]and board[3]==board[5]:
        if board[3]=="X":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("Computer Won! You Lost :(",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        elif board[3]=="O":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("YOU WON!!!!:)",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
    elif board[1]==board[4]and board[1]==board[7]:
        if board[1]=="X":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("Computer Won! You Lost :(",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        elif board[1]=="O":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("YOU WON!!!!:)",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
    if board[6]==board[7]and board[6]==board[8]:
        if board[6]=="X":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("Computer Won! You Lost :(", True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        elif board[6]=="O":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("YOU WON!!!!:)",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
    elif board[0]==board[3]and board[0]==board[6]:
        if board[0]=="X":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("Computer Won! You Lost :(",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
        elif board[0]=="O":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.write("YOU WON!!!!:)",True,align="center",font=("Arial", 16, "bold"))
            for i in range(len(board)):
                board[i]="_"
            return True
    count = 0
    for i in range(len(board)):
        if board[i] != "_":
            count+=1
    if count ==len(board):
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        turtle.write("NO WINNER!",True,"center",font=("Arial", 16, "bold"))
        for i in range(len(board)):
            board[i]="_"
        return True
    return False
            
def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    #possibilities = [['X','X','_'],['_','X','X'],['X','_','X']]
    boardindex = [[0,1,2],[0,4,8],[3,4,5],[6,7,8],[1,4,7],[0,3,6],[2,4,6],[2,5,8]]
    
    #if it is possible for the computer to win in one move, it must do so
    
    
    if board[0]=='X' and board[1]=='X' and board[2]=='_':
        print('1')
        board[2]='X'
    elif board[0]=='X' and board[1]=='_' and board[2]=='X':
        print('2')
        board[1]='X'
    elif board[0]=='_' and board[1]=='X' and board[2]=='X':
        print('3')
        board[0]='X'
    elif board[0]=='X' and board[4]=='X' and board[8]=='_':
        print('4')
        board[8]='X'
    elif board[0]=='X' and board[4]=='_' and board[8]=='X':
        print('5')
        board[4]='X'
    elif board[0]=='_' and board[4]=='X' and board[8]=='X':
        print('6')
        board[0]='X'

    elif board[3]=='X' and board[4]=='X' and board[5]=='_':
        print('7')
        board[5]='X'
    elif board[3]=='X' and board[4]=='_' and board[5]=='X':
        print('8')
        board[4]='X'
    elif board[3]=='_' and board[4]=='X' and board[5]=='X':
        print('9')
        board[3]='X'

    elif board[6]=='X' and board[7]=='X' and board[8]=='_':
        print('10')
        board[8]='X'
    elif board[6]=='X' and board[7]=='_' and board[8]=='X':
        print('11')
        board[7]='X'
    elif board[6]=='_' and board[7]=='X' and board[8]=='X':
        print('12')
        board[6]='X'

    elif board[1]=='X' and board[4]=='X' and board[7]=='_':
        print('13')
        board[7]='X'
    elif board[1]=='X' and board[4]=='_' and board[7]=='X':
        print('14')
        board[4]='X'
    elif board[1]=='_' and board[4]=='X' and board[7]=='X':
        print('15')
        board[1]='X'

    elif board[0]=='X' and board[3]=='X' and board[6]=='_':
        print('16')
        board[6]='X'
    elif board[0]=='X' and board[3]=='_' and board[6]=='X':
        print('17')
        board[3]='X'
    elif board[0]=='_' and board[3]=='X' and board[6]=='X':
        print('18')
        board[0]='X'

    elif board[2]=='X' and board[4]=='X' and board[6]=='_':
        print('19')
        board[6]='X'
    elif board[2]=='X' and board[4]=='_' and board[6]=='X':
        print('20')
        board[4]='X'
    elif board[2]=='_' and board[4]=='X' and board[6]=='X':
        print('21')
        board[2]='X'

    elif board[2]=='X' and board[5]=='X' and board[8]=='_':
        print('22')
        board[8]='X'
    elif board[2]=='X' and board[5]=='_' and board[8]=='X':
        print('23')
        board[5]='X'
    elif board[2]=='_' and board[5]=='X' and board[8]=='X':
        print('24')
        board[2]='X'
        
    #if the human player is able to win in th next move, the computer must try to block it.
       
    elif board[0]=='O' and board[1]=='O' and board[2]=='_':
        print('25')
        board[2]='X'
    elif board[0]=='O' and board[1]=='_' and board[2]=='O':
        print('26')
        board[1]='X'
    elif board[0]=='_' and board[1]=='O' and board[2]=='O':
        print('27')
        board[0]='X'
    elif board[0]=='O' and board[4]=='O' and board[8]=='_':
        print('28')
        board[8]='X'
    elif board[0]=='O' and board[4]=='_' and board[8]=='O':
        print('29')
        board[4]='X'
    elif board[0]=='_' and board[4]=='O' and board[8]=='O':
        print('30')
        board[0]='X'

    elif board[3]=='O' and board[4]=='O' and board[5]=='_':
        print('31')
        board[5]='X'
    elif board[3]=='O' and board[4]=='_' and board[5]=='O':
        print('32')
        board[4]='X'
    elif board[3]=='_' and board[4]=='O' and board[5]=='O':
        print('33')
        board[3]='X'

    elif board[6]=='O' and board[7]=='O' and board[8]=='_':
        print('34')
        board[8]='X'
    elif board[6]=='O' and board[7]=='_' and board[8]=='O':
        print('35')
        board[7]='X'
    elif board[6]=='_' and board[7]=='O' and board[8]=='O':
        print('36')
        board[6]='X'

    elif board[1]=='O' and board[4]=='O' and board[7]=='_':
        print('37')
        board[7]='X'
    elif board[1]=='O' and board[4]=='_' and board[7]=='O':
        print('38')
        board[4]='X'
    elif board[1]=='_' and board[4]=='O' and board[7]=='O':
        print('39')
        board[1]='X'

    elif board[0]=='O' and board[3]=='O' and board[6]=='_':
        print('40')
        board[6]='X'
    elif board[0]=='O' and board[3]=='_' and board[6]=='O':
        print('41')
        board[3]='X'
    elif board[0]=='_' and board[3]=='O' and board[6]=='O':
        print('42')
        board[0]='X'

    elif board[2]=='O' and board[4]=='O' and board[6]=='_':
        print('43')
        board[6]='X'
    elif board[2]=='O' and board[4]=='_' and board[6]=='O':
        print('44')
        board[4]='X'
    elif board[2]=='_' and board[4]=='O' and board[6]=='O':
        print('45')
        board[2]='X'
    elif board[2]=='O' and board[5]=='O' and board[8]=='_':
        print('46')
        board[8]='X'
    elif board[2]=='O' and board[5]=='_' and board[8]=='O':
        print('47')
        board[5]='X'
    elif board[2]=='_' and board[5]=='O' and board[8]=='O':
        print('48')
        board[2]='X'
    #the computer's next move may be any random valid position
    elif True:
        print('49')
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        print(x,y)
        i = 0
        while i < len(board):
            if indexes2[i][0]<=x<= indexes2[i][1] and indexes2[i][2]<=y<=indexes2[i][3]:
                if board[i]=="_":
                    board[i]='X'
                    break
                    return True
                elif board[i]=='O' or board[i]=='X':
                    x = random.randint(-300,300)
                    y = random.randint(-300,300)
                    i=0
            else:
                i+=1
           # print(x,y)
def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    print('Before user move',the_board)
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        print('After user move',the_board)
        if not check_game_over(the_board):
            print('Before computer move',the_board)
            do_computer_move(the_board)
            draw_board(the_board)
            print('After computer move',the_board)
            check_game_over(the_board)
            print('After game checked',the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.setup(700,700)
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()

main()
