from datetime import date
from Depense import Depense
from BudgetManager import BudgetManager  # ta classe déjà écrite

def menu():
    print("\n=== Gestionnaire de Budget ===")
    print("1. Ajouter une dépense")
    print("2. Supprimer une dépense")
    print("3. Afficher toutes les dépenses")
    print("4. Total des dépenses")
    print("5. Quitter")
    choix = input("Choisis une option : ")
    return choix

def main():
    bm = BudgetManager()

    while True:
        choix = menu()

        if choix == "1":
            nom = input("Nom de la dépense : ")
            montant = float(input("Montant : "))
            categorie = input(f"Catégorie ({', '.join(bm.categorie)}) : ")
            dep = Depense(nom, montant, categorie, str(date.today()))
            bm.add_depense(dep)

        elif choix == "2":
            dep_id = int(input("ID de la dépense à supprimer : "))
            bm.delete_depense(dep_id)

        elif choix == "3":
            print("\n--- Liste des dépenses ---")
            bm.afficher_depenses()

        elif choix == "4":
            total = bm.total_depenses()
            print(f"Total des dépenses : {total} €")

        elif choix == "5":
            print("Au revoir !")
            break

        else:
            print("Option invalide, réessaie.")

if __name__ == "__main__":
    main()
