class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - Statut : {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche ajoutée : {tache}")

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche supprimée : {tache}")
                return
        print(f"Tâche non trouvée : {titre}")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                print(f"Tâche marquée comme terminée : {tache}")
                return
        print(f"Tâche non trouvée : {titre}")

    def afficherListe(self):
        if not self.taches:
            print("Aucune tâche dans la liste.")
        else:
            for tache in self.taches:
                print(tache)

    def filterListe(self, statut):
        resultats = [tache for tache in self.taches if tache.statut == statut]
        return resultats


# Tester le code
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Relire les notes du cours")
tache3 = Tache("Faire du sport", "Aller à la salle de sport")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

liste_taches.afficherListe()

liste_taches.marquerCommeFinie("Faire les courses")

liste_taches.supprimerTache("Réviser pour l'examen")

liste_taches.afficherListe()

taches_a_faire = liste_taches.filterListe("à faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(tache)
