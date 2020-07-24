import random
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

def comp_choice(bo):
    available_moves = []
    for i, pos in enumerate(bo):
        if check_space(i,bo) and i != 0:
            available_moves.append(i)

    if len(available_moves) > 0:

        for pos in available_moves:
            for mark in ['O','X']:
                check_board = list(bo)
                check_board[pos] = mark
                if check_win(check_board):
                    bo[pos] = 'O'
                    print('HERE')
                    return True
        else:
            pos = random.choice(available_moves)
            bo[pos] = 'O'
            return True
    return False




def check_full_board(bo):
    for pos in range(1,10):
        if check_space(pos,bo):
            return False
    return True

def check_win(bo):
    return ((bo[1] == bo[2] == bo[3]) or
    (bo[4] == bo[5] == bo[6]) or
    (bo[7] == bo[8] == bo[9]) or
    (bo[1] == bo[5] == bo[9]) or
    (bo[3] == bo[5] == bo[7]) or
    (bo[1] == bo[4] == bo[7]) or
    (bo[2] == bo[5] == bo[8]) or
    (bo[3] == bo[6] == bo[9]))

def check_space(pos,bo):
    return not bo[pos] in ['X','O']


if __name__ == "__main__":
    while not check_full_board(board):

        draw_board(board)

        player_choice(board)
        if  check_win(board):
            draw_board(board)
            print('Player Wins')
            break

        if not comp_choice(board):
            draw_board(board)
            print('Tie Game')
            break
        if check_win(board):
            draw_board(board)
            print('Computer Wins')
            break

    else:
        draw_board(board)
        print('Tie Game')
