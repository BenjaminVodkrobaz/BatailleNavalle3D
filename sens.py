from enum import Enum
# Enum qui représente le sens du bateau posé


class Sens(Enum):
    HAUT = 0
    BAS = 1 
    GAUCHE = 2 
    DROITE = 3

    @staticmethod
    def from_str(label):
        if label.lower() in ('sens.bas', 'bas'):
            return Sens.BAS
        if label.lower() in ('sens.droite', 'droite'):
            return Sens.DROITE
        if label.lower() in ('sens.haut', 'haut'):
            return Sens.HAUT
        if label.lower() in ('sens.gauche', 'gauche'):
            return Sens.GAUCHE
