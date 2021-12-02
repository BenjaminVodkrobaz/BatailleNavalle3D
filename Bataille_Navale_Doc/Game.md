CONTROLLEUR :

Class : Game

Attr :
-	joueur1 : [[Joueur]]
-	joueur2 : [[Joueur]]

Méthode :
-	init()
	-	Demander qui est joueur A et son doux nom
	-	Init plateau (joueur et ennemi) pour chaque joueur -> vide

- gameLoop()
	- Tant que tout les joueurs ont des bateaux :
		- On affiche les plateaux (joueur et ennemi) du joueur 1 
		- On demande les coordonnées du tir au joueur 1 
			- Verification des coordonnées, si coordonnées -> bateau coulé | hors du plateau => on redemande une nouvelle coordonnée de tir

		- On tire sur le plateau joueur du joueur 2 ( on accède aux coordonnées (X,Y,Z))
		- Selon la valeur de retour :
			- si il y a rien -> on vérifie (si dans le plateau)
				- (X+1,Y,Z)
				- (X-1,Y,Z)
				- (X,Y+1,Z)
				- (X,Y-1,Z)
				- (X,Y1,Z+1)
				- (X,Y1,Z-1)
				
				=> Si il y a rien : on ajoute [[Resultat_Tir]].R sur le plateau ennemi du joueur 1 à toutes ces coordonnées. Sinon, il y a un bateau et donc on ajoute [[Resultat_Tir]].V à toutes ces coordonnées.
			- si il y a un bateau -> on vérifie que toute les cases du bateaux sont touchées 
				- Si oui : le bateau passe à l'état coulé et ne peux plus être visé et le joueur 2 perd son bateau
				- Si non : le bateau ne coule pas

		- On affiche les plateaux (joueur et ennemi) du joueur 1
		- On vérifie si le joueur 2 a tout ses bateaux de vivant
			- Si oui : on continue le jeu
			- Si non : le joueur 1 a gagné

		- On fait pareil avec le joueur 2
		
	