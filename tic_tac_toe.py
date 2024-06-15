import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize an empty board
        self.current_winner = None  # Track the winner!

    def print_board(self):
        # Board layout
        print("\nCurrent Board:")
        for i, row in enumerate([self.board[i * 3:(i + 1) * 3] for i in range(3)]):
            print('| ' + ' | '.join(self.color_letter(spot) for spot in row) + ' |')
        print()

    def color_letter(self, letter):
        # Color the board letters
        if letter == 'X':
            return f'\033[91m{letter}\033[0m'  # Red color for AI
        elif letter == 'O':
            return f'\033[94m{letter}\033[0m'  # Blue color for Human
        return letter

    def print_board_nums(self):
        # Board layout with numbers
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        print("\nBoard Positions:")
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(state, player, alpha, beta):
    max_player = 'X'  # AI is trying to maximize (X)
    other_player = 'O' if player == 'X' else 'X'

    # First, check if the previous move is a winner
    if state.current_winner == other_player:
        return {'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}

    elif not state.empty_squares():  # No empty squares
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -math.inf}  # Each score should maximize (be larger)
    else:
        best = {'position': None, 'score': math.inf}  # Each score should minimize

    for possible_move in state.available_moves():
        state.make_move(possible_move, player)
        sim_score = minimax(state, other_player, alpha, beta)  # Simulate a game after making that move

        # Undo move
        state.board[possible_move] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move  # This represents the move optimal next move

        if player == max_player:  # Maximize the max_player (AI)
            if sim_score['score'] > best['score']:
                best = sim_score  # Replace best
            alpha = max(alpha, sim_score['score'])
        else:  # Minimize the other player
            if sim_score['score'] < best['score']:
                best = sim_score  # Replace best
            beta = min(beta, sim_score['score'])

        if beta <= alpha:
            break

    return best

def play():
    game = TicTacToe()
    print("\033[93mWelcome to Tic Tac Toe!\033[0m")

    player_name = input("\033[38;2;255;192;203mPlease enter your name: \033[0m")
    print(f"\n\033[38;2;255;192;203mWelcome, {player_name}!\033[0m")

    game.print_board_nums()

    letter = 'O'  # Starting letter
    while game.empty_squares():
        if letter == 'O':  # Human turn
            square = None
            while square not in game.available_moves():
                square = input('\033[95mEnter your move (0-8): \033[0m')
                try:
                    square = int(square)
                    if square not in game.available_moves():
                        raise ValueError
                except ValueError:
                    print("Invalid move. Try again.")

            game.make_move(square, letter)
            print(f'\033[95m{player_name} moved to square {square}\033[0m')
            game.print_board()

            if game.current_winner:
                print(f'\033[92mCongratulations, {player_name}! {letter} wins!\033[0m')
                return
            letter = 'X'  # Switch player
        else:  # AI turn
            print('\033[95mAI is making a move...\033[0m')
            square = minimax(game, letter, -math.inf, math.inf)['position']
            game.make_move(square, letter)
            print(f'\033[95mAI moved to square {square}\033[0m')
            game.print_board()

            if game.current_winner:
                print(f'\033[92m{letter} wins! Better luck next time, {player_name}.\033[0m')
                return
            letter = 'O'  # Switch player

    print("\033[92mIt's a tie!\033[0m")

if __name__ == '__main__':
    play()
