from enum import Enum
from etat_bateau import Etat_Bateau
from sens import Sens
from num_joueur import Num_Joueur
from plateau import Plateau

class TypeOfPiece(Enum):
    Bateau1 = 0
    Bateau2 = 1
    Bateau3 = 2


class Piece:

    def __init__(self, plateau: Plateau,
                 joueur: Num_Joueur,
                 sens: Sens,
                 taille: int,
                 x: int,
                 y: int,
                 z: int):
        """intance de plateau, player (JOUEUR_A || JOUEUR_B), sens, taille, x, y, z"""
        self.plateau = plateau
        self.headCoord = (x, y, z)
        self.caseList = list()
        self.joueur = joueur
        self.sens = sens
        self.taille = taille
        self.piece_init()

    def piece_squares(self):
        positions = [int]
        for i in range(self.taille):
            positions.append(self.caseList[i])
        return positions

    def modify_state(self, x, y, z, etat_bateau):
        pass

    def piece_init(self) -> bool:
        if self.check_no_boat():
            self.caseList.append({'x': self.headCoord[0], 'y': self.headCoord[1],
                                  'z': self.headCoord[2], 'state': Etat_Bateau.EN_VIE})
            if self.taille != 1:
                for i in range(self.taille - 1):
                    if self.sens == Sens.DROITE:
                        self.caseList.append({'x': self.headCoord[0] + i + 1, 'y': self.headCoord[1],
                                              'z': self.headCoord[2], 'state': Etat_Bateau.EN_VIE})

                    elif self.sens == Sens.GAUCHE:
                        self.caseList.append(
                            {'x': self.headCoord[0] - i - 1, 'y': self.headCoord[1],
                             'z': self.headCoord[2], 'state': Etat_Bateau.EN_VIE})

                    elif self.sens == Sens.HAUT:
                        self.caseList.append(
                            {'x': self.headCoord[0], 'y': self.headCoord[1] + i + 1,
                             'z': self.headCoord[2], 'state': Etat_Bateau.EN_VIE})

                    elif self.sens == Sens.BAS:
                        self.caseList.append(
                            {'x': self.headCoord[0], 'y': self.headCoord[1] - i - 1,
                             'z': self.headCoord[2], 'state': Etat_Bateau.EN_VIE})
            return True
        else:
            return False

    def check_no_boat(self) -> bool:
        # TODO Finish implementation for all squares and not only one.
        for i in range(self.taille):
            if self.plateau.get_square_content(self.headCoord[0], self.headCoord[1], self.headCoord[2]) is not None:
                pass
            else:
                return False
        return True


        pass

    def update_plateau(self):
        pass
        # TODO implement that
