from enum import Enum
#Enum qui représente l'état d'une case du plateau ennemi

class Etat_Tir(Enum) :
    R = 0  # Rien en vue
    V = 1  # Bateau en vue
    T = 2  # Touché
    C = 3  # Coulé
