import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))

    def lancerJeu(self):
        joueur = Personnage("Joueur", self.niveau * 20)
        ennemi = Personnage("Ennemi", self.niveau * 15)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu !")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu !")
                break

        self.verifierGagnant(joueur, ennemi)

    def verifierGagnant(self, joueur, ennemi):
        if joueur.vie > 0:
            print(f"{joueur.nom} a gagné !")
        else:
            print(f"{ennemi.nom} a gagné !")


# Tester le jeu
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
