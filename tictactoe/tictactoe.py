"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if not any(EMPTY in row for row in board):
        return None

    return X if sum(row.count(O) for row in board) == sum(row.count(X) for row in board) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    return None if winner(board) != None else { (row,column) for row in range(len(board)) for column in range(len(board)) if board[row][column] == EMPTY }




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
         raise ValueError

    board_copy = [row.copy() for row in board]
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    winning_lines =[
        [ board[0][0], board[0][1], board[0][2] ],
        [ board[1][0], board[1][1], board[1][2] ],
        [ board[2][0], board[2][1], board[2][2] ],

        [ board[0][0], board[1][0], board[2][0] ],
        [ board[0][1], board[1][1], board[2][1] ],
        [ board[0][2], board[1][2], board[2][2] ],

        [ board[0][0], board[1][1], board[2][2] ],
        [ board[2][0], board[1][1], board[0][2] ],
    ]

    if [X,X,X] in (row for row in winning_lines):
        return X
    if [O,O,O] in (row for row in winning_lines):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return True if winner(board) is not None or player(board) is None else False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_ =  winner(board)
    if winner_ == X: return 1
    elif winner_ == O: return -1
    else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    resulted_actions = []
    for action in actions(board):
        new_board = result(board,action)
        resulted_actions.append((action,value(new_board)))

    best_x = max(resulted_actions, key=lambda item: item[1])[0]
    best_o = min(resulted_actions, key=lambda item: item[1])[0]


    return best_x if player(board) == X else best_o


def value(board):

    if terminal(board):
        return utility(board)

    scores = []
    for action in actions(board):
        new_board = result(board,action)
        scores.append(value(new_board))

    return max(scores) if player(board) == X else min(scores)
