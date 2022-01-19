from piece import Piece
from num_joueur import Num_Joueur
from sens import Sens


class Plateau:
    def __init__(self):
        self.current_player = Num_Joueur.JOUEUR_A
        self.player_A_grid = [[[None] * 10] * 5] * 3
        self.player_B_grid = [[[None] * 10] * 5] * 3
        self.player_A_piece1 = None
        self.player_A_piece2 = None
        self.player_A_piece3 = None
        self.player_B_piece1 = None
        self.player_B_piece2 = None
        self.player_B_piece3 = None
        print("placement des pièces du joueur A :")
        self.__placementPieces__(Num_Joueur.JOUEUR_A)  # Placement des pièces des 2 joueurs.
        print("placement des pièces du joueur B :")
        #self.__placementPieces__(Num_Joueur.JOUEUR_B)

    def __placementPieces__(self, player: Num_Joueur):
        # TODO implement for both players
        self.player_A_piece1 = self.__placement_bateau__(1)
        self.player_A_piece2 = self.__placement_bateau__(2)
        self.player_A_piece3 = self.__placement_bateau__(3)

    def __placement_bateau__(self, taille) -> Piece:
        print(f"placement du bateau de taille {taille}")
        while True:
            try:
                print("veuillez indiquer la position à laquelle vous souhaitez placer le bateau sous le format x,"
                      "y,z :")
                pos = input()
                pos = pos.split(',', 3)
                if len(pos) != 3 \
                        or int(pos[0]) > 9 \
                        or int(pos[1]) > 4 \
                        or int(pos[2]) > 2 \
                        or int(pos[0]) < 0 \
                        or int(pos[1]) < 0 \
                        or int(pos[2]) < 0:
                    x = int(pos[0])
                    y = int(pos[1])
                    z = int(pos[2])
                    print("la valeur x,y,z entrée n'est pas valide veuillez rééssayer.")
                    continue
                x = int(pos[0])
                y = int(pos[1])
                z = int(pos[2])
                return Piece(self, self.current_player, Sens.DROITE, taille, x, y, z)
            except Exception as e:
                print("Veuillez fournir des données valides")
                pass

    def turn_manager(self):
        self.print_player_turn()
        self.print_self_grid(self.current_player)  # devrait montrer le plateau de l'autre joueur
        # par les inputs utilisateur
        #  TODO montrer le plateau connu de l'autre joueur
        #  TODO demander ou tirer
        #  TODO afficher le résultat du tir

        print(self.player_A_piece1.piece_squares())

        # TODO créer la fonction qui modifie le plateau suivant les pièces présentes.

        self.change_player_turn()

    def print_self_grid(self, joueur: Num_Joueur):
        if joueur == Num_Joueur.JOUEUR_A:
            self.print_A_grid()
        else:
            self.print_B_grid()

    def get_player_turn(self):
        return self.current_player

    def change_player_turn(self):
        self.current_player = Num_Joueur((self.current_player.value + 1) % 2)

    def print_player_turn(self):
        print(f"c'est au tour de {self.current_player.name}")

    def print_A_grid(self):
        for j in range(3):
            print("                    Profondeur : ", 100 * j, "\n")
            for i in range(5):
                print(self.player_A_grid[j][i][0:])
            print("")

    def print_B_grid(self):
        for j in range(3):
            print("                    Profondeur : ", 100 * j, "\n")
            for i in range(5):
                print(self.player_B_grid[j][i][0:])
            print("")

    def get_square_content(self, x, y, z):
        if self.current_player == Num_Joueur.JOUEUR_A:
            print("player A grid at asked position", self.player_A_grid[z][y][x]) # TODO delete the string as used for information purposes
        else:
            print("player B grid at asked position", self.player_B_grid[z][y][x]) # TODO delete the string as used for information purposes
        return


if __name__ == "__main__":
    a = Plateau()
