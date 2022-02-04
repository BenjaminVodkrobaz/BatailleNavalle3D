from plateau import Plateau
from etat_tir import Etat_Tir

class Game:

    def __init__(self):
        print("def plateau A-----------")
        plateauA = Plateau(mock=True)
        print("def plateau B-----------")
        plateauB = Plateau(mock=True)

        self.joueurs = dict()

        self.joueurs["joueurA"] = plateauA
        self.joueurs["joueurB"] = plateauB

        self.joueEnPremier()
        

    def joueEnPremier(self):
        input_joueur = 0
        while(input_joueur != 1 and input_joueur != 2) :
            print("QUI JOUE EN PREMIER ? \n\t joueurA -> 1 \n\t joueurB -> 2 :")
            input_joueur = int(input())
            if (input_joueur == 1) : 
                self.joueur_actuel = self.joueurs["joueurA"]
                self.joueur_actuel_code = 'A'
                self.prochain_joueur = self.joueurs["joueurB"]
            elif (input_joueur == 2) :
                self.joueur_actuel = self.joueurs["joueurB"]
                self.joueur_actuel_code = 'B'
                self.prochain_joueur = self.joueurs["joueurA"]

    def gameloop(self):
        flag_bateau = True # flag qui determine si il reste des bateaux
        while(flag_bateau):
            print(f'plateau du joueur {self.joueur_actuel_code}')
            self.joueur_actuel.print_grid()
            self.joueur_actuel.print_prim_grid()

            print(f'tir du joueur {self.joueur_actuel_code}')
            self.game_tir()

            print(f'plateau du joueur {self.joueur_actuel_code}')
            self.joueur_actuel.print_grid()
            self.joueur_actuel.print_prim_grid()
            if not self.prochain_joueur.check_all_bateaux_vivants() :
                flag_bateau = False
            else : 
                self.changement_joueur()

        print(f"ET LE GAGNANT EST LE JOUEUR {self.joueur_actuel_code} ! BIEN JOUE JOUEUR {self.joueur_actuel_code}, TU AS ETE LE PLUS FORT !! \n\n\n\n\n ENCORE B-R-A-V-O, JOUEUR {self.joueur_actuel_code}.")

        
    
    def game_tir(self):
        print("WAZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        coord_tir = dict()
        coord_tir["x"] = -1
        coord_tir["y"] = -1
        coord_tir["z"] = -1

        print("ENTREZ LES COORDONNEES DU TIR X,Y,Z")
        
        string_input = str(input())
        coord_tir["x"] = int(string_input.split(',')[0])
        coord_tir["y"] = int(string_input.split(',')[1])
        coord_tir["z"] = int(string_input.split(',')[2])

        while(coord_tir["x"] < 0
            or coord_tir["x"] >= 10
            or coord_tir["y"] < 0 
            or coord_tir["y"] >= 5 
            or coord_tir["z"] < 0
            or coord_tir["z"] >= 3
            or self.tir(coord_tir) == False) : #PROBLEME AQUI
            print("ENTREZ LES COORDONNEES DU TIR X,Y,Z")
        
            string_input = str(input())
            coord_tir["x"] = int(string_input.split(',')[0])
            coord_tir["y"] = int(string_input.split(',')[1])
            coord_tir["z"] = int(string_input.split(',')[2])

            
    def changement_joueur(self):
        temp = self.joueur_actuel
        self.joueur_actuel = self.prochain_joueur
        if self.joueur_actuel_code == 'A' :
            self.joueur_actuel_code = 'B'
        elif self.joueur_actuel_code == 'B' :
            self.joueur_actuel_code = 'A'

        self.prochain_joueur = temp
        print(f"JOUEUR ACTUEL : {self.joueur_actuel_code}\nPROCHAIN JOUEUR : {self.prochain_joueur}")

    def tir(self,coord_tir) :
        value = self.prochain_joueur.player_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]]

        if value == None :
            self.update_plateau_prime(coord_tir, Etat_Tir.R)
            return True
        elif not self.joueur_actuel.check_bateau_vivant(coord_tir["x"],coord_tir["y"],coord_tir["z"]) :
            return False
        else :
            self.prochain_joueur.update_plateau(coord_tir)
            self.update_plateau_prime(coord_tir, Etat_Tir.T)
            return True
        

    def update_plateau_prime(self,coord_tir, etat_tir):
        flag_vu = False
        if etat_tir == Etat_Tir.R :
            try :
                if self.prochain_joueur.player_grid[coord_tir["z"]+1][coord_tir["y"]][coord_tir["x"]] != None \
                    and flag_vu == False:
                        flag_vu = True
            except IndexError :
                pass

            try :
                if self.prochain_joueur.player_grid[coord_tir["z"]][coord_tir["y"]+1][coord_tir["x"]] != None \
                    and flag_vu == False:
                        flag_vu = True
            except IndexError :
                pass
            try :                
                if self.prochain_joueur.player_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]+1] != None \
                    and flag_vu == False:
                        flag_vu = True
            except IndexError :
                pass
            try :             
                if self.prochain_joueur.player_grid[coord_tir["z"]-1][coord_tir["y"]][coord_tir["x"]] != None \
                    and flag_vu == False \
                    and coord_tir["z"]-1 >= 0:
                        flag_vu = True
            except IndexError :
                pass
            try :             
                if self.prochain_joueur.player_grid[coord_tir["z"]][coord_tir["y"]-1][coord_tir["x"]] != None \
                    and flag_vu == False \
                    and coord_tir["y"]-1 >= 0:
                        flag_vu = True
            except IndexError :
                pass
            try :
                if self.prochain_joueur.player_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]-1] != None \
                    and flag_vu == False \
                    and coord_tir["x"]-1 >= 0:
                        flag_vu = True
            except IndexError :
                pass
            try :
                if self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]] == None \
                        or self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]] == Etat_Tir.R:
                    self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]] = Etat_Tir.R
            except IndexError :
                pass
                
                if flag_vu :
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]+1][coord_tir["y"]][coord_tir["x"]] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]+1][coord_tir["y"]][coord_tir["x"]] == Etat_Tir.R:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]+1][coord_tir["y"]][coord_tir["x"]] == Etat_Tir.V
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]+1][coord_tir["x"]] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]+1][coord_tir["x"]] == Etat_Tir.R:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]+1][coord_tir["x"]] == Etat_Tir.V
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]+1] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]+1] == Etat_Tir.R:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]+1] == Etat_Tir.V
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]-1][coord_tir["y"]][coord_tir["x"]] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]-1][coord_tir["y"]][coord_tir["x"]] == Etat_Tir.R \
                                and coord_tir["z"]-1 >= 0:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]-1][coord_tir["y"]][coord_tir["x"]] == Etat_Tir.V
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]-1][coord_tir["x"]] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]-1][coord_tir["x"]] == Etat_Tir.R \
                                and coord_tir["y"]-1 >= 0:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]-1][coord_tir["x"]] == Etat_Tir.V
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]-1] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]-1] == Etat_Tir.R \
                                and coord_tir["x"]-1 >= 0:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]-1] == Etat_Tir.V
                    except IndexError :
                        pass
                else :
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]+1][coord_tir["y"]][coord_tir["x"]] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]+1][coord_tir["y"]][coord_tir["x"]] == Etat_Tir.R:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]+1][coord_tir["y"]][coord_tir["x"]] == Etat_Tir.R
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]+1][coord_tir["x"]] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]+1][coord_tir["x"]] == Etat_Tir.R:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]+1][coord_tir["x"]] == Etat_Tir.R
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]+1] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]+1] == Etat_Tir.R:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]+1] == Etat_Tir.R
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]-1][coord_tir["y"]][coord_tir["x"]] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]-1][coord_tir["y"]][coord_tir["x"]] == Etat_Tir.R \
                                and coord_tir["z"]-1 >= 0:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]-1][coord_tir["y"]][coord_tir["x"]] == Etat_Tir.R
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]-1][coord_tir["x"]] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]-1][coord_tir["x"]] == Etat_Tir.R \
                                and coord_tir["y"]-1 >= 0:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]-1][coord_tir["x"]] == Etat_Tir.R
                    except IndexError :
                        pass
                    try :
                        if self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]-1] == None \
                                or self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]-1] == Etat_Tir.R \
                                and coord_tir["x"]-1 >= 0:
                            self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]-1] == Etat_Tir.R
                    except IndexError :
                        pass



        if etat_tir == Etat_Tir.T :
            self.joueur_actuel.player_prim_grid[coord_tir["z"]][coord_tir["y"]][coord_tir["x"]] = Etat_Tir.T


            