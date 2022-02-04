from piece import Piece
from sens import Sens
from etat_tir import Etat_Tir
from etat_bateau import Etat_Bateau


class Plateau:
    def __init__(self, mock):
        self.player_grid = [[[None for _ in range(10)] for _ in range(5)] for _ in range(3)]
        self.player_prim_grid = [[[None for _ in range(10)] for _ in range(5)] for _ in range(3)]
        self.player_pieces = []
        print("placement des pièces :")
        self.__placementPieces__(mock)  # Placement des pièces des 2 joueurs

    def __placementPieces__(self, mock = False):
        #  TODO modifier que les cases correctes
        for i in range(3):
            if mock :
                print(f"pièce {i}")
            self.player_pieces.append(self.__placement_bateau__(i + 1, mock))
            self.update_main_grid(self.player_pieces[i])

    def __placement_bateau__(self, taille, mock) -> Piece:
        print(f"placement du bateau de taille {taille}")
        while True:
            #try:
            if not mock :
                if True:
                    print("veuillez indiquer la position à laquelle vous souhaitez placer le bateau sous le format x,"
                            "y,z :")
                    pos = input()
                    pos = pos.split(',', 3)
                    print(pos)
                    if len(pos) != 3 \
                            or int(pos[0]) > 9 \
                            or int(pos[1]) > 4 \
                            or int(pos[2]) > 2 \
                            or int(pos[0]) < 0 \
                            or int(pos[1]) < 0 \
                            or int(pos[2]) < 0:
                        print("la valeur x,y,z entrée n'est pas valide veuillez rééssayer.")
                        continue
                    x = int(pos[0])
                    y = int(pos[1])
                    z = int(pos[2])

                    print("Veuillez indiquer le sens pour votre bateau : GAUCHE/DROITE/HAUT/BAS")
                    sens = str(input())
                    print(sens)
                    if sens != "GAUCHE" and sens != "DROITE" and sens != "HAUT" and sens != "BAS":
                        print("la valeur du sens n'est pas correcte veuillez réessayer.")
                        continue
                    if sens == "GAUCHE":
                        sens = Sens.GAUCHE
                    if sens == "DROITE":
                        sens = Sens.DROITE
                    if sens == "HAUT":
                        sens = Sens.HAUT
                    if sens == "BAS":
                        sens = Sens.BAS
                    if not self.check_valid_placement(taille, sens, x, y, z):
                        print("Le placement n'est pas correct, veuillez replacer correctement le bateau.")
                        continue
                    return Piece(self, sens, taille, x, y, z)
                # except Exception as e:
                #     print(f"{e}Veuillez fournir des données valides")
                #     pass
            else :
                return Piece(self, Sens.BAS, taille, 1, 1, taille-1)

    def check_valid_placement(self, taille: int, sens: Sens, x: int, y: int, z: int):
        headCoord = (x, y, z)
        if taille != 1:
            for i in range(taille):
                if sens == Sens.DROITE:
                    if headCoord[0] + i > 9:
                        print("Le placement est hors du plateau.")
                        return False
                    if self.get_square_content(headCoord[0] + i, headCoord[1], headCoord[2]) is not None:
                        print("Un bateau est déjà présent sur l'une des cases.")
                        return False
                elif sens == Sens.GAUCHE:
                    if headCoord[0] - i < 0:
                        print("Le placement est hors du plateau.")
                        return False
                    if self.get_square_content(headCoord[0] - i, headCoord[1], headCoord[2]) is not None:
                        print("Un bateau est déjà présent sur l'une des cases.")
                        return False
                elif sens == Sens.HAUT:
                    print("heardcoord-i", headCoord[1] - i)
                    if headCoord[1] - i < 0:
                        print("Le placement est hors du plateau.")
                        return False
                    if self.get_square_content(headCoord[0], headCoord[1] - i, headCoord[2]) is not None:
                        print("Un bateau est déjà présent sur l'une des cases.")
                        return False
                elif sens == Sens.BAS:
                    if headCoord[1] + i > 4:
                        print("Le placement est hors du plateau.")
                        return False
                    if self.get_square_content(headCoord[0], headCoord[1] + i, headCoord[2]) is not None:
                        print("Un bateau est déjà présent sur l'une des cases.")
                        return False
            return True
        else:
            if self.get_square_content(headCoord[0], headCoord[1], headCoord[2]) is not None:
                print("Un bateau est déjà présent sur l'une des cases.")
                return False
            return True

    #  permet d'update la main grid suivant la piece envoyée en paramètre
    def update_main_grid(self, piece: Piece):
        for i in range(piece.taille):
            self.player_grid[piece.caseList[i]["z"]][piece.caseList[i]["y"]][piece.caseList[i]["x"]] = \
                piece.caseList[i]["state"]
        self.print_grid()

    def print_grid(self):
        textEndLine = "\033[0;0m"
        for z in range(3):
            print("            Profondeur : ", 100 * z, "\n")
            print("     0  1  2  3  4  5  6  7  8  9")
            print("   -------------------------------- ")
            for y in range(5):
                tmpstr = ""
                for x in range(10):
                    if self.player_grid[z][y][x] is None:
                        tmpstr = tmpstr + "   "
                    elif self.player_grid[z][y][x] == Etat_Bateau.EN_VIE:
                        backgroundColor = 42 + self.numero_bateau(x, y, z)
                        textBeginning = f"\033[1;30;{backgroundColor}m"
                        tmpstr = tmpstr + f"{textBeginning} B {textEndLine}"
                    elif self.player_grid[z][y][x] == Etat_Bateau.TOUCHE:
                        backgroundColor = 42 + self.numero_bateau(x, y, z)
                        textBeginning = f"\033[1;30;{backgroundColor}m"
                        tmpstr = tmpstr + f"{textBeginning} T {textEndLine}"
                    elif self.player_grid[z][y][x] == Etat_Bateau.COULE:
                        backgroundColor = 41
                        textBeginning = f"\033[1;30;{backgroundColor}m"
                        tmpstr = tmpstr + f"{textBeginning} C {textEndLine}"
                    else:
                        print("Etat inconnu : ", self.player_grid[z][y][x])
                print(f"{y} | {tmpstr} |")
            print("   -------------------------------- ")

    def numero_bateau(self, x, y, z):
        for i in range(len(self.player_pieces)):
            for j in range(len(self.player_pieces[i].piece_squares())):
                if (x, y, z) == self.player_pieces[i].piece_squares()[j]:
                    return i
        return -1000

    def print_prim_grid(self):
        for z in range(3):
            print("            Profondeur : ", 100 * z, "\n")
            print("     0  1  2  3  4  5  6  7  8  9")
            print("   -------------------------------- ")
            for y in range(5):
                tmpstr = ""
                for x in range(10):
                    if self.player_prim_grid[z][y][x] is None:
                        tmpstr = tmpstr + "   "
                    elif self.player_prim_grid[z][y][x] == Etat_Tir.R:
                        tmpstr = tmpstr + " R "
                    elif self.player_prim_grid[z][y][x] == Etat_Bateau.TOUCHE:
                        tmpstr = tmpstr + " T "
                    elif self.player_prim_grid[z][y][x] == Etat_Bateau.T or self.player_prim_grid[z][y][x] == Etat_Tir.T:
                        tmpstr = tmpstr + " T "
                    elif self.player_prim_grid[z][y][x] == Etat_Bateau.COULE:
                        backgroundColor = 42 + self.numero_bateau(x, y, z)
                        textBeginning = f"\033[1;31;{backgroundColor}m"
                        tmpstr = tmpstr + f"{textBeginning} C \033[0;0m"
                    else:
                        print("Etat inconnu")
                print(f"{y} | {tmpstr} |")
            print("   -------------------------------- ")

    def get_square_content(self, x, y, z):
        return self.player_grid[z][y][x]

    def check_all_bateaux_vivants(self):
        for i in range(len(self.player_pieces)):
            if self.player_pieces[i].caseList[0]['state'] != Etat_Bateau.COULE:
                print('WAZAAAAAAAAAAAAAAAAAAAAAAAAAAA 2 LE RETOUR')
                return True
        print("tous les bateaux sont coulés, fin de la partie.")
        return False

    def check_bateau_vivant(self, x, y, z):
        for i in range(len(self.player_pieces)):
            actualPiece = self.player_pieces[i]
            squares = actualPiece.piece_squares()
            for j in range(len(squares)):
                if squares[j] == (x, y, z):
                    if actualPiece.caseList[j]["state"] == Etat_Bateau.EN_VIE:
                        return True
        return False

    #  changer l'état du bateau à la coord donnée, passage en_vie à touché et potentiellement de touché à coulé
    def update_plateau(self, coord_tir: dict):
        for i in range(len(self.player_pieces)):
            actualPiece = self.player_pieces[i]
            squares = actualPiece.piece_squares()
            for j in range(len(squares)):
                if squares[j] == (coord_tir['x'], coord_tir['y'], coord_tir['z']):
                    actualPiece.caseList[j]['state'] = Etat_Bateau.TOUCHE
                    self.update_main_grid(actualPiece)
                    self.check_bateau_coule(actualPiece)

    def check_bateau_coule(self, piece: Piece):
        for i in range(piece.taille):
            if piece.caseList[i]['state'] != Etat_Bateau.TOUCHE:
                return False
        for i in range(piece.taille):
            piece.caseList[i]['state'] = Etat_Bateau.COULE
        self.update_main_grid(piece)
        print("Le bateau a été coulé !")
        self.check_all_bateaux_vivants()
        return True


if __name__ == "__main__":
    a = Plateau()