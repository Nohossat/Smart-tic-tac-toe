from player import Player
import random
from exceptions import MissingArgument

class Computer(Player):

    def __init__(self, token):
        super().__init__(token)

        self.combinations = [
            [0, 1, 2],
            [0, 4, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [2, 4, 6],
            [3, 4, 5],
            [6, 7, 8]
        ] # needed to keep track if the opponent is winning

        self.possible_winning_combinations = [
            [0, 1, 2],
            [0, 4, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [2, 4, 6],
            [3, 4, 5],
            [6, 7, 8]
        ]


    def choose_best_square(self, board, opponent_token):
        square_played_by_opponent = [i for i in range(0, 9) if board[i] == opponent_token]
        updated_possible_combinations = []
        choice = None

        # we get the remaining winning combinations
        for combi in self.possible_winning_combinations:
            if not (set(combi) & set(square_played_by_opponent)):
                updated_possible_combinations.append(combi)

        self.possible_winning_combinations = updated_possible_combinations

        # decide if I have to block the opponent
        for combi in self.combinations:
            remaining_squares = [i for i in combi if isinstance(board[i], int)]
            opponent_is_winning = [i for i in combi if board[i] == opponent_token]

            if len(opponent_is_winning) == 2 and len(remaining_squares) == 1: # the opponent is winning but I still can block him
                choice = remaining_squares[0] + 1 # convert to correct indexing
                break
        
        # improvement, if the machine sees she is about to win, no need to block the human

        # decides it is better to try a winning strategy
        if choice is None:
            for i in self.possible_winning_combinations[0]:
                if isinstance(board[i], int):
                    choice = i + 1 # convert to correct indexing
                    break

        return choice

    def choose_square(self, kwargs):
        """
        random choice among available squares by computer
        """
        print(f"Joueur {self.token} (Computer)")

        try :
            if kwargs["board"] is None or kwargs["opponent_token"] is None:
                raise MissingArgument

            choice = self.choose_best_square(**kwargs)
            return choice
        except MissingArgument as e:
            print("there is an arg missing in the function call")


if __name__=='__main__':
    computer = Computer("X")
    computer.choose_best_square(["O", "X", 3, 
                              4, "O", "X", 
                              "O", "X", 9], "X")

    