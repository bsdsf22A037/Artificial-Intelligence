
class Minimax:
    def __init__(self, game_state):
        self.game_state = game_state

    def is_terminal(self, state):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if state[condition[0]] == state[condition[1]] == state[condition[2]] != ' ':
                return True
        return ' ' not in state

    def utility(self, state):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if state[condition[0]] == state[condition[1]] == state[condition[2]] == 'X':
                return 1
            elif state[condition[0]] == state[condition[1]] == state[condition[2]] == 'O':
                return -1
        return 0

    def minimax(self, state, depth, maximizing_player):
        if self.is_terminal(state):
            return self.utility(state)

        if maximizing_player:
            max_eval = -float('inf')
            for i in range(len(state)):
                if state[i] == ' ':
                    state[i] = 'X'
                    eval = self.minimax(state, depth + 1, False)
                    state[i] = ' '
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(len(state)):
                if state[i] == ' ':
                    state[i] = 'O'
                    eval = self.minimax(state, depth + 1, True)
                    state[i] = ' '
                    min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, state):
        best_val = -float('inf')
        best_move = None
        for i in range(len(state)):
            if state[i] == ' ':
                state[i] = 'X'
                move_val = self.minimax(state, 0, False)
                state[i] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = i
        return best_move

game_state = ['X', 'O', 'X', ' ', 'O', ' ', ' ', ' ', ' ']
minimax_solver = Minimax(game_state)
best_move = minimax_solver.best_move(game_state)
print(f"Best move is at index: {best_move}")
