class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde}")
        print(f"Autorisation de découvert : {self.__decouvert}")
        print()

    def afficherSolde(self):
        print(f"Solde du compte : {self.__solde}")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} effectué. Nouveau solde : {self.__solde}")

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde : {self.__solde}")
        else:
            print("Opération impossible : solde insuffisant et pas de découvert autorisé.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Agios appliqués. Nouveau solde : {self.__solde}")

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès.")
        else:
            print("Opération impossible : solde insuffisant et pas de découvert autorisé.")


# Créer une première instance de la classe CompteBancaire
compte1 = CompteBancaire("123456", "Doe", "John", 5000)

# Appeler les différentes méthodes pour vérifier leur fonctionnement
compte1.afficher()
compte1.versement(2000)
compte1.retrait(1000)
compte1.afficherSolde()

# Ajouter l'attribut découvert à la classe CompteBancaire
# Créer une deuxième instance de la classe CompteBancaire avec découvert autorisé
compte2 = CompteBancaire("789012", "Smith", "Alice", -1000, decouvert=True)

# Faire un versement du compte1 vers compte2 pour remettre compte2 à zéro
compte1.virement(compte2, 1500)

# Afficher les comptes après l'opération
compte1.afficher()
compte2.afficher()
