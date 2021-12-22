"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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

    # Since we are receiving a board, which is a matrix, as an input, we can determine by the number of not EMPTY's
    counter = 0
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == EMPTY:
                counter += 1

    if terminal(board):
        return "Game is already over!"

    if counter % 2 != 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # If element (i, j) is EMPTY, then it is a possible action 
    plays = set()

    for i in range(0, len(board)):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                plays.add((i, j))
        
    if terminal(board):
        return "Game is already over!"

    return plays


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Our output board should be our current board + the action taken in position (i, j)

    # The specification asks us to use a deepcopy of the board in order to use MiniMax
    """
    From https://docs.python.org/3/library/copy.html

    The deepcopy() function avoids these problems by:
    keeping a memo dictionary of objects already copied during the current copying pass; and
    letting user-defined classes override the copying operation or the set of components copied. 
    """

    if action not in actions(board):
        raise Exception("Invalid spot!")

    board_copy = deepcopy(board)

    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check for horizontal wins
    for i in range(0, len(board)):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    # Check for vertical wins
    for i in range(0, len(board)):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    
    # Check for diagonals
    # board[1][1] is a commom element of both diagonals so, if it is not EMPTY, neither of the diagonals are EMPTY
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) and (board[1][1] != EMPTY):
        return board[1][1]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # 2 cases: Board full or winner = True
    counter = 0
    for i in board:
        if EMPTY in i:
            counter += 1
    if counter != 0 and winner(board) is None:
        return False
    elif winner(board) is not None or counter == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else: 
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)

        # Create an array to store all the possible values and actions
        # For every possible action in the current state of the board...
        # Append to the array the min value that an action can result in + the action itself
        # Get the max value from the array according to the first item from the [value, (action)], which would be the value 
        # The move will be the second item from the [value, (action)], which is the action
        # For "O", it's the opposite

    if current_player == X:
        all_values = []

        for action in actions(board):
            all_values.append([Min_Value(result(board, action)), action])

        highest = max(all_values, key=lambda item:item[0])
        move = highest[1]

    elif current_player == O:
        all_values = []

        for action in actions(board):
            all_values.append([Max_Value(result(board, action)), action])

        lowest = min(all_values, key=lambda item:item[0])
        move = lowest[1]

    return move


def Max_Value(board):

    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, Min_Value(result(board, action)))

    return v

def Min_Value(board):

    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, Max_Value(result(board, action)))

    return v

        
"""
Pseudo code from lecture:

Given a state s:
MAX picks action a in Actions(s) that produces highest value of Min-Value(Result(s, a))
MIN picks action a in Actions(s) that produces smallest value of Max-Value(Result(s, a))

function Max-Value(state): 
    if Terminal(state): 
        return Utility(state) 
    v = -inf 
    for action in Actions(state): 
        v = max(v, Min-Value(Result(state, action))) 
    return v

Value v is -infinity and, for every action possible, v is going to be the max value between it's current value and the minimum value that the opponent can get
"""