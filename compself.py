from game import minimax, check_win_mark, check_full_board, check_space
import random
import sys

plays = sys.argv[1]


count_wins = 0
count_tie = 0
x_wins = 0
o_wins = 0


def best_move(bo, player):
    if player == 'O':
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
    else:
        best_score = 2
        available_moves = []
        move = 0
        for i, pos in enumerate(bo):
            if check_space(i, bo) and i != 0:
                available_moves.append(i)
        for pos in available_moves:
            old_pos = bo[pos]
            bo[pos] = 'X'
            score = minimax(bo, 'O',-2,2)
            bo[pos] = old_pos
            if score < best_score:
                best_score = score
                move = pos
        return move



for i in range(int(plays)):
    board = [str(x) for x in range(10)]
    while not check_full_board(board):


        board[best_move(board,'X')] = 'X'

        if check_win_mark(board,'X'):
            x_wins += 1
            break

        board[best_move(board,'O')] = 'O'

        if check_win_mark(board,'O'):
            o_wins +=1
            break
        if check_full_board(board):
            count_tie +=1


print(f'X Wins: {x_wins}')
print(f'O Wins: {o_wins}')
print(f'Wins: {x_wins + o_wins}')
print(f'Ties: {count_tie}')
