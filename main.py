import plateau

class Game:
    def __init__(self):
        self.gameInit()
        self.gameLoop()

    def gameInit(self):
        print("Entrez le nom du joueur A")
        joueurA = input()
        print("Entrez le nom du joueur B")
        joueurB = input()
    def gameLoop(self):
        pass
    def gameEnd(self):
        pass #TODO définir comment réinitialiser la game

if __name__=="__main__":
    game = Game()
