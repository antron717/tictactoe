# import random
from termcolor import colored
import sys

board = [str(x) for x in range(10)]

def color_mark(bo,i):
    if bo[i] == 'O':
        return colored(bo[i],'red')
    elif bo[i] == 'X':
        return colored(bo[i],'green')
    else:
        return bo[i]

def draw_board(bo):
    i = 1
    print('--+---+---')
    for x in range(1,10,3):

        print(color_mark(bo,i)+" | "+color_mark(bo,i+1)+" | "+color_mark(bo,i+2))
        print("--+---+---")
        i += 3

def player_choice(bo):
    pos = 0
    while not check_space(pos,bo) or pos == 0:
        try:
            pos = int(input('Enter Position (1 to 9): '))
            if not pos in range(1,10):
                pos = 0
                continue
        except:
            pos = 0
            continue
    bo[pos] = 'X'

# old function, before minimax
# def comp_choice(bo):
#     available_moves = []
#     for i, pos in enumerate(bo):
#         if check_space(i,bo) and i != 0:
#             available_moves.append(i)
#
#     if len(available_moves) > 0:
#
#         for pos in available_moves:
#             for mark in ['O','X']:
#                 check_board = list(bo)
#                 check_board[pos] = mark
#                 if check_win(check_board):
#                     bo[pos] = 'O'
#                     print('HERE')
#                     return True
#         else:
#             pos = random.choice(available_moves)
#             bo[pos] = 'O'
#             return True
#     return False

def minimax(bo, player,a,b):
    if check_win_mark(bo,'O'):
        return 1
    elif check_win_mark(bo,'X'):
        return -1
    elif check_full_board(bo):
        return 0
    available_moves = []
    for i, space in enumerate(bo):
        if check_space(i,bo) and i != 0:
            available_moves.append(i)
    if player == 'O':
        best_score = -2
        for pos in available_moves:
            old_pos = bo[pos]
            bo[pos] = 'O'
            score = minimax(bo, 'X',a,b)
            bo[pos] = old_pos
            best_score = max(score,best_score)
            if best_score >= b:
                return best_score
            if best_score > a:
                a = best_score
        return best_score
    else:
        best_score = 2
        for pos in available_moves:
            old_pos = bo[pos]
            bo[pos] = 'X'
            score = minimax(bo, 'O',a,b)
            bo[pos] = old_pos
            best_score = min(score,best_score)
            if best_score <= a:
                return best_score
            if best_score < b:
                b = best_score
        return best_score

def check_win_mark(bo,mark):
    return ((bo[1] == mark and bo[2] == mark and bo[3] == mark) or
    (bo[4] == mark and bo[5] == mark and bo[6] == mark) or
    (bo[7] == mark and bo[8] == mark and bo[9] == mark) or
    (bo[1] == mark and bo[5] == mark and bo[9] == mark) or
    (bo[3] == mark and bo[5] == mark and bo[7] == mark) or
    (bo[1] == mark and bo[4] == mark and bo[7] == mark) or
    (bo[2] == mark and bo[5] == mark and bo[8] == mark) or
    (bo[3] == mark and bo[6] == mark and bo[9] == mark))


def check_full_board(bo):
    for pos in range(1,10):
        if check_space(pos,bo):
            return False
    return True


def check_space(pos,bo):
    return not bo[pos] in ['X','O']


def best_move(bo):
    best_score = -2
    available_moves = []
    move = 0
    for i, pos in enumerate(bo):
        if check_space(i, bo) and i != 0:
            available_moves.append(i)
        for pos in available_moves:
            old_pos = bo[pos]
            bo[pos] = 'O'
            score = minimax(bo, 'X',-2,2)
            bo[pos] = old_pos
            if score > best_score:
                best_score = score
                move = pos
    return move


if __name__ == "__main__":
    while not check_full_board(board):
        draw_board(board)

        player_choice(board)
        if check_win_mark(board,'X'):
            draw_board(board)
            print('Player Wins')
            break
        board[best_move(board)] = 'O'
        if check_win_mark(board,'O'):
            draw_board(board)
            print('Computer Wins')
            break
    else:
         draw_board(board)
         print('Tie Game')
