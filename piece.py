from enum import Enum

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


    def pieceInit(self):
        self.caseList.append({'x':self.headCoord[0],'y':self.headCoord[1],'z':self.headCoord[2],'etat':Etat_Bateau.EN_VIE})
        if self.taille != 1 :
            for i in range(self.taille-1):
