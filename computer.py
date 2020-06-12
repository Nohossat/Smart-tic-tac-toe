from player import Player
import random

class Computer(Player):

    def __init__(self, token):
        super().__init__(token)

    def choose_square(self, available_squares):
        """
        random choice among available squares by computer
        """
        print(f"Joueur {self.token} (Computer)")
        choice = random.choice(available_squares)

        return choice

        # the computer already knows all the winning combinations
        # it will take the best decision according to the current state of the game

        # self.choose_best_square()

    def choose_best_square(self):
        pass

    