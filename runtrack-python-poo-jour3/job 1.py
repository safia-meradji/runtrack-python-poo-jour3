class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def augmenter_population(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        # Ajouter la personne à la population de la ville
        self.__ville.augmenter_population()

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville


# Créer un objet Ville avec comme arguments “Paris” et 1000000
paris = Ville("Paris", 1000000)
# Afficher en console le nombre d’habitants de la ville de Paris
print(f"Population de la ville de Paris : {paris.get_nombre_habitants()}")

# Créer un autre objet Ville avec comme arguments “Marseille” et 861635
marseille = Ville("Marseille", 861635)
# Afficher en console le nombre d’habitants de la ville de Marseille
print(f"Population de la ville de Marseille : {marseille.get_nombre_habitants()}")

# Créer les objets suivants :
# - John, 45 ans, habitant à Paris
# - Myrtille, 4 ans, habitant à Paris
# - Chloé, 18 ans, habitant à Marseille
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes
print(f"Mise à jour de la population de la ville de Paris :  après l'arrivée de John et Myrtille: {paris.get_nombre_habitants()}")
print(f"Mise à jour de la population de la ville de Marseille : après l'arrivée de Chloé: {marseille.get_nombre_habitants()}")
