TEMPLATE_FIELD = '|e|e|e|\n|e|e|e|\n|e|e|e|\n'
from math import inf
HUGE_NUMBER = inf


class AlphaBetaNode(object):
    def __init__(self):
        pass

    def generate_children(self):
        pass

    def is_max_node(self):
        pass

    def is_end_state(self):
        pass

    def value(self):
        pass


class TicTacToe(AlphaBetaNode):
    """Class that contains current state of the game and implements AlphaBetaNode methods
    :attr state: Current state of the board (str)
    :attr state: Indicates whose turn it is (Boolean)
    """

    def __init__(self, state, crosses_turn):
        super().__init__()
        self.state = state
        self.crosses_turn = crosses_turn

    def is_end_state(self):
        return ('?' not in self.state) or self.won('x') or self.won('o')

    def won(self, c):
        triples = [self.state[0:3], self.state[3:6], self.state[6:9], self.state[::3], self.state[1::3],
                   self.state[2::3], self.state[0] + self.state[4] + self.state[8],
                   self.state[2] + self.state[4] + self.state[6]]
        combo = 3 * c
        return combo in triples

    def __str__(self):
        field = TEMPLATE_FIELD
        for c in self.state:
            field = field.replace('e', c, 1)

        return field

    def is_max_node(self):
        return self.crosses_turn

    def generate_children(self):
        """
        Generates list of all possible states after this turn
        :return: list of TicTacToe objects
        """

        children = []
        symbol = 'x' if self.crosses_turn else 'o'
        
        for i in range(len(self.state)):
            if self.state[i] == '?':
                new_state = self.state[:i] + symbol + self.state[i+1:]
                children.append(TicTacToe(new_state, not self.crosses_turn))
        
        return children

    def value(self):
        if self.won('x'):
            return 1
        elif self.won('o'):
            return -1
        else:
            return 0

def alpha_beta_value(node):
    """Implements the MinMax algorithm with alpha-beta pruning
    :param node: State of the game (TicTacToe)
    :return: int
    """
    if node.is_max_node():
        return max_value(node, -HUGE_NUMBER, HUGE_NUMBER)
    else:
        return min_value(node, -HUGE_NUMBER, HUGE_NUMBER)

def max_value(node, alpha, beta):
    # Implement me
    if node.is_end_state():
        return node.value()
    
    value = -HUGE_NUMBER
    for child in node.generate_children():
        value = max(value, min_value(child, alpha, beta))
        if value >= beta:
            return value
        alpha = max(alpha, value)
    
    return value

def min_value(node, alpha, beta):
    # Implement me
    if node.is_end_state():
        return node.value()
    
    value = HUGE_NUMBER
    for child in node.generate_children():
        value = min(value, max_value(child, alpha, beta))
        if value <= alpha:
            return value
        beta = min(beta, value)
    
    return value
