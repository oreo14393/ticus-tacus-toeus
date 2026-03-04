import random
import os

# Company Branding
COMPANY_NAME = "Toes Games"
WELCOME_MESSAGE = f"Welcome to {COMPANY_NAME} - Tic-Tac-Toe"

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.player = 'X'
        self.ai = 'O'
        self.game_over = False
        self.winner = None

    def display_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n Positions: 1-9\n")

    def player_turn(self):
        while True:
            try:
                position = int(input("Your move (1-9): ")) - 1
                if position < 0 or position > 8:
                    print("Invalid position. Choose 1-9.")
                    continue
                if self.board[position] != ' ':
                    print("Square already taken.")
                    continue
                self.board[position] = self.player
                break
            except ValueError:
                print("Enter a number between 1-9.")

    def ai_turn(self):
        available = [i for i in range(9) if self.board[i] == ' ']
        position = random.choice(available)
        self.board[position] = self.ai
        print(f"AI chose position {position + 1}")

    def check_winner(self, symbol):
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.board[i] == symbol for i in combo) for combo in winning_combos)

    def check_draw(self):
        return all(cell != ' ' for cell in self.board)

    def play(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"\n{'='*40}")
        print(f"  {WELCOME_MESSAGE}")
        print(f"  Play as {self.player} vs AI ({self.ai})")
        print(f"{'='*40}\n")

        while not self.game_over:
            self.display_board()
            self.player_turn()
            
            if self.check_winner(self.player):
                self.display_board()
                print(" You win!")
                self.game_over = True
                break
            
            if self.check_draw():
                self.display_board()
                print(" It's a draw!")
                self.game_over = True
                break
            
            print("AI is thinking...")
            self.ai_turn()
            
            if self.check_winner(self.ai):
                self.display_board()
                print(" AI wins!")
                self.game_over = True
                break
            
            if self.check_draw():
                self.display_board()
                print(" It's a draw!")
                self.game_over = True

    def replay(self):
        while True:
            choice = input("\nPlay again? (R)estart or (Q)uit: ").upper()
            if choice == 'R':
                return True
            elif choice == 'Q':
                print(f"Thanks for playing {COMPANY_NAME} Tic-Tac-Toe!")
                return False
            else:
                print("Invalid input. Enter R or Q.")

def main():
    while True:
        game = TicTacToe()
        game.play()
        if not game.replay():
            break

if __name__ == "__main__":
    main()
