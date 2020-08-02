import pygame

pygame.init()

board = [x for x in range(10)]

get_board_pos = {
    range(200):1,
    range(200,400):2,
    range(400,600):3
}

gety = {
    range(200):1

}

drawpos = {
    1:(0,0)
}

locx = {
    1:((0,0),(200,200),(200,0),(0,200)),
    2:((200,0),(400,200),(400,0),(200,200)),
    3:((400,0),(600,200),(600,0),(400,200)),
    4:((0,200),(200,400),(200,200),(0,400)),
    5:((200,200),(400,400),(400,200),(200,400)),
    6:((400,200),(600,400),(600,200),(400,400)),
    7:((0,400),(200,600),(200,400),(0,600)),
    8:((200,400),(400,600),(400,400),(200,600)),
    9:((400,400),(600,600),(600,400),(400,600))
    }
loco = {
    1:(100,100),
    2:(300,100),
    3:(500,100),
    4:(100,300),
    5:(300,300),
    6:(500,300),
    7:(100,500),
    8:(300,500),
    9:(500,500)
}


GAME_FONT = pygame.font.SysFont('Comic Sans', 300)
WHITE = (255,255,255)
BLACK = (0,0,0)
BORDER = [(0,0),(0,600),(0,600),(600,600),(600,600),(600,0)]
pygame.display.set_caption("Tic Tac Toe")
screen = pygame.display.set_mode((600,600))
screen.fill(WHITE)

pygame.draw.lines(screen,BLACK,True,BORDER,10)
pygame.draw.line(screen,BLACK,(200,0),(200,600),10)
pygame.draw.line(screen,BLACK,(400,0),(400,600),10)
pygame.draw.line(screen,BLACK,(0,200),(600,200),10)
pygame.draw.line(screen,BLACK,(0,400),(600,400),10)

pygame.display.flip()
text = GAME_FONT.render('X',1,BLACK)

def check_space(pos,bo):
    return not bo[pos] in ['X','O']


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


def display_board(bo):
    for pos, mark in enumerate(bo):
        if mark in ['X','O']:
            display_mark(pos,mark)
            pygame.display.flip()


def display_mark(pos,mark):
    if mark == 'X':
        # pygame.draw.line(screen,BLACK,drawpos[pos],drawpos[pos]+200,20)
        pygame.draw.line(screen,BLACK,locx[pos][0],locx[pos][1],20)
        pygame.draw.line(screen,BLACK,locx[pos][2],locx[pos][3],20)
    elif mark == 'O':
        pygame.draw.circle(screen,BLACK,(loco[pos]),90,20)

def get_position(x,y):
    for key in get_board_pos:
        if x in key:
            posx = get_board_pos[key]
        if y in key:
            posy = get_board_pos[key]
    if posy == 1:
        return posx
    elif posy == 2:
        return posx + 3
    else:
        return posx + 6

running = True
player = 'X'
while running:
    display_board(board)
    # pygame.draw.polygon(screen,RED,[(0,0),(200,200),(200,0),(0,200)],10)
    # screen.blit(text,(0,0))
    if check_full_board(board):
        print('Tie Game')
        break
    while player == 'X':

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                board[get_position(x,y)] = 'X'
                player = 'O'
                if check_win_mark(board,'X'):
                    print('Player Wins')
                    display_board(board)
                    pygame.time.delay(3000)
                    running = False
    move = best_move(board)
    if move == 0:
        continue
    board[move] = 'O'
    player = 'X'
    if check_win_mark(board,'O'):
        print('Computer Wins')
        display_board(board)
        pygame.time.delay(3000)
        running = False
