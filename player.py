import random
from exceptions import ValueTooSmallError, ValueTooBigError, ValueNotAvailable

class Player:
    def __init__(self, token):
        self.token = token

    def choose_square(self, available_squares):
        """
        allow human being to fill a square, input validation also included
        """
        print(f"Joueur {self.token}, à toi de jouer : ")

        while True:
            try:
                choice = int(input("Dans quelle case, veux-tu placer ton pion (entre 1 et 9): "))

                if choice > 9 :
                    raise ValueTooBigError
                elif choice < 0:
                    raise ValueTooSmallError
                elif choice not in available_squares: 
                    raise ValueNotAvailable
                else :
                    break

            except ValueError as e:
                print("Votre choix doit être une valeur numérique, comprise entre 1 et 9")
            except ValueTooSmallError as e:
                print("Votre choix doit être un chiffre supérieur à 0")
            except ValueTooBigError as e:
                print("Votre choix doit être un chiffre inférieur à 9")
            except ValueNotAvailable as e:
                print("Case non disponible : il faut en choisir une autre")
        
        return choice