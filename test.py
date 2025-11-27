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

test_afficher_depense()