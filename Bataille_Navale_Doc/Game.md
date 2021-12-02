CONTROLLEUR :

Class : Game

Attr :
-	joueur1 : [[Joueur]]
-	joueur2 : [[Joueur]]

Méthode :
-	init()
	-	Demander qui est joueur A
	-	Init plateau (joueur et ennemi) pour chaque joueur -> vide

- gameLoop()
	- Tant que tout les joueurs ont des bateaux :
		- On affiche les plateaux (joueur et ennemi) du joueur 1 
		- On demande les coordonnées du tir au joueur 1 
			- Verification des coordonnées, si coordonnées -> bateau coulé | hors du plateau => on redemande une nouvelle coordonnée de tir

		- On tire sur le plateau joueur du joueur 2 ( on accède aux coordonnées (X,Y,Z))
		- Selon la valeur de retour :
			- R -> on vérifie (si dans le plateau)
				- (X+1,Y,Z)
				- (X-1,Y,Z)
				- (X,Y+1,Z)
				- (X,Y-1,Z)
				- (X,Y-1,Z+1)
				- (X,Y-1,Z-1)
				
				=> Si il y a rien : on ajoute  sur le plateau ennemi du joueur 1 à toute ces coordonnées. Sinon, il y a un bateau et donc on affiche 