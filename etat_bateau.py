from enum import Enum
#Enum qui représente l'état d'un bateau dans le plateau joueur

class Etat_Bateau(Enum) :
    V = 0 # Bateau en vie
    T = 1 # Bateau touché
    C = 2 # BBateau coulé
    EN_VIE = 0  # Bateau en vie
    TOUCHE = 1  # Bateau touché
    COULE = 2   # Bateau coulé