import math


board = [' ' for _ in range(9)]


def print_board():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')


def check_winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8], 
        [0,4,8], [2,4,6]           
    ]
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False

def is_draw(b):
    return ' ' not in b


def get_available_moves(b):
    return [i for i in range(len(b)) if b[i] == ' ']


def minimax(b, depth, is_maximizing, alpha, beta):
    if check_winner(b, 'O'):
        return 1
    if check_winner(b, 'X'):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(b):
            b[move] = 'O'
            eval = minimax(b, depth + 1, False, alpha, beta)
            b[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(b):
            b[move] = 'X'
            eval = minimax(b, depth + 1, True, alpha, beta)
            b[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Enter a number between 1 and 9.")


def play_game():
    print("play Tic-Tac-Toe!")
    print_board()

    while True:
        human_move()
        print_board()
        if check_winner(board, 'X'):
            print("win!")
            break
        if is_draw(board):
            print("draw match!")
            break

        print("opponent")
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
