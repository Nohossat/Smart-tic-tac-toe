import random
from exceptions import ValueTooSmallError, ValueTooBigError

class Morpion:
    def __init__(self, human=True):
        """
        initialize attributes and start the game
        """

        print("Le jeu du morpion")

        # initialize attributs
        self.board = ["*"] * 9 
        self.available_squares = list(range(1,10))
        self.players = ["0", "X"]
        self.winning_combi = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
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

        if self.mode: # when True, play verses human
            self.get_human_choice()
        else :
            if self.current_player == "0":
                self.get_computer_choice()
            else :
                self.get_human_choice()

    def print_board(self):
        """
        print the current state of the board
        """
        print('')

        for key, i in enumerate(self.board):
            if (key + 1) % 3 == 0:
                print(i)
            else :
                print(i, end =" ")
        print('')
        print('-----------------')

    def get_human_choice(self):
        """
        allow human being to fill a square, input validation also included
        """
        print(f"Joueur {self.current_player}, à toi de jouer : ")

        while True:
            try:
                choice = int(input("Dans quelle case, tu veux placer ton pion (entre 1 et 9): "))

                if choice > 9 :
                    raise ValueTooBigError
                elif choice < 0:
                    raise ValueTooSmallError

                if choice in self.available_squares: 
                    self.print_choice(choice)
                    break
                else : 
                    print("Case non disponible : il faut en choisir une autre")

            except ValueError as e:
                print("Votre choix doit être une valeur numérique, comprise entre 1 et 9")
            except ValueTooSmallError as e:
                print("Votre choix doit être un chiffre supérieur à 0")
            except ValueTooBigError as e:
                print("Votre choix doit être un chiffre inférieur à 9")

    def get_computer_choice(self):
        """
        random choice among available squares by computer
        """
        print(f"Joueur {self.current_player} (Computer) ")
        choice = random.choice(self.available_squares)
        self.print_choice(choice)

    def print_choice(self, square):
        """
        print current player choice in the designated square
        """
        self.available_squares.remove(square)

        square = square - 1 # we have to remove 1 for indexation purpose
        self.board[square] = self.current_player
        self.check_winner()

    def check_winning_combinations(self):
        """
        check among the winning combinations if the current player has one of them
        """
        for square1, square2, square3 in self.winning_combi:
            if self.current_player == self.board[square1] == self.board[square2] == self.board[square3]:
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
        
        if self.board.count(self.current_player) >= 3:
            if self.check_winning_combinations() :
                self.print_board()
                print("=================")
                print('')
                print(f"{self.current_player} a gagné")
                print("End of the game")
            else :
                if "*" not in self.board:
                    # game finished because all squares are filled
                    self.print_board()
                    print("il n'y a pas de gagant")
                    print("End of the game")
                else :
                    # no winning combination, so continue
                    self.change_player()
                    self.start_game()
        else :
            # there isn't enough square filled, so go on
            self.change_player()
            self.start_game()