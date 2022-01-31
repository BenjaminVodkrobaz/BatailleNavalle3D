from enum import Enum
from etat_bateau import Etat_Bateau
from sens import Sens


class TypeOfPiece(Enum):
    Bateau1 = 0
    Bateau2 = 1
    Bateau3 = 2


class Piece:

    def __init__(self, plateau,
                 sens: Sens,
                 taille: int,
                 x: int,
                 y: int,
                 z: int):
        """instance de plateau, sens, taille, x, y, z"""
        self.plateau = plateau
        self.headCoord = (x, y, z)
        self.caseList = list()
        self.sens = sens
        self.taille = taille
        self.piece_init()

    def piece_squares(self):
        positions = []
        for i in range(self.taille):
            positions.append((self.caseList[i]["x"], self.caseList[i]["y"], self.caseList[i]["z"]))
        return positions

    def piece_init(self) -> bool:
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
                        {'x': self.headCoord[0], 'y': self.headCoord[1] -i -1,
                         'z': self.headCoord[2], 'state': Etat_Bateau.EN_VIE})

                elif self.sens == Sens.BAS:
                    self.caseList.append(
                        {'x': self.headCoord[0], 'y': self.headCoord[1] + i + 1,
                         'z': self.headCoord[2], 'state': Etat_Bateau.EN_VIE})
            return True
        else:
            return False
