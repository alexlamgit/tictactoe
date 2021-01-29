boardlist = [
    '_', '_', '_',
    '_', '_', '_',
    '_', '_', '_',
]
boardchart = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
]
def printboard():  # Both functions print out the board and reference board in more usual layout.

    print(boardlist[0:3])
    print(boardlist[3:6])
    print(boardlist[6:9])

def printboardchart():
    print(boardchart[0:3])
    print(boardchart[3:6])
    print(boardchart[6:9])

x_wasdoubled = 0
o_wasdoubled = 0

def get_x_move():  # Gets X's move while showing the board for visual support

    global o_wasdoubled
    o_wasdoubled = 0 # Stating the value again to reset

    printboardchart()
    print(' ')
    printboard()
    print(' ')
    print('Time for the X player to make his move! ')
    move_x = int(input('Using the number chart printed above as reference, type the number where you want to play. \n'))
    if boardlist[move_x - 1] != '_': # Checks whether or not the move is legal
        print('Invalid selection. Please try again. ')
        o_wasdoubled = 1  # Indicator for the gamestart function. If is True, can't pass turn
    else:
        boardlist[move_x - 1] = '\u0332'.join('X')
        o_wasdoubled = 0

def get_o_move():  # Gets O's move while showing the board for visual support

    global x_wasdoubled
    x_wasdoubled = 0

    printboardchart()
    print(' ')
    printboard()
    print(' ')
    print('Time for the O player to make his move! ')
    move_o = int(input('Using the number chart printed above as reference, type the number where you want to play. \n'))
    if boardlist[move_o - 1] != '_':
        print('Invalid selection. Please try again. ')
        x_wasdoubled = 1  # Indicator for the gamestart function. If is True, can't pass turn
    else:
        boardlist[move_o - 1] = '\u0332'.join('O')
        x_wasdoubled = 0

o_win = 0
x_win = 0

def checkwin():
    global o_win
    global x_win

    for item in boardlist:
        if boardlist[0: 3] == ['X', 'X', 'X'] or boardlist[3: 6] == ['X', 'X', 'X'] or boardlist[6: 9] == ['X', 'X', 'X'] or boardlist[
            0: 6: 3] == ['X', 'X', 'X'] or boardlist[
            1: 7: 3] == ['X', 'X', 'X'] or boardlist[
            2: 8: 3] == ['X', 'X', 'X'] or boardlist[
            0: 9: 4] == ['X', 'X', 'X'] or boardlist[
            2: 7: 2] == ['X', 'X', 'X']:
            x_win = 1
        elif boardlist[0: 3] == ['O', 'O', 'O'] or boardlist[3: 6] == ['O', 'O', 'O'] or boardlist[6: 9] == ['O', 'O', 'O'] or boardlist[
                0: 6: 3] == ['O', 'O', 'O'] or boardlist[
                1: 7: 3] == ['O', 'O', 'O'] or boardlist[
                2: 8: 3] == ['O', 'O', 'O'] or boardlist[
                0: 9: 4] == ['O', 'O', 'O'] or boardlist[
                2: 7: 2] == ['O', 'O', 'O']:
                o_win = 1


def gamestart():  # Starts

    global o_win
    global x_win

    gameovertie = 0

    print('\n')
    print('*' * 30)
    print('**   Welcome to TicTacToe   **')
    print('*' * 30 + '\n')

    for eachitem in boardlist:

        if boardlist.count('_') == 0:                               #All of the checks to look for a win or a tie
            gameovertie = 1
            printboard()
            break

        checkwin()
        if x_win == 1 or o_win == 1:
            printboard()
            break

        if x_wasdoubled == 0:
            get_x_move()
        else:
            get_o_move()

        if boardlist.count('_') == 0:                               #All of the checks to look for a win or a tie
            gameovertie = 1
            printboard()
            break
        checkwin()
        if x_win == 1 or o_win == 1:
            printboard()
            break

        if o_wasdoubled == 0:
            get_o_move()
        else:
            get_x_move()

    if gameovertie == 1:
        print('The game was a tie! ')
    elif x_win == 1:
        print('X won!')
    elif o_win == 1:
        print('O won!')
gamestart()
