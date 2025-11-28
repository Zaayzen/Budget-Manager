from Depense import Depense
from BudgetManager import BudgetManager

def test_add_depense():
    manager = BudgetManager()

    dep1 = Depense("Essence", 70, "Transport", "2025-11-26")
    dep2 = Depense("Restaurant", 20, "Alimentation", "2025-11-26")
    manager.add_depense(dep1)
    manager.add_depense(dep2)
    assert len(manager.depenses) == 1
    assert manager.depenses[0].nom == "Essence"
    assert manager.depenses[0].montant == 70
    assert manager.depenses[1].nom == "Restaurant"
    assert manager.depenses[1].montant == 20


def test_delete_depense():
    manager = BudgetManager()

    dep1 = Depense("Essence", 70, "Transport", "2025-11-26")
    dep2 = Depense("Restaurant", 20, "Alimentation", "2025-11-26")

    manager.add_depense(dep1)
    manager.add_depense(dep2)

    assert len(manager.depenses) == 2

    manager.delete_depense(dep1.id)

    assert len(manager.depenses) == 1
    assert manager.depenses[0].nom == "Restaurant"
    assert manager.depenses[0].montant == 20

def test_afficher_depense():
    manager = BudgetManager()

    manager.add_depense(Depense("Essence", 60, "Transport", "2025-11-27"))
    manager.add_depense(Depense("Course", 40, "Alimentation", "2025-11-27"))

    manager.afficher_depenses()



def __init__(self, fichier_donnees = "depenses.csv"):
    self.depenses = [] 
    self.fichier_donnees = fichier_donnees
    self.categorie = ["Transport", "Alimentation", "Loisirs", "Autre"]
    self.next_id = 1
    self.charger_depenses()

def test_charger_depenses():
    import os
    if os.path.exists("depenses.csv"):
        os.remove("depenses.csv")

    print("=== TEST : Sauvegarde ===")
    bm1 = BudgetManager()

    dep1 = Depense("Essence", 50, "Transport")
    dep2 = Depense("Pizza", 12, "Alimentation")
    dep3 = Depense("JJJ", 20, "Autre")

    bm1.add_depense(dep1)
    bm1.add_depense(dep2)
    bm1.add_depense(dep3)

    print("Dépenses ajoutées dans bm1 :")
    bm1.afficher_depenses()

    print("\n=== TEST : Chargement ===")
    bm2 = BudgetManager()  # Ceci recharge le CSV automatiquement

    print("Dépenses chargées dans bm2 :")
    bm2.afficher_depenses()

    print("\n=== TEST : Total ===")
    print("Total bm1 :", bm1.total_depenses())
    print("\nLe prochain ID devrait être →", bm1.next_id)

test_charger_depenses()




