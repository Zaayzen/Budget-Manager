import csv

class BudgetManager:
    def __init__(self, fichier_donnees="depenses.csv"):
        self.depenses = []
        self.fichier_donnees = fichier_donnees
        self.categorie = ["Transport", "Alimentation", "Loisirs", "Autre"]
        self.next_id = 1

    def add_depense(self, depense):
        if depense.montant < 0:
            print ("Erreur le montant de peut pas être négatif")
        elif depense.nom.strip() == "" :
            print("Erreur la depense n'a pas de nom")
        elif depense.categorie not in self.categorie:
            print("Erreur catégorie non valide")
        else:
            self.depenses.append(depense)
            depense.id = self.next_id
            self.next_id += 1
            with open(self.fichier_donnees, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([depense.id, depense.nom, depense.montant, depense.categorie, depense.date])
            print(f"Dépense' {depense.nom}' de {depense.montant}€ ajoutée avec l'ID {depense.id}")
    

    def delete_depense(self, id):
        for dep in self.depenses :
            if dep.id == id:
                self.depenses.remove(dep)
                print(f"Dépense '{dep.nom}' supprimée !")
                return
        print (f"Aucune dépense trouvée avec l'ID {id}")