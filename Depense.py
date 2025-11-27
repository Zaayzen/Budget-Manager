from datetime import date
class Depense:
    def __init__(self, nom, montant, categorie, date_depense = None):
        self.nom = nom
        self.montant = montant
        self.categorie = categorie
        if date_depense == None:
            self.date = str(date.today())
        else:
            self.date = date_depense
        self.id = None
