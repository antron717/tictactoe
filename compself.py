from game import *
import random
import sys

plays = sys.argv[1]


count_wins = 0
count_tie = 0
x_wins = 0
o_wins = 0


# def comp_choice(bo,mark):
#     available_moves = []
#     if mark == 'X':
#         check_pattern = ['X','O']
#     else:
#         check_pattern = ['O','X']
#     for i, pos in enumerate(bo):
#         if check_space(i,bo) and i != 0:
#             available_moves.append(i)
#
#     if len(available_moves) > 0:
#
#         for pos in available_moves:
#             for mark in check_pattern:
#                 check_board = list(bo)
#                 check_board[pos] = mark
#                 if check_win(check_board):
#                     bo[pos] = mark
#                     return True
#         else:
#             pos = random.choice(available_moves)
#             bo[pos] = mark
#             return True
#     return False


for i in range(int(plays)):
    board = [str(x) for x in range(10)]
    while not check_full_board(board):


        board[best_move(board)] = 'X'

        #
        # if not comp_choice(board,'X'):
        #     count_tie += 1
        #     break
        if check_win(board):
            x_wins += 1
            break
        board[best_move(board)] = 'O'
        # if not comp_choice(board,'O'):
        #     count_tie += 1
        #     break
        if check_win(board):
            o_wins +=1
            break
        if check_full_board(board):
            count_tie +=1


print(f'X Wins: {x_wins}')
print(f'O Wins: {o_wins}')
print(f'Wins: {x_wins + o_wins}')
print(f'Ties: {count_tie}')
