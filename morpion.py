from player import Player
from computer import Computer
import random

class Morpion:
    def __init__(self, human=True):
        """
        initialize attributes and start the game
        """

        print("Le jeu du morpion")

        # initialize attributs
        self.board = list(range(1,10))
        self.available_squares = list(range(1,10))

        if not human:
            self.players = [Player("0"), Computer("X")]
        else :
            self.players = [Player("0"), Player("X")]

        self.winning_combi = [
            [0, 1, 2],
            [0, 4, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [2, 4, 6],
            [3, 4, 5],
            [6, 7, 8]
        ] # il y a 8 combinaisaons gagnates - on récupère leurs index
        self.current_player = self.players[random.randint(0,1)]
        self.mode = human
        
        # launch game
        self.start_game()

    def start_game(self):
        """
        launch the game with the current state of the board and the current player
        """

        self.print_board()
        choice = self.current_player.choose_square(self.available_squares)
        self.print_choice(choice)

    def print_board(self):
        """
        print the current state of the board
        """
        print('\n')

        for key, i in enumerate(self.board):
            if (key + 1) % 3 == 0:
                print(i)
            else :
                print(i, end =" ")
        print('-----------------')

    def print_choice(self, square):
        """
        print current player choice in the designated square
        """
        self.available_squares.remove(square) 

        square = square - 1 # we have to remove 1 for indexation purposes
        self.board[square] = self.current_player.token # place pawn
        self.check_winner()

    def check_winning_combinations(self):
        """
        check among the winning combinations if the current player has one of them
        """
        
        for square1, square2, square3 in self.winning_combi:
            if self.current_player.token == self.board[square1] == self.board[square2] == self.board[square3]:
                return True
        return False

    def change_player(self):
        # change player for next round
        index = (self.players.index(self.current_player) + 1) % 2
        self.current_player = self.players[index]

    def check_winner(self):
        """
        check if there is a winner, otherwise resume the game
        """

        if self.board.count(self.current_player.token) >= 3:
            if self.check_winning_combinations() :
                self.print_board()
                print("=================\n")
                print(f"{self.current_player.token} a gagné\n")
                print("End of the game")
            else :
                if not self.available_squares:
                    # game finished because all squares are filled
                    self.print_board()
                    print("il n'y a pas de gagant\n")
                    print("End of the game")
                else :
                    # no winning combination, so continue
                    self.change_player()
                    self.start_game()
        else :
            # there isn't enough square filled, so go on
            self.change_player()
            self.start_game()