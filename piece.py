from enum import Enum
from etat_bateau import Etat_Bateau
from sens import Sens

class TypeOfPiece(Enum):
    Bateau1 = 0
    Bateau2 = 1
    Bateau3 = 2


class Piece:

    def __init__(self,joueur,sens,taille, x, y, z):
        self.headCoord = (x,y,z)
        self.caseList = list()
        self.joueur = joueur
        self.sens = sens
        self.taille = taille
        self.pieceInit()

    def pieceCases(self):
        return self.caseList

    def modifierEtat(self,x,y,z, etat_bateau):
        pass

    def pieceInit(self):
        self.caseList.append({'x':self.headCoord[0],'y':self.headCoord[1],'z':self.headCoord[2],'etat':Etat_Bateau.EN_VIE})
        if self.taille != 1 :
            for i in range(self.taille-1):
                if self.sens == Sens.DROITE:
                    self.caseList.append({'x':self.headCoord[0]+i+1,'y':self.headCoord[1],
                                          'z':self.headCoord[2],'etat':Etat_Bateau.EN_VIE})
                elif self.sens == Sens.GAUCHE:
                    self.caseList.append(
                        {'x': self.headCoord[0] - i - 1, 'y': self.headCoord[1],
                         'z': self.headCoord[2],'etat': Etat_Bateau.EN_VIE})
                elif self.sens == Sens.HAUT:
                    self.caseList.append(
                        {'x': self.headCoord[0], 'y': self.headCoord[1] + i + 1,
                         'z': self.headCoord[2],'etat': Etat_Bateau.EN_VIE})
                elif self.sens == Sens.BAS:
                    self.caseList.append(
                        {'x': self.headCoord[0], 'y': self.headCoord[1] - i - 1,
                         'z': self.headCoord[2],'etat': Etat_Bateau.EN_VIE})

