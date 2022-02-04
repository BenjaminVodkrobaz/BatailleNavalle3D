from piece import Piece
from sens import Sens
from etat_tir import Etat_Tir
from etat_bateau import Etat_Bateau
import pathlib

NOMBRE_DE_BATEAUX = 3
p = pathlib.Path().resolve() / "last_game.txt"



class Plateau:
    def __init__(self):
        self.new_game = True
        self.file_content = []
        self.player_grid = [[[None for _ in range(10)] for _ in range(5)] for _ in range(3)]
        self.player_prim_grid = [[[None for _ in range(10)] for _ in range(5)] for _ in range(3)]
        self.player_pieces = []
        self.__ask_for_new_game__()  # demande si les joueurs souhaitent reprendre la partie précédente
        print("placement des pièces du joueur :")
        self.__placementPieces__()  # Placement des pièces du joueur

        self.update_file([str(x.headCoord) + "\n" + str(x.sens) for x in self.player_pieces])

        tmpdict1 = {'x': 2, 'y': 2, 'z': 2}
        tmpdict2 = {'x': 2, 'y': 3, 'z': 2}
        tmpdict3 = {'x': 1, 'y': 2, 'z': 2}
        tmpdict4 = {'x': 3, 'y': 2, 'z': 2}
        tmpdict5 = {'x': 3, 'y': 3, 'z': 2}
        tmpdict6 = {'x': 3, 'y': 4, 'z': 2}
        self.update_plateau(tmpdict1)
        self.update_plateau(tmpdict2)
        self.update_plateau(tmpdict3)
        self.update_plateau(tmpdict4)
        self.update_plateau(tmpdict5)
        self.update_plateau(tmpdict6)
        self.print_prim_grid()

    def __ask_for_new_game__(self):
        if p.is_file():
            print("Il existe une ancienne partie enregistrée souhaitez-vous la continuer ? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    self.new_game = False
                    with p.open() as f:
                        self.file_content = f.readlines()
                    p.unlink()
                    break
                elif answer == "n":
                    self.new_game = True
                    p.unlink()
                    break
                else:
                    print("réponse invalide, rééssayez.")

    def __placementPieces__(self):
        for i in range(NOMBRE_DE_BATEAUX):
            if not self.new_game:
                pos = eval(self.file_content[i * 2].replace("(", "").replace(")", "").replace("\n", "") \
                           .replace(" ", ""))
                sens = Sens.from_str(self.file_content[i * 2 + 1].strip('\n'))
                self.player_pieces.append(self.__placement_bateau__(i + 1, True, pos, sens))
            else:
                self.player_pieces.append(self.__placement_bateau__(i + 1))
            self.update_main_grid(self.player_pieces[i])

    def __placement_bateau__(self, taille, replay=False, coords=(0, 0, 0), senspiece=Sens.BAS) -> Piece:
        print(f"placement du bateau de taille {taille}")
        while True:
            if not replay:
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
                    print("la valeur x,y,z entrée n'est pas valide veuillez rééssayer.")
                    continue
                x = int(pos[0])
                y = int(pos[1])
                z = int(pos[2])

                print("Veuillez indiquer le sens pour votre bateau : gauche/droite/haut/bas")
                sens = str(input()).lower()
                if sens != "gauche" and sens != "droite" and sens != "haut" and sens != "bas":
                    print("la valeur du sens n'est pas correcte veuillez réessayer.")
                    continue
                if sens == "gauche":
                    sens = Sens.GAUCHE
                if sens == "droite":
                    sens = Sens.DROITE
                if sens == "haut":
                    sens = Sens.HAUT
                if sens == "bas":
                    sens = Sens.BAS
                if not self.check_valid_placement(taille, sens, x, y, z):
                    print("Le placement n'est pas correct, veuillez replacer correctement le bateau.")
                    continue
                return Piece(self, sens, taille, x, y, z)
            else:
                return Piece(self, senspiece, taille, coords[0], coords[1], coords[2])

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
                    elif self.player_prim_grid[z][y][x] == Etat_Bateau.EN_VIE:
                        tmpstr = tmpstr + " B "
                    elif self.player_prim_grid[z][y][x] == Etat_Tir:
                        tmpstr = tmpstr + " B "
                    elif self.player_prim_grid[z][y][x] == Etat_Bateau.TOUCHE:
                        tmpstr = tmpstr + " T "
                    elif self.player_prim_grid[z][y][x] == Etat_Bateau.COULE:
                        backgroundColor = 41
                        textBeginning = f"\033[1;30;{backgroundColor}m"
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
                    self.check_bateau_coule(actualPiece)
                    self.update_main_grid(actualPiece)

    def check_bateau_coule(self, piece: Piece):
        for i in range(piece.taille):
            if piece.caseList[i]['state'] != Etat_Bateau.TOUCHE:
                return False
        for i in range(piece.taille):
            piece.caseList[i]['state'] = Etat_Bateau.COULE
            self.player_prim_grid[piece.caseList[i]["z"]][piece.caseList[i]["y"]][piece.caseList[i]["x"]] = Etat_Bateau.COULE  # on coule le bateau associé au plateau prime aussi
        print("Le bateau a été coulé !")
        self.check_all_bateaux_vivants()
        return True

    def update_file(self, strings_to_add: list[str]):
        lines = ""
        if p.is_file():
            lines = p.read_text()
        else:
            p.touch()
        for i in range(len(strings_to_add)):
            lines = lines + strings_to_add[i] + "\n"
        with p.open("w") as f:
            f.write(lines)


if __name__ == "__main__":
    a = Plateau()
