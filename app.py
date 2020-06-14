from morpion import Morpion
import argparse


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Play Tic-Tac-Toe\n")
    parser.add_argument('-mode', '--mode', help='play against Human', default=False)
    args = parser.parse_args()
    mode = False

    if args.mode in ["h", "human", "humain", "manuel"]:
        mode = True

    morpion_game = Morpion(human=mode)
    morpion_game.start_game()