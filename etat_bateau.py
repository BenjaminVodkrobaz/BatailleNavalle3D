from enum import Enum
#Enum qui représente l'état d'un bateau dans le plateau joueur

class Etat_Bateau(Enum) :
    EN_VIE = 0 # Bateau en vie
    TOUCHE = 1 # Bateau touché
    COULE = 2 # BBateau coulé