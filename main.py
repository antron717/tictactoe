
board = [str(x) for x in range(10)]
test_board = ['#','1','2','3','4','X','O','7','8','9']
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
        # try:
        #     int(pos)
        #     if not pos in range(1,10):
        #         pos = 0
        #         continue
        # except:
        #     pos = 0
        #     continue


def comp_choice():
    pass

def check_full_board(board):
    for pos in range(1,10):
        return not check_space(pos,test_board)

def check_win(board,mark):
    pass

def check_space(pos,board):
    return not board[pos] in ['X','O']

draw_board(test_board_full)
print(check_full_board(test_board))
