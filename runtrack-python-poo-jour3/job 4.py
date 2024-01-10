class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1
        print(f"{self.nom} a marqué un but!")

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a effectué une passe décisive!")

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune.")

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge.")

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (#{self.numero}), Position: {self.position}")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
        print(f"Joueur {joueur.nom} ajouté à l'équipe {self.nom}.")

    def afficherStatistiquesJoueurs(self):
        print(f"\nStatistiques des joueurs de l'équipe {self.nom} :")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                else:
                    print("Action non reconnue.")
                return
        print(f"Joueur {nom_joueur} non trouvé dans l'équipe {self.nom}.")


# Créer plusieurs joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Iniesta", 8, "Milieu")
joueur4 = Joueur("Piqué", 3, "Défenseur")

# Créer deux équipes
equipe1 = Equipe("Barcelona")
equipe2 = Equipe("Real Madrid")

# Ajouter les joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur4)

# Afficher les statistiques des joueurs avant le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simuler un match
equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Iniesta", "passe")
equipe2.mettreAJourStatistiquesJoueur("Ronaldo", "but")
equipe2.mettreAJourStatistiquesJoueur("Piqué", "rouge")

# Afficher les statistiques des joueurs après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
