from alphabeta import TicTacToe
from alphabeta import alpha_beta_value
import time
from math import inf as HUGE_NUMBER


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game (TicTacToe)
    """
    while not state.is_end_state():
        alku = time.time()
        print(state)
        print("Current player:", "X" if state.crosses_turn else "O")

        children = state.generate_children()
        
        best_child = None
        best_value = -HUGE_NUMBER if state.is_max_node() else HUGE_NUMBER

        for child in children:
            child_value = alpha_beta_value(child)
            if state.is_max_node():
                if child_value > best_value:
                    best_value = child_value
                    best_child = child
            else:
                if child_value < best_value:
                    best_value = child_value
                    best_child = child

        state = best_child
        loppu = time.time()
        print("Time:",1000 * (loppu - alku), "ms")
        print("Value:", best_value)
    
    print(state)
    print("Game over!")
    if state.won('x'):
        print("X wins!")
    elif state.won('o'):
        print("O wins!")
    else:
        print("It's a draw!")

def main():
    """You need to implement the following functions/methods:
    play(state): makes turn and prints the result of it until the game is over
    value() in TicTacToe class: returns the current score of the game
    generate_children() in TicTacToe class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    """
    empty_board = 3 * '???'
    state = TicTacToe(empty_board, True)
    print(state)
    play(state)


if __name__ == '__main__':
    main()
