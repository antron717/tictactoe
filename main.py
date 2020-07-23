
board = [str(x) for x in range(10)]
test_board = ['#','O','X','X','4','X','X','7','8','X']
test_board_full = ['X' for x in range(10)]

def draw_board(board):
    i = 1
    print('----------')
    for x in range(1,10,3):
        print(board[i]+" | "+board[i+1]+" | "+board[i+2])
        print("----------")
        i += 3

def player_choice():
    pos = 0
    while not check_space(pos,test_board) or pos == 0:
        try:
            pos = int(input('Enter Position (1 to 9): '))
            if not pos in range(1,10):
                pos = 0
                continue
        except:
            pos = 0
            continue


def comp_choice():
    pass

def check_full_board(board):
    for pos in range(1,10):
        if check_space(pos,board):
            return False
    return True

def check_win(board):
    return ((board[1] == board[2] == board[3]) or
    (board[4] == board[5] == board[6]) or
    (board[7] == board[8] == board[9]) or
    (board[1] == board[5] == board[9]) or
    (board[3] == board[5] == board[7]) or
    (board[1] == board[4] == board[7]) or
    (board[2] == board[5] == board[8]) or
    (board[3] == board[6] == board[9]))

def check_space(pos,board):
    return not board[pos] in ['X','O']

draw_board(test_board)
print(check_full_board(test_board_full))
