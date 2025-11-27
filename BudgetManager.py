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
        depense_trouve = False
        for dep in self.depenses :
            if dep.id == id:
                self.depenses.remove(dep)
                depense_trouve = True 
                break
        print (f"Aucune dépense trouvée avec l'ID {id}")
        
        sl = []
        with open(self.fichier_donnees, "r", newline="") as f:
            reader = csv.reader(f)
            for ligne in reader : 
                if str(ligne[0] != str(id)):
                    sl.append(ligne)
        with open(self.fichier_donnees, "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerows(sl) 
        print(f"Dépense avec id {id} supprimée !")

    def afficher_depenses(self):
        if not self.depenses : 
            print("Aucune dépense trouvée")
            return 
        for dep in self.depenses :
            print(f"ID: {id} | Nom: {dep.nom} | Montant {dep.montant}€" f"Catégorie: {dep.categorie} | Date: {dep.date}")

    def total_depenses(self):
        total = 0
        for dep in self.depenses:
            total += dep.montant
        return total

    def total_depenses_csv(self): 
        total = 0 
        try: 
            with open(self.fichier_donnees, "r") as f:
                reader = csv.reader(f)
                for row in reader :
                    toral += float(row[2])
        except FileNotFoundError: 
            return 0 
        return total
