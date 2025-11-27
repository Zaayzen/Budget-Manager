import os
from BudgetManager import BudgetManager
from Depense import Depense

def test_sauvegarde_et_chargement():
    # On supprime l'ancien fichier s'il existe pour repartir propre
    if os.path.exists("depenses.csv"):
        os.remove("depenses.csv")

    print("=== TEST : Sauvegarde ===")
    bm1 = BudgetManager()

    dep1 = Depense("Essence", 50, "Transport")
    dep2 = Depense("Pizza", 12, "Alimentation")

    bm1.add_depense(dep1)
    bm1.add_depense(dep2)

    print("Dépenses ajoutées dans bm1 :")
    bm1.afficher_depenses()

    print("\n=== TEST : Chargement ===")
    bm2 = BudgetManager()  # Ceci recharge le CSV automatiquement

    print("Dépenses chargées dans bm2 :")
    bm2.afficher_depenses()

    print("\n=== TEST : Total ===")
    print("Total bm2 :", bm2.total_depenses())
